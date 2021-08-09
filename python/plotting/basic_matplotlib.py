import matplotlib.pyplot as plt
import numpy as np

times = np.linspace(0,10, 11)
times = np.random.rand((11, 3))

plt.figure(figsize=(10,5))
plt.plot(times, pos_error)
plt.xlabel('Time (s)')
plt.ylabel('Error (m)')
plt.title('Position Error')
plt.show()
plt.savefig('temp/pos_error.png')