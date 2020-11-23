#!/usr/bin/env python
# from: https://stackoverflow.com/q/52910944/4292910

import numpy as np
from mayavi import mlab
import vtk
from vtk.numpy_interface import dataset_adapter as dsa

# in_file = "airboat.obj"
in_file = "/home/kit/git/vinci/projects/afuera/3d_inpainting/depth/art_impressionist5_mesh.obj"


reader = vtk.vtkOBJReader()
reader.SetFileName(in_file)
reader.Update()

polydata = reader.GetOutput()
# it's actually a VTKArray, but isinstance(points, np.ndarray) is true
points: np.ndarray = dsa.WrapDataObject(polydata).Points

# np.min(x): -639
# np.max(x): 0
# np.min(y): 0
# np.max(y): 499
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]
# using the below, you see that x and y are still a plane
# when using: /home/kit/git/vinci/projects/afuera/3d_inpainting/depth/art_impressionist5_mesh.obj
# z = np.zeros(points.shape[0])


w = int(abs(np.min(x) - np.max(x))) + 1
h = int(abs(np.min(y) - np.max(y))) + 1

# re-construct a depth image from all of the coordinates, only taking the
# highest z value
# it's slow, but has to be done...
depth = np.zeros((h, w))
for x_coor, y_coor, z_val in zip(x, y, z):
    x_coor_real = int(abs(x_coor))
    y_coor_real = int(abs(y_coor))
    val = depth[y_coor_real, x_coor_real]
    depth[y_coor_real, x_coor_real] = max(val, z_val)


# y_sort_indcs = np.argsort(y)
# x_sorted = x[y_sort_indcs]
# y_sorted = y[y_sort_indcs]
# z_sorted = z[y_sort_indcs]

# split_indcs = np.where(np.diff(y_sorted))[0] + 1
# x_split = np.split(x_sorted, split_indcs)
# y_split = np.split(y_sorted, split_indcs)
# z_split = np.split(z_sorted, split_indcs)


# see: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html?highlight=contour_surf#mesh
# mlab.points3d(x, y, z)

y_range = np.arange(h)
x_range = np.arange(w)

x_m, y_m = np.meshgrid(x_range, y_range)

mlab.figure(size=(1280,720))

# see: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html?highlight=contour_surf#mesh
mlab.mesh(-1*x_m, y_m, depth)

mlab.show()    
