import cv2
import numpy as np


def contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    dy = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

    mag = np.sqrt(dx ** 2 + dy ** 2)
    angle = np.arctan2(dy, dx)

    thresh = 50
    mag[mag < thresh] = 0

    for y in range(1, mag.shape[0] - 1):
        for x in range(1, mag.shape[1] - 1):
            if mag[y][x] > 0:
                theta = angle[y][x]
                if theta < -np.pi / 4 or theta > np.pi / 4:
                    if mag[y][x] < mag[y - 1][x] or mag[y][x] < mag[y + 1][x]:
                        mag[y][x] = 0
                else:
                    if mag[y][x] < mag[y][x - 1] or mag[y][x] < mag[y][x + 1]:
                        mag[y][x] = 0

    mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    cv2.imshow("Contours", mag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("D:/School/PVSO/Projects/Zadanie_3/obrazocek.jpg")
contours(img)
