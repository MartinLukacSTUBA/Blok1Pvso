import cv2
import numpy as np

img = cv2.imread("D:/School/PVSO/Projects/Zadanie_3/obrazocek.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelEdgeX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelEdgeY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)


mag = np.sqrt(sobelEdgeX ** 2 + sobelEdgeY ** 2)
angle = np.arctan2(sobelEdgeY, sobelEdgeX)


thresh = 30
mag[mag < thresh] = 0

for sobelEdgeY in range(1, mag.shape[0] - 1):
    for sobelEdgeX in range(1, mag.shape[1] - 1):
        if mag[sobelEdgeY][sobelEdgeX] > 0:
            theta = angle[sobelEdgeY][sobelEdgeX]
            if theta < -np.pi / 4 or theta > np.pi / 4:
                if mag[sobelEdgeY][sobelEdgeX] < mag[sobelEdgeY - 1][sobelEdgeX] or mag[sobelEdgeY][sobelEdgeX] < \
                        mag[sobelEdgeY + 1][sobelEdgeX]:
                    mag[sobelEdgeY][sobelEdgeX] = 0
            else:
                if mag[sobelEdgeY][sobelEdgeX] < mag[sobelEdgeY][sobelEdgeX - 1] or mag[sobelEdgeY][sobelEdgeX] < \
                        mag[sobelEdgeY][sobelEdgeX + 1]:
                    mag[sobelEdgeY][sobelEdgeX] = 0

mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow("Contours", mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
