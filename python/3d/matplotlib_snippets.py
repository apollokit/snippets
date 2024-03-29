# from:
# https://stackoverflow.com/questions/6539944/color-matplotlib-plot-surface-command-with-surface-gradient

# Python-matplotlib Commands
# from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def plot_surface_example():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, .25)
    Y = np.arange(-5, 5, .25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    Gx, Gy = np.gradient(Z) # gradients with respect to x and y
    G = (Gx**2+Gy**2)**.5  # gradient magnitude
    N = G/G.max()  # normalize 0..1
    surf = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1,
        facecolors=cm.jet(N),
        linewidth=0, antialiased=False, shade=False)
    plt.show()


ax.view_init(elev=90., azim=0.) # view from above
ax.plot3D(error_hill[first_slice, 1], error_hill[first_slice, 0], error_hill[first_slice, 2], 'k*', label='virt tug')