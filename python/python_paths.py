from os import path
from pathlib import Path

DATA_STORE_DIR = 'the_parent_dir'

# get absolute paths of every dir or file starting with "mc_" in the tree (search
#  recursively)
abs_paths = [dir_path.as_posix() for dir_path in Path(DATA_STORE_DIR).rglob('mc_*')]
            
# get rel paths to DATA_STORE_DIR
rel_paths = [path.relpath(abs_path, DATA_STORE_DIR) for abs_path in abs_paths]
        