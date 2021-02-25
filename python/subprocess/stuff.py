import subprocess


# https://docs.python.org/3/library/subprocess.html#subprocess.check_output
# If passing a single string, either shell must be True (see below) or else the string must simply name the program to be executed without specifying any arguments.
out = subprocess.check_output("ls -l", shell=True)

print(out.decode())

love information I love you too reba