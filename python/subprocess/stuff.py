import subprocess


## best (as of python 3.5)

# with terminal output
subprocess.run(['wget', url, '-O', path.join(repo_out_dir, filename)])  
# to totally suppress output at terminal
subprocess.run(['wget', url, '-O', path.join(repo_out_dir, filename)],  
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL)





# https://docs.python.org/3/library/subprocess.html#subprocess.check_output
# If passing a single string, either shell must be True (see below) or else the string must simply name the program to be executed without specifying any arguments.
out = subprocess.check_output("ls -l", shell=True)

print(out.decode())



## also

bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
