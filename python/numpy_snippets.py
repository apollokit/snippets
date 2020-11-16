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