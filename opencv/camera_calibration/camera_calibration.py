# code from: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html

import numpy as np
import cv2
import glob
import json

# termination criteria
# documentation: https://docs.opencv.org/3.4/d9/d5d/classcv_1_1TermCriteria.html
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Number of inner corners per a chessboard row and column
# based on: https://shimat.github.io/opencvsharp_docs/html/e302fba7-86bb-0ccd-f8b8-228c390ae682.htm
pattern_size = (9, 6)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((pattern_size[0] * pattern_size[1] ,3), np.float32)
objp[:,:2] = np.mgrid[0:pattern_size[0],0:pattern_size[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('images/*.jpg')

for fname in images:
    print(fname)
    img = cv2.imread(fname)
    h,  w = img.shape[:2]

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
    # cv2.imshow('img',gray)
    # cv2.waitKey(500)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, pattern_size , None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        # uncomment to see the pattern drawn on the chessboard
        # cv2.imshow('img',img)
        # cv2.waitKey()
    else:
        print(f"Did not find chess board corners for {fname}")

## get calibration parameters

# mtx is the camera matrix
# dist are the distortion coefficients
# then the rotation and translation vectors
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints,
    gray.shape[::-1],None,None)

# these are all numpy arrays
out_params = {
    "mtx": mtx.tolist(),
    "dist": dist.tolist(),
    "rvecs": [vec.tolist() for vec in rvecs],
    "tvecs": [vec.tolist() for vec in tvecs],
}
with open('calculated_parameters.json', 'w') as f:
    json.dump(out_params, f)


## undistort first image

img = cv2.imread(images[0])
h,  w = img.shape[:2]

newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]

# combined = np.concatenate([img, dst], axis=1)
# cv2.imshow('combined', combined)
cv2.imshow('dst', dst)
cv2.waitKey()

# cv2.imwrite('calibresult.png',dst)


## calculate error

tot_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    tot_error += error

# not sure exactly what a good number is here, the original article is not
# that helpful
print("total error: ", tot_error/len(objpoints))


cv2.destroyAllWindows()
