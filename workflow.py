import subprocess

subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Automated commit message.'])
subprocess.call(['git', 'pull', 'origin', 'master'])
subprocess.call(['git', 'push', '-u', 'origin', 'master'])