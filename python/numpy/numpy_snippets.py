import numpy as np

# Make a diagonal matrix
np.diag([1,1,1])
# array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]])

# Using where
a = np.arange(10)
# a ... array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.where(a < 5, a, 10*a)
# array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])



# ignores errors like
# /Users/ktikennedy/starfish/Basilisk/basilisk_derived/dist3/Basilisk/utilities/RigidBodyKinematics.py:2069: RuntimeWarning: overflow encountered in double_scalars
#   C[0, 1] = 8 * q1 * q2 + 4 * q3 * S
with np.errstate(invalid='ignore'):
    thrust_force_N_convert[imc, itime, :] = np.matmul(
        rbk.MRP2C(sigma_BN[imc, itime, :]).T, force_b[:, itime])


# Print array with full precision
# np print
# np format long
# numpy format long
# printoptions
# print format long
# np suppress scientific notation
np.set_printoptions(precision=15, suppress=True)
print(array)

# print array with , separator
np.array2string(array, separator=', ')