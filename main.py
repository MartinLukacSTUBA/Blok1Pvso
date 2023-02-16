import cv2
import numpy as np

camera = cv2.VideoCapture(0)
i = 0
while True:
    return_value, image = camera.read()
    cv2.imshow('image', image)
    if cv2.waitKey(20) == 32:
        cv2.imwrite('test' + str(i) + '.jpg', image)
        i = i + 1
        if i == 4:
            img1 = cv2.imread(cv2.samples.findFile("test0.jpg"))
            img2 = cv2.imread(cv2.samples.findFile("test1.jpg"))
            img3 = cv2.imread(cv2.samples.findFile("test2.jpg"))
            img4 = cv2.imread(cv2.samples.findFile("test3.jpg"))
            vertical = np.concatenate((img1, img2), axis=0)
            vertical1 = np.concatenate((img3, img4), axis=0)
            horizontal = np.concatenate((vertical, vertical1), axis=1)

            # cv2.imshow("Display window", horizontal)
            cv2.imwrite("2x2.png", horizontal)
            shape = horizontal.shape

            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])

            firstQuarter = horizontal[0:int(shape[0] / 2), 0:int(shape[1] / 2)]
            dst1 = cv2.filter2D(firstQuarter, -1, kernel)
            horizontal[0:int(shape[0] / 2), 0:int(shape[1] / 2)] = dst1

            # secondQuarter = horizontal[0:int(shape[0] / 2), int(shape[1] / 2):int(shape[1])]
            # dst2 = cv2.rotate(secondQuarter, cv2.ROTATE_90_CLOCKWISE)
            # horizontal[0:int(shape[0] / 2), int(shape[1] / 2):int(shape[1])] = dst2

            red = horizontal[int(shape[0] / 2):shape[0], 0:int(shape[1] / 2)]
            red[:, :, 0] = 0
            red[:, :, 1] = 0
            horizontal[int(shape[0] / 2):shape[0], 0:int(shape[1] / 2)] = red
            cv2.imshow("Output1", horizontal)
            print(horizontal.shape, horizontal.dtype, horizontal.size)
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break
camera.release()
cv2.destroyAllWindows()
