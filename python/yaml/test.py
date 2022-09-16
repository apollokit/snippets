""

import os
import yaml
# pip install pyyaml-include
from yamlinclude import YamlIncludeConstructor

YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir='.')

with open('testb1.yml') as f:
    data = yaml.load(f)
    # data = yaml.load(f)

print(data)


# class MyLoader(yaml.SafeLoader):
#     def __init__(self, stream):
#         self._root = os.path.split(stream.name)[0]
#         super(MyLoader, self).__init__(stream)
#     def include(self, node):
#         filename = os.path.join(self._root, self.construct_scalar(node))
#         with open(filename, 'r') as f:
#             a=1
#             return yaml.load(f, MyLoader)

# MyLoader.add_constructor('!include', MyLoader.include)

# with open('testb1.yml') as f:
#     data = yaml.load(f, MyLoader)

# print(data)

# import hiyapyco
# # conf = hiyapyco.load('testc0.yml', 'testc1.yml', method=hiyapyco.METHOD_MERGE, interpolate=True, failonmissingfiles=True)
# conf = hiyapyco.load('testc0.yml', 'testc1.yml', method=hiyapyco.METHOD_SIMPLE, interpolate=True, failonmissingfiles=True)

# print(conf)

a=1