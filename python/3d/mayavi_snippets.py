# other useful links:
# - displaying the mesh on a map plot lib plot: https://stackoverflow.com/a/29430323/4292910

import cv2
import numpy as np

from mayavi import mlab

from v.cv.utils import remap_gray_image

depth = np.load('doublestrike.npy')
depth = remap_gray_image(depth)

h, w = depth.shape
y = np.arange(h)
x = np.arange(w)

x_m, y_m = np.meshgrid(x, y)

mlab.clf()

# see:
# http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html?highlight=contour_surf
# have to use transpose, because reasons... (it won't render correctly
# otherwise)
# mlab.surf(x_m.T, y_m.T, depth)

# see: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html?highlight=contour_surf#mesh
mlab.mesh(x_m, -1*depth, -1*y_m)
# mlab.show()

# view the file with: $ ctmviewer shape.obj
# note won't have color map
mlab.savefig("shape.obj")