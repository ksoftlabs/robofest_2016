import cv2
import numpy as np
import math
import psutil
import global_values


def draw_machine_details(frame, fps):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    cv2.putText(frame, 'FPS ' + str(fps), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 0, 0))
    cv2.putText(frame, 'CPU usage ' + str(cpu), (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 0, 0))
    cv2.putText(frame, 'Memory usage ' + str(mem), (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 0, 0))


def get_gradient(x1, y1, x2, y2):
    x_diff = float(x2 - x1)
    if x_diff == 0.0:
        x_diff = 0.0000000000001
    return (y2 - y1) / x_diff


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def get_red_mask(frame_hsv):
        lower_red_mask = cv2.inRange(frame_hsv, global_values.lower_red1, global_values.upper_red1)
        upper_red_mask = cv2.inRange(frame_hsv, global_values.lower_red2, global_values.upper_red2)
        return lower_red_mask + upper_red_mask


def get_green_mask(frame_hsv):
    return cv2.inRange(frame_hsv, global_values.lower_green, global_values.upper_green)


def get_blue_mask(frame_hsv):
    return cv2.inRange(frame_hsv, global_values.lower_blue, global_values.upper_blue)


def apply_mask(original_frame, color='any'):
    frame_hsv = cv2.cvtColor(original_frame, cv2.COLOR_BGR2HSV)

    if color == 'red':
        frame_mask = get_red_mask(frame_hsv)
    elif color == 'green':
        frame_mask = get_green_mask(frame_hsv)
    elif color == 'blue':
        frame_mask = get_blue_mask(frame_hsv)
    else:       # Use all 3 colours for testing
        frame_mask = get_red_mask(frame_hsv) + get_green_mask(frame_hsv) + get_blue_mask(frame_hsv)

    return cv2.bitwise_and(original_frame, original_frame, mask=frame_mask)


def get_normal_threshold(gray_img, min_val=70, max_val=255, thresh_type=cv2.THRESH_BINARY):
    returned = False
    while not returned:
        returned, threshold_img = cv2.threshold(gray_img, min_val, max_val, thresh_type)
    return threshold_img


def get_otsu_threshold(gray_img):
    returned = False
    while not returned:
        returned, threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold_img


def get_otsu_gaussian_threshold(gray_img, width=3, height=3):
    blurred = cv2.GaussianBlur(gray_img, (width, height), 0)
    returned = False
    while not returned:
        returned, threshold_img = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold_img


def get_contours(img):
    _, contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


# Just detect and circle the significant points
def good_features_to_track(img):
    corners = cv2.goodFeaturesToTrack(img, 7, 0.01, 10)
    if corners is not None:
        corners = np.int0(corners)

        for i in corners:
            x, y = i.ravel()
            cv2.circle(img, (x, y), 3, 255, -1)
    else:
        print 'No corners found'


# Just detect and circle corners
def detect_corners(gray_img, original_img):
    gray = np.float32(gray_img)
    dst = cv2.cornerHarris(gray, 2, 29, 0.05)

    dst = cv2.dilate(dst, None)         # Result is dilated for marking the corners, not important

    # Threshold for an optimal value, it may vary depending on the image.
    original_img[dst > 0.1 * dst.max()] = [0, 0, 255]
