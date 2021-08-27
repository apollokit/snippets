import matplotlib.pyplot as plt
import numpy as np

times = np.linspace(0,10, 11)
pos_error = np.random.rand((11, 3))

legend_comps = ['r (radial)', 'i (along-track)', 'c (normal)']

plt.figure(figsize=(10,5))
plt.plot(times, pos_error)
plt.xlabel('Time (s)')
plt.ylabel('Error (m)')
plt.title('Position Error')
# plt.legend(legend_comps)
plt.show()
plt.savefig('temp/pos_error.png')


# for 3 stacked subplots, looks like stacked.png in this directory

fig, ax = plt.subplots(3, 1, figsize=(10, 5))
ax[0].plot(times, pos_error.squeeze()[:,0])
ax[0].set_ylabel(f'{legend_comps[0]} (m)')
ax[0].get_xaxis().set_ticklabels([])
ax[0].grid()
ax[1].plot(times, pos_error.squeeze()[:,1], color='orange')
ax[1].set_ylabel(f'{legend_comps[1]} (m)')
ax[1].get_xaxis().set_ticklabels([])
ax[1].grid()
ax[2].plot(times, pos_error.squeeze()[:,2], color='green')
ax[2].set_ylabel(f'{legend_comps[2]} (m)')
ax[2].grid()
# labels
ax[0].set_title('Position Error - Hill Frame')
ax[2].set_xlabel('Time (s)')
plt.show()