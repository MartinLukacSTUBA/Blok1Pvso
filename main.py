import cv2
import numpy as np

camera = cv2.VideoCapture(0)
i = 0
while True:
    return_value, image = camera.read()
    cv2.imshow('image', image)
    if cv2.waitKey(1) == 32:
        cv2.imwrite('test' + str(i) + '.jpg', image)
        i = i + 1
        print(i)
        if i == 4:
            img1 = cv2.imread(cv2.samples.findFile("test0.jpg"))
            img2 = cv2.imread(cv2.samples.findFile("test1.jpg"))
            img3 = cv2.imread(cv2.samples.findFile("test2.jpg"))
            img4 = cv2.imread(cv2.samples.findFile("test3.jpg"))
            vertical = np.concatenate((img1, img2), axis=0)
            vertical1 = np.concatenate((img3, img4), axis=0)
            horizontal = np.concatenate((vertical, vertical1), axis=1)

            # cv2.imshow("Display window", horizontal)
            horizontal = cv2.resize(horizontal, (900, 900))
            cv2.imwrite("2x2.png", horizontal)
            shape = horizontal.shape

            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            firstQuarter = horizontal[0:int(shape[0] / 2), 0:int(shape[1] / 2)]
            dst1 = cv2.filter2D(firstQuarter, -1, kernel)
            horizontal[0:int(shape[0] / 2), 0:int(shape[1] / 2)] = dst1

            secondQuarter = horizontal[0:int(shape[0] / 2), int(shape[1] / 2):int(shape[1])]
            dst2 = np.zeros((secondQuarter.shape[1], secondQuarter.shape[0], 3), dtype=np.uint8)
            for i in range(secondQuarter.shape[0]):
                for j in range(secondQuarter.shape[1]):
                    dst2[j, secondQuarter.shape[0] - 1 - i] = secondQuarter[i, j]
            horizontal[0:int(shape[0] / 2), int(shape[1] / 2):int(shape[1])] = dst2

            red = horizontal[int(shape[0] / 2):shape[0], 0:int(shape[1] / 2)]
            red[:, :, 0] = 0
            red[:, :, 1] = 0
            horizontal[int(shape[0] / 2):shape[0], 0:int(shape[1] / 2)] = red
            cv2.imshow("Output1", horizontal)
            print(horizontal.shape, horizontal.dtype, horizontal.size)
            i = 0
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break
camera.release()
cv2.destroyAllWindows()
