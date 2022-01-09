
# linestyles:  see https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html


import matplotlib.pyplot as plt
import numpy as np

times = np.linspace(0,10, 11)
pos_error = np.random.rand((11, 3))

legend_comps = ['r (radial)', 'i (along-track)', 'c (normal)']


## Basic-est
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


## reset color cycler
fig, ax = plt.subplots(num=1, clear=True)
for imc_ind, mc_indx in enumerate(mc_indcs):
    # this resets for mc_indx
    ax.set_prop_cycle(None)
    for mt in opt_run_times[mc_indx]:
        horz_indcs = [mt, mt]
        vert_indcs = [mc_indx - 0.4, mc_indx + 0.4]
        ax.plot(...)


## subplots, combined xyz, flat legend
# plot_1.png
fig, axs = plt.subplots(4,1)
ax = axs[0]
ax.set_title('Omegas')
ax.plot(t_hist, np.linalg.norm(torque_out, axis=1))
ax.set_xlabel('time (s)')
ax.set_ylabel(f'Torque magnitude\n[Nm]')
ax.grid()
for icomponent, component in enumerate(['x', 'y', 'z']):
    ax = axs[icomponent + 1]
    ax.plot(t_hist, torque_out[:, icomponent])
    ax.set_xlabel('time (s)')
    ax.set_ylabel(f'Torque {component}\n[Nm]')
    ax.grid()


## subplots, separate xyz
# plot_2.png
fig, axs = plt.subplots(4,1)
ax = axs[0]
ax.set_title('Omegas')
ax.plot(t_hist, np.linalg.norm(omega_errors, axis=1))
ax.set_xlabel('time (s)')
ax.set_ylabel(f'omega error magnitude \n[deg/sec]')
ax.grid()
for icomponent, component in enumerate(['x', 'y', 'z']):
    ax = axs[icomponent + 1]
    ax.plot(t_hist, omega_errors[:, icomponent])
    ax.set_xlabel('time (s)')
    ax.set_ylabel(f'omega error {component}\n[deg/sec]')
    ax.grid()


# for text and arrow
ax.annotate('local max', xy=(3, 1),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )


# for just text
#  see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
#  see https://jakevdp.github.io/PythonDataScienceHandbook/04.09-text-and-annotation.html
ax.text(1.0, 0.9, "converted B -> N", ha="right",transform=ax.transAxes)
