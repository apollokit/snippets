# See https://linuxize.com/post/bash-redirect-stderr-stdout/

# redirect the command output (stdout) to the file
command > file
command 1> file

# redirect stderr
command 2> file

# write to two different files
command 2> error.txt 1> output.txt

# To redirect stderr to stdout and have error messages sent to the same file as standard output
command > file 2>&1
command &> file

# redirect both standard output and standard error to grep
command 2>&1 | grep ERROR

# tee output
# https://stackoverflow.com/a/418899/4292910
# goes to both standard out and file
ls -a | tee output.file
# plus standard error
ls -a 2>&1 | tee output.file