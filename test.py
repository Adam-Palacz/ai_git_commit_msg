import subprocess

output = subprocess.check_output(['git', 'diff', '--', '.']).decode('utf-8')
with open('test.txt', 'w') as file:
    file.write(output)

