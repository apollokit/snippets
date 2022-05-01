# Recursively search files for lines with substring 'my search string' under top_dir

from pathlib import Path
import re
from os import path

top_dir = "my_dir"

abs_paths = [dir_path.as_posix() 
    for dir_path in Path(top_dir).rglob('log*')]

for file in abs_paths:
    for iline, line in enumerate(open(file, 'r')):
        if re.search('my search string', line):
            print(line)