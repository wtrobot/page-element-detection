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
    print(m," ",n," ",c)
    co=ip.convolution3D(img,m,n,c)
    print(co.shape)
    #co=ip.convolution3D(co,co.shape[0],co.shape[1],co.shape[2]*2)
    #pool=ip.maxPool(co,co.shape[0],co.shape[1],c,3,3,stride=2)
    #print(pool.shape[0]," ",pool.shape[1]," ",c)
    #co=ip.convolution3D(pool,pool.shape[0],pool.shape[1],c)
    #print(co.shape[0]," ",co.shape[1]," ",c)
    #pool=ip.maxPool(co,co.shape[0],co.shape[1],c,3,3,stride=2)
    #print(pool.shape[0]," ",pool.shape[1]," ",c)
    #co=ip.convolution3D(pool,pool.shape[0],pool.shape[1],c)
    #print(co.shape[0]," ",co.shape[1]," ",c)
    #pool=ip.maxPool(co,co.shape[0],co.shape[1],c,3,3,stride=2)
    #print(pool.shape[0]," ",pool.shape[1]," ",c)
    end=time.time()
    print("cython timed ",end-strt)
    
    cv2.imshow('image',co)
    cv2.waitKey(5000)
    
if __name__=="__main__":
    main()
