import numpy as np

## imread
grey_img = cv2.imread('/home/img/python.png', cv2.IMREAD_GRAYSCALE)

## imwrite

# when using imwrite, it's important to know that it should be written out on a
# 255 scale
depth_clipped = np.where(depth <= 1., depth, 1.)
cv2.imwrite(f'./images/{image_name}_depth.png', depth_clipped*255)

## other stuff

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


def opencv_main_loop_example(args):
    
    # do parse args
    pass

    print("Initializing video capture")
    if camera is not None:
        capture = cv2.VideoCapture(camera)
    else:
        capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(video))
    if not capture.isOpened:
        print('Unable to open: ' + input)
        exit(0)

    # first frame waits for a keypress
    wait_time = 0
    iframe = 0

    if num_frames == 0:
        print('Running forever')
    else:
        print(f'Running for {num_frames} frames')

    while True:
        # grab the current frame and initialize the occupied/unoccupied
        # text
        ret, frame = capture.read()
        print(f'frame: {iframe}')

        cv2.imshow('image', frame)

        # handle loop control
        if iframe == 0:
            print('Press any key to continue (in popup window), or q to quit')
        key = cv2.waitKeyEx(wait_time) & 0xFF

        if key != 255:
            print(key)

        # Control logic:
        # - on first iter, don't interpret commands other than quit
        # - if any other key is pressed, then start looping
        # - after first iteration, proceed through remaining command logic
        # - can still press q at any time to quit

        # if the `q` key is pressed, break from the loop
        if key == ord("q"):
            break
        # On first iter, if another key pressed, set wait time to 1ms and loop
        elif iframe == 0:
            wait_time = 1
        # command logic after the first iteration
        elif iframe > 0:
            # pause/unpause, set wait_time to infinity, 1ms
            if key == ord("p"):
                wait_time = 0 if wait_time else 1
            # minus key - zoom out
            elif key == ord("-"):
                pass
            # plus (or equals) key - zoom in
            elif (key == ord("+") or key == ord("=")):
                pass
            # left arrow key (move center left)
            elif key == 81:
                pass
            # up arrow key
            elif key == 82:
                pass
            # right arrow key
            elif key == 83:
                pass
            # down arrow key
            elif key == 84:
                pass

        iframe += 1

        time.sleep(0)