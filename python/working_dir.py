import os
import shutil

os.chdir(os.path.dirname(__file__))

indint = 0
shutil.copytree('logs1', os.path.join('logs2', f'mc{indint}'))
