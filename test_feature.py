#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:46:19 2019

@author: nikhil133
"""
import imagepreprocessing as ip
import cv2
import time
import numpy as np
from math import floor
import pickle
def main():
    X=pickle.load(open("X.pickel","rb"))
    X=X/255
    dense=[]
    for i in range(X.shape[0]):
        x=X[i].reshape(X[i].shape[2],X[i].shape[0],X[i].shape[1])
        co=ip.convolutionlayer2d(x,4,3,3,1,0)
        pool=ip.maxpool(co,2,2,2)
        co=ip.convolutionlayer2d(pool,64,3,3,1,0)
        pool=ip.maxpool(co,2,2,2)
        
        dense.append(pool)
    print(np.array(dense).shape)
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
    #end=time.time()
    #print(pool)
    #print("cython timed ",end-strt)
    
    #cv2.imshow('image',co)
    #cv2.waitKey(5000)
    
if __name__=="__main__":
    main()
