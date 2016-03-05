__author__ = 'yicong'


import cv2
import numpy as np
import csv
import os
import sys

COIN_RADIUS = 0.02

imgfn = sys.argv[1]
img = cv2.imread(imgfn, 0)
# img = cv2.flip(img, 1)

def bpfilter(img, lf, hf):
    imgblur1 = cv2.GaussianBlur(img, (lf, lf), -1)
    imgblur2 = cv2.GaussianBlur(img, (hf, hf), -1)
    imgdiff = np.int32(imgblur1) - np.int32(imgblur2)
    imgdiff -= imgdiff.min()
    imgdiff = np.uint8(imgdiff)
    return imgdiff

if __name__ == '__main__':
    imgdiff = bpfilter(img, 11, 17)
    _, imgdiffbw = cv2.threshold(imgdiff,0, 255, cv2.THRESH_OTSU)
    # imgdiffbw = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,23,15)
    # erase some area for better contour detection
    imgdiffbw[:2, :] = 255
    imgdiffbw[-2:, :] = 255
    imgdiffbw[:, :2] = 255
    imgdiffbw[:, -2:] = 255
    # kernel = np.ones((5,5),np.uint8)
    # imgdiffbw = cv2.erode(imgdiffbw,kernel,iterations = 1)
    cv2.imwrite('imgdiffbw.png', imgdiffbw)

    imgdiffbw = cv2.resize(imgdiffbw,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
