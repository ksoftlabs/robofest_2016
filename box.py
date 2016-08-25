import cv2
import numpy as np
import image_process


class Box:
    def __init__(self,image):
        self.image=image
        imgp=image_process.Images(self.image)
        self.green_img = imgp.only_green()
        self.red_img=imgp.only_red()
        self.blue_img=imgp.only_blue()

    def box_detect(self):
        params = cv2.SimpleBlobDetector_Params()

        params.filterByCircularity = False
        params.minCircularity = 0

        detector = cv2.SimpleBlobDetector(params)

        keypoints = detector.detect(self.red_img)
        im_with_keypoints = cv2.drawKeypoints(self.image, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        return im_with_keypoints
