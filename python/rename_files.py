"""Recursively rename all the files under a given directory (but don't rename dirs)"""

from genericpath import isdir
import os
from os import path
import glob
import inflection

dir = '/Users/ktikennedy/starfish/Basilisk/basilisk_derived/src/Starfish/sim_configuration/run_files'

paths = [path.abspath(p) for p in glob.glob(path.join(dir, '**/*'), recursive=True)]

fp = open('renamed.csv', 'a')

for ipat, pat in enumerate(paths):
    # skip dirs
    if path.isdir(pat):
        continue

    dir_path = path.dirname(pat)
    file_name = path.basename(pat)

    new_name = file_name
    # new_name = new_name.replace('softwareScenario', 'sw_scenario')
    # new_name = new_name.replace('software_scenario', 'sw_scenario')
    # new_name = new_name.replace('sws', 'sw_scenario')
    # new_name = new_name.replace('tugConfiguration', 'tugconfig')
    # new_name = new_name.replace('nav_configuration', 'navconfig')
    # new_name = new_name.replace('scenario_', 'sim_scenario_')

# if '_tarconfig' in new_name:
    #     new_name = new_name.replace('_tarconfig', '')
    #     new_name = 'sw_tarconfig_' + new_name
    if '_simulation' in new_name:
        new_name = new_name.replace('_simulation', '')
    new_name = new_name.replace('run_', 'run_sim_')

    new_name = inflection.underscore(new_name)
    new_full_path = path.join(dir_path, new_name)
    
    if new_name != file_name:
        print(f'{ipat} rename {file_name} to {new_name}')
        os.rename(pat, new_full_path)
        fp.write(f'{file_name}, {new_name}\n')