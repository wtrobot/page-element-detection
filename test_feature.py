#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:46:19 2019

@author: nikhil133
"""
import imagepreprocessing as ip
import cv2
import time

def main():
    img,m,n,c=ip.readImage("image/studentregistrationform.png")
    
    strt=time.time()
    co=ip.convolution3D(img,m,n,c)
    end=time.time()
    print("cython timed ",end-strt)
    
    cv2.imshow('image',co)
    cv2.waitKey(1000)
    
if __name__=="__main__":
    main()
