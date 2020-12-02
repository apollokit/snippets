# pip install PyYAML

import yaml

with open(file_name, 'r') as f:
    yo = yaml.load(f, Loader=yaml.FullLoader)