#! /usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------#
#                                                                       #
# Copyright (C) 2015, David A. Hall                                     #
#                     Eureka, MO USA                                    #
# This program is free software. You can redistribute it and/or modify  #
#   it under the terms of the GNU General Public License Version 2.     #
#   This program is distributed in the hope that it is useful,          #
#   but WITHOUT ANY WARRANTY IMPLIED OR OTHERWISE.                      #
#                                                                       #
#-----------------------------------------------------------------------#

__filename__ = "libframes.py"
__author__ = "David Hall"
__last_update__ = "11 April 2015"

import os
import sys
import cv2
import numpy as np


def simple_threshold(image, threshold, maxval, th_type):
    """Implements simple thresholding algorithm from OpenCV

    Arguments:
        image: image to threshold
        threshold: threshold value
                   > 0 and less than largest pixel value
        maxval: value of output pixel if image pixel is greater than threshold value
                range of values: 0 -> largest integer
        th_type: threshold type
                 accepts cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV,
                         cv2.THRESH_TRUNC,
                         cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV
    Returns a list:
        threshold value: integer
        thresholded image: numpy array"""
    ret, th_img = cv2.threshold(image, threshold, maxval, th_type)
    return th_img

def adaptive_threshold(image, maxval, ad_method, th_type, blk_size, constant):
    """Implements adaptive thresholding algorithm from OpenCV

    Arguments:
        image: source image
        maxval: value of output pixel if image pixel is greater than threshold value
                range of values: 0 -> largest integer
        ad_method: threshold algorithm
                   accepts cv2.ADAPTIVE_THRESH_MEAN_C,
                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        th_type: threshold type
                 accepts cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV
        blk_size: size of pixel neighborhood used to calculate threshol level
                  odd integer > 0 (3, 5, 7, etc.)
        constant: subtracted from mean
                  normally a postive integer
    Returns a list:
        thresholded image: numpy array"""
    return cv2.adaptiveThreshold(image, maxval, ad_method, th_type, blk_size, constant)

if __name__ == "__main__":
    from matplotlib import pyplot as plt

    img = cv2.imread('../test_frames/copernicus.tiff')
    white = 255
    levels = [(i * (img.max() - img.min())/4 + img.min()) for i in range(1, 4)]
    print('Image Range: ', img.max(), img.min())
    print('Thresholds: ', levels)

    for (title, type) in list((('Simple Binary', cv2.THRESH_BINARY),
                               ('Simple ToZero', cv2.THRESH_TOZERO))):
        for i in range(3):
            plt.subplot(2, 2, i + 1)
            level = i * (img.max() - img.min())/4 + img.min()
            plt.imshow(simple_threshold(img, level, white, type))
            plt.axis('off')
            plt.title(title + '  Threshold: ' + str(level))
        plt.subplot(2, 2, 4)
        plt.imshow(img)
        plt.axis('off')
        plt.title('Original')
        plt.show()

    for (title, method) in list((('Adaptive Mean', cv2.ADAPTIVE_THRESH_MEAN_C),
                                 ('Adaptive Gaussian', cv2.ADAPTIVE_THRESH_GAUSSIAN_C))):
        plt.subplot(2, 1, 1)
        plt.imshow(adaptive_threshold(img[..., 0], white, method, cv2.THRESH_BINARY, 11, 2))
        plt.axis('off')
        plt.title(title)
        plt.subplot(2, 1, 2)
        plt.imshow(img)
        plt.axis('off')
        plt.title('Original')
        plt.show()
