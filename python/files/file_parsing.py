import numpy as np

## import a text file with multiple lines of values of the same data type

# example of file
# UTIAS Multi-Robot Cooperative Localization and Mapping Dataset
# produced by Keith Leung (keith.leung@robotics.utias.utoronto.ca) 2009
# Barcode Data Fomat:
# Subject #    Barcode #
#   1        5 
#   2       14 
#   3       41 
#   4       32 
#   5       23 
#   6       72 
#   7       27 
#   8       54 
#   9       70 

barcodes_raw = np.genfromtxt(file_path, dtype=np.int, skip_header=4)
# barcodes_raw
# array([[1, 5],
#        [2, 14],
#        [3, 41]
#        ....])
