import json
import logging
import subprocess
import os
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

AI_MODEL = "claude-3-haiku-20240307"

AI_SYSTEM_TEMPLATE = """
You will be acting as a helpful software developer that generates descriptive
git commit messages based on git diff output.
Here are the steps to follow:
First, I will provide the git diff output for the commit in question:

<git_diff>
GIT_DIFF
</git_diff>

Carefully review this diff and identify the key changes
that were made in this commit. Consider things like:
- Which files were added, modified or deleted
- For modified files, what was the nature of the changes
  (new features, bug fixes, refactoring, etc.)
- Are the changes related to a particular feature, task or bugfix
- Generated message should be very general and very simple
- Dont use more than 10 words in message
- Avoid any additional messages and mentions about git diff in response

Write your generated commit message as JSON {\"commit_message\": \"message\"}.
Example: {\"commit_message\": \"Add new resource group rg-wsb-etc\"}
"""


def generate_ai_commit_message(git_diff: str) -> str:
    """
    Generate a commit message using the AI
    model based on the provided git diff.

    Args:
        git_diff (str): The git diff output.

    Returns:
        str: The generated commit message.
    """
    client = anthropic.Anthropic(api_key=os.getenv("API_KEY"))

    message = client.messages.create(
        model=AI_MODEL,
        max_tokens=1500,
        temperature=0,
        system=AI_SYSTEM_TEMPLATE,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": git_diff
                    }
                ]
            }
        ]
    )

    ai_message = message.content[0].text
    commit_message = json.loads(ai_message)['commit_message']
    return commit_message


def main():
    """
    Main function to generate and apply the commit message.
    """
    script_dir = Path(__file__).resolve().parent
    git_diff_file = script_dir / "git_diff.txt"

    try:
        output = subprocess.check_output(['git', 'diff', '--', '.']).decode('utf-8')

        git_diff = "<git_diff>\n" + output + "\n<git_diff>"

        commit_message = generate_ai_commit_message(git_diff)

        print("\n#########")
        print("Commit message: " + commit_message)
        print("#########")

        command = input("Enter - accept commit message | Any other key - discard commit message: ")
        if command != "":
            print("Commit message discarded")
            return

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error occurred while running git commands: {e}")


if __name__ == "__main__":
    main()
