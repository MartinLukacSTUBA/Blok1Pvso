import glob

import cv2
import numpy as np

camera = cv2.VideoCapture(0)
i = 0
while True:
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    objp = np.zeros((6 * 7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

    objPoints = []
    imgPoints = []

    images = glob.glob('C:\Users\mario\Desktop\Predmety\2. ing\VZI\Blok1Pvso\úloha2/**/*.jpg', recursive= True)

    return_value, image = camera.read()
    cv2.imshow('image', image)
    if cv2.waitKey(1) == 32:
        cv2.imwrite('calibration' + str(i) + '.jpg', image)
        i = i + 1
        print(i)
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break
camera.release()
cv2.destroyAllWindows()
