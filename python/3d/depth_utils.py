import cv2
import numpy as np

def fill_depth_holes(depth: np.ndarray) -> np.ndarray:
    """Fill small holes (pixel value == 0) in a depth image 

    Due to distortions from a perfect x, y grid in a depth mesh, there can be
    holes at certain pixel locations. These are currently zero. fix this by
    taking the average of the non-zero nearest neighbor values.
        
    Args:
        depth: the depth image, two dimensional array with values being depth
    
    Returns:
        the depth image with holes filled in
    """

    # get a mask of pixels that are nonzero
    # see https://java2blog.com/cv2-threshold-python/
    _, thresholded = cv2.threshold(depth, 1.0, 1, cv2.THRESH_BINARY)
    # count how many pixels in each 3 by 3 square are nonzero
    kernel = np.ones((3,3), np.float32)
    local_num_nonzero = cv2.filter2D(thresholded, -1, kernel)
    # possible to have neighborhoods of all zeros...just set that to 1 (won't
    # matter anyway, because we'll be dividing 0 by 1 to get the average)
    local_num_nonzero = np.where(local_num_nonzero == 0, 1, local_num_nonzero)
    # figure out the average value for non-zeros within each 3 by 3 square
    depth_filler = cv2.filter2D(depth, -1, kernel) / local_num_nonzero
    # fill in the holes wherever there's a zero
    depth = np.where(depth == 0, depth_filler, depth)
    return depth