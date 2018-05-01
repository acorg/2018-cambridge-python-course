import subprocess

result = subprocess.run(['date | wc'],
                        shell=True,
                        stdout=subprocess.PIPE,
                        universal_newlines=True)

print(result.stdout[:-1])
