import glob

import cv2
import numpy as np

camera = cv2.VideoCapture(0)
i = 0
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

            objp = np.zeros((6 * 7, 3), np.float32)
            objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

            objPoints = []
            imgPoints = []

            images = glob.glob(r'C:\Users\mario\Desktop\Predmety\2. ing\VZI\Blok1Pvso\uloha2\**.jpg', recursive=True)

            for fName in images:
                img = cv2.imread(fName)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                ret, corners = cv2.findChessboardCorners(gray, (7, 5), None)
                print(corners)
                if ret:
                    objPoints.append(objp)
                    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                    imgPoints.append(corners2)
                ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, gray.shape[::-1], None, None)
                print("fy a fx: " + objPoints, "cy a cx" + imgPoints)
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break
camera.release()
cv2.destroyAllWindows()
