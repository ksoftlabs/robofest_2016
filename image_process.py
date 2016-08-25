import cv2
import global_values

class Images:
    def __init__(self,frame):
        self.image= frame
        cv2.namedWindow("Test")



    def get_contours(self,image):
        imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(imgray, (3, 3), 0)
        ret,thresh = cv2.threshold(blurred,50,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('Test',thresh)
        return contours

    def only_red(self):
        frame=self.image
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red_mask = cv2.inRange(hsv, global_values.lower_red1, global_values.upper_red1)
        upper_red_mask = cv2.inRange(hsv, global_values.lower_red2, global_values.upper_red2)

        mask = lower_red_mask + upper_red_mask

        return cv2.bitwise_and(frame,frame, mask= mask)

    def only_blue(self):
        frame=self.image
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, global_values.lower_blue, global_values.upper_blue)
        return cv2.bitwise_and(frame,frame, mask= mask)

    def only_green(self):
        frame=self.image
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, global_values.lower_green, global_values.upper_green)
        return cv2.bitwise_and(frame,frame, mask= mask)