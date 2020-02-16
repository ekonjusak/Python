from __future__ import division
import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import cos, sin

# https://www.youtube.com/watch?v=aBhUbN1ksto
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

def show(image):
    plt.figure(figsize=(10,10))
    plt.imshow(image, interpolation='nearest')

def overlay_mask(mask,image):
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5,0)
    return img

def find_bigest_contour(image):
    image= image.copy()
    _,contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APROX_SIMPLE )
    countour_sizes =[(cv2.contourArea(countour),countour) for countour in contours]
    biggest_contour = max(countour_sizes,key=lambda x:x[0])[1]
    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask,[biggest_contour],1,255,-1)

    return biggest_contour,mask

def circle_contour(image, contour):
    image_with_ellipse= image.copy()
    ellipse = cv2.fitEllipse(contour)
    cv2.ellipse(image_with_ellipse, ellipse, green, 2, cv2.CV_AA)
    return image_with_ellipse

# https://www.youtube.com/watch?v=aBhUbN1ksto

