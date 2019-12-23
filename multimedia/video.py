import subprocess
import json

the_file = '~/temp/Acorn_Woodpecker_00001.mp4'

# https://docs.python.org/3/library/subprocess.html#subprocess.check_output
# If passing a single string, either shell must be True (see below) or else the string must simply name the program to be executed without specifying any arguments.
out_json = subprocess.check_output([f'ffprobe -i {the_file}  -v quiet '
    '-print_format json -show_format -show_streams -hide_banner'], shell=True)

print(json.loads(out_json))

