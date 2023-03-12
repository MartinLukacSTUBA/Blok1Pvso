import glob

import cv2
import numpy as np

camera = cv2.VideoCapture(0)
i = 0
a = 0
while True:
    return_value, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    if cv2.waitKey(1) == 32:
        cv2.imwrite('calibration' + str(i) + '.jpg', image)
        i = i + 1
        print(i)
        if i == 10:
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            objp = np.zeros((7 * 5, 3), np.float32)
            objp[:, :2] = np.mgrid[0:7, 0:5].T.reshape(-1, 2)

            objPoints = []
            imgPoints = []

            images = glob.glob(r'D:\School\PVSO\Projects\uloha1\**.jpg', recursive=True)
            # D:\School\PVSO\Projects\uloha2\**.jpg
            # C:\Users\mario\Desktop\Predmety\2. ing\VZI\Blok1Pvso\uloha2\**.jpg

            for fName in images:
                img = cv2.imread(fName)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                ret, corners = cv2.findChessboardCorners(gray, (7, 5), None)
                print(ret)
                if ret == True:
                    objPoints.append(objp)
                    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                    imgPoints.append(corners2)
                    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, gray.shape[::-1], None,
                                                                       None)
                    a = a + 1
                    print(a)
                    if a == 10:
                        calibration = cv2.imread('calibration9.jpg')
                        h, w = calibration.shape[:2]
                        newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
                        dst = cv2.undistort(calibration, mtx, dist, None, newCameraMtx)
                        cv2.imwrite('calibResult.jpg', dst)
                        print(newCameraMtx)
                else:
                    print("Nevysiel nam ret==True")
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break

camera.release()
cv2.destroyAllWindows()

# #Here starts task 3 !
# # Load calibration result
calib_result = cv2.imread('calibResult.jpg')
h, w = calib_result.shape[:2]

# Load camera and start capturing frames
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Undistort the frame using the calibration parameters
    new_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    undistorted = cv2.undistort(frame, mtx, dist, None, new_mtx)

    # Convert the frame to grayscale and reduce noise
    gray = cv2.cvtColor(undistorted, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Detect circles using the Hough transform
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows/8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)

    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(undistorted, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(undistorted, center, radius, (255, 0, 255), 3)

    # Display the frame
    cv2.imshow('detected circles', undistorted)

    # Wait for user input to exit
    if cv2.waitKey(1) == 120:
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

# camera = cv2.VideoCapture(0)
# i = 0
# a = 0
# while True:
#     return_value, image = camera.read()
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('image', gray)
#     key = cv2.waitKey(1)
#     if key == 120:  # exit on X
#         break
# camera.release()
# cv2.destroyAllWindows()
