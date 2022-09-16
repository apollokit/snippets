"from https://pypi.org/project/ruamel.yaml/0.10.2/"

import ruamel.yaml
import yaml

# inp = """\
# - &CENTER {x: 1, y: 2}
# - &LEFT {x: 0, y: 2}
# - &BIG {r: 10}
# - &SMALL {r: 1}
# # All the following maps are equal:
# # Explicit keys
# - x: 1
#   y: 2
#   r: 10
#   label: center/big
# # Merge one map
# - <<: *CENTER
#   r: 10
#   label: center/big
# # Merge multiple maps
# - <<: [*CENTER, *BIG]
#   label: center/big
# # Override
# - <<: [*BIG, *LEFT, *SMALL]
#   x: 1
#   label: center/big
# """

# yamlobj = YAML()

# data = yamlobj.load(inp)
# # assert data[7]['y'] == 2
# print(data)

# with open('out.yml', 'wb') as f:
#     yamlobj.dump(data, f)

inp = """\
- &CENTER {x: 1, y: 2}
# Merge one map
- <<: *CENTER
  r: 10
  label: center/big
"""

# data = ruamel.yaml.load(inp, ruamel.yaml.RoundTripLoader)
data = yaml.load(inp)
# assert data[7]['y'] == 2
print(data)

with open('out.yml', 'w') as f:
    yaml.dump(data, f)

a=1