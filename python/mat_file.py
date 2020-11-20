## load a large .mat file, and cache the items of interest to pickle so they
# don't have to be loaded from the large file next time

# need to use h5py for newer .mat files
import h5py
import scipy

file = 'rgbd/nyu_depth_v2/nyu_depth_v2_labeled.mat'
pkl_file = 'rgbd/nyu_depth_v2/img.pkl'

if os.path.exists(pkl_file):
    img, depth = unpickle_thing(pkl_file)
else:
    import h5py
    with h5py.File(file, 'r') as f:
        f.keys()

        images = f['images'][()]
        depths = f['depths'][()]
        pickle_thing((img, depth), pkl_file)


# can use scipy.io for older .mat files
mat = scipy.io.loadmat(file)