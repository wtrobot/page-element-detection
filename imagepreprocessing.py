#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:59:02 2019

@author: nikhil133
"""
import numpy as np
import cv2

#reads an image and return numpy array and its dimension row,column,channel
def readImage(image_path):
    img=np.asarray(cv2.imread(image_path))
    return img,img.shape[0],img.shape[1],img.shape[2]