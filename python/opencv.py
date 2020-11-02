import numpy as np

def show_cv2_image(image: np.ndarray):
    """Use cv2 imshow to show an image
    
    includes the boilerplate around imshow necessary to actually see the image
     and close it gracefully
    
    Args:
        image:  the image as a numpy array
    """
    import cv2
    # Displaying the image
    cv2.imshow('image', image)
    # waits for user to press any key
    cv2.waitKey(0)
    # close all open windows after the keypress
    cv2.destroyAllWindows()