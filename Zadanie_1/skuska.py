from ximea import xiapi
import cv2
import os

cam = xiapi.Camera()  # use xiapi cam
cam.open_device()

# open camera
# camera settings cOn. set_exposure (10000)
cam.set_param('imgdataformat', 'XI_RGB32')
cam.set_param('auto_wb', 1)

# get into working directory
img = xiapi.Image()
# create instance to store. image
cam.start_acquisition()  # start data inquisiton

a = " "
iteracia = 1

while (1):

    cam.get_image (img)

    # if cv2.waitKey() != ord(' '): #cv2.waitKey (1) :
    #
    # cam.get_image (img)
    image = img.get_image_data_numpy()
    image = cv2. resize(image, (240 ,240))
    cv2. imshow("test", image)
    a = cv2.waitKey(1)

    if a == ord('c'):

        filename = "ing" + str(iteracia) + " . jpg"
        cv2.imwrite(filename, image)
        iteracia = iteracia + 1

    if a == ord('q'):
        break

cam.stop_acquisition()
cam.close_device()
# stop data acquisition
# stop communication