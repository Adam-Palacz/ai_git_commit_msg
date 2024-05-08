# AI-Powered Git Commit Message Generator

## Introduction
This project is a Python script that uses an AI model to generate descriptive git commit messages based on the changes in a git repository. The script retrieves the git diff output, passes it to the AI model, and generates a concise and informative commit message that can be used to commit the changes.

## Installation
1. Clone the repository:
```
git clone https://github.com/Adam-Palacz/ai_git_commit_msg
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Set the `API_KEY` environment variable with your Anthropic API key:
```
export API_KEY=your_anthropic_api_key
```

## Usage
To generate and apply a commit message, run the following command:
```
python main.py
```
The script will:
1. Retrieve the git diff output and save it to a temporary file.
2. Pass the git diff to the AI model and generate a commit message.
3. Print the generated commit message.
4. Add the changes to the git staging area.
5. Commit the changes with the generated message.
6. Push the commit to the remote repository.

## Code Structure
The main components of the code are:

1. `generate_ai_commit_message(git_diff: str) -> str`: This function takes the git diff output as input and generates a commit message using the Anthropic AI model.
2. `main()`: This is the entry point of the script, which retrieves the git diff, generates the commit message, and applies the commit.

The script also uses the following libraries:
- `json`: For parsing and generating JSON data.
- `logging`: For logging error messages.
- `subprocess`: For running git commands.
- `os`: For interacting with the operating system.
- `pathlib`: For working with file paths.
- `anthropic`: For interacting with the Anthropic AI model.
- `dotenv`: For loading environment variables from a `.env` file.

## Notable Features
- **AI-Powered Commit Message Generation**: The script leverages an AI model to generate concise and informative commit messages based on the changes in the git repository.
- **Automated Commit Process**: The script automates the entire commit process, including adding the changes to the staging area, committing the changes, and pushing the commit to the remote repository.
- **Error Handling**: The script includes error handling to catch any issues that may occur during the git command execution.

## Contributing
If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Contributions are welcome!

## License
This project is licensed under the [MIT License](LICENSE).