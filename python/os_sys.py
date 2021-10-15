# get all subdirs in input_dat_directory
folders = sorted([os.path.join(input_dat_directory, f.name) for f in os.scandir(input_dat_directory) if f.is_dir()])