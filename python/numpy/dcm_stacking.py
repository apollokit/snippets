# stacking two 16-long unit 3-vectors into the first two rows of a DCM
import numpy as np

x_hat.shape
# (16, 3)
y_hat.shape
# (16, 3)

np.stack((x_hat, y_hat), axis=2).shape
# (16, 3, 2)

yo = np.stack((x_hat, y_hat), axis=2)

yo[0,0,0]
# 0.025227504428857083
x_hat[0,0]
# 0.025227504428857083

x_hat[0,2]
# -0.24798343369878786
yo[0,2,0]
# -0.24798343369878786

yo[0,0,1]
# 0.014198004485760907
y_hat[0,0]
# 0.014198004485760907

yo[0,2,1]
# 0.0007993029462308103
y_hat[0,2]
# 0.0007993029462308103

## for full DCM, use
z_hat.shape
# (16, 3)
dcm = np.stack((x_hat, y_hat, z_hat), axis=2)
np.stack((x_hat, y_hat, z_hat), axis=2).shape
# (16, 3, 3)

pos_error.shape
# (16, 3)

# expand dims to turn each pos_error into a column vector (16, 3, 1)
rotated = dcm @ np.expand_dims(pos_error, axis=2)