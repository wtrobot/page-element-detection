#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:59:02 2019

@author: nikhil133
"""
#import numpy as npp
import numpy as np
cimport numpy as np
import cv2
from math import floor
#reads an image and return numpy array and its dimension row,column,channel
'''
def readImage(image_path):
    img=np.asarray(cv2.imread(image_path))
    return img,img.shape[0],img.shape[1],img.shape[2]
'''
#detects vertical and horizontal edge with 3x3 kernel for RGB channel
#default stride=1 and padding 0
'''
cpdef float summation(np.ndarray[double,mode="c",ndim=2] arr):
    cdef float sums=0.0
    cdef int i,j
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            sums+=arr[i][j]
    return sums 
'''   
def readImage(image_path):
    cdef np.ndarray[np.double_t,ndim=3] img
    img=np.asarray(cv2.imread(image_path)).astype(float)
    return img,int(img.shape[0]),int(img.shape[1]),int(img.shape[2])

cpdef np.ndarray[np.double_t,ndim=3] convolution3D(np.ndarray[np.double_t,ndim=3] img_arr,int row, int col,int channel,int padding=0,int stride=1):
    
    cdef np.ndarray[np.double_t,ndim=2] V_kernel=np.array([(1.0,1.0,1.0),(1.0,-8.0,1.0),(1.0,1.0,1.0)])
    cdef np.ndarray[np.double_t,ndim=2] H_kernel=V_kernel.T
    cdef float r=floor((row+2*padding-V_kernel.shape[0]+1)/stride)
    cdef float c=floor((col+2*padding-V_kernel.shape[1]+1)/stride)
    cdef np.ndarray[np.double_t,ndim=3] conv
    conv = np.zeros([int(r),int(c),int(channel)],dtype=np.double)
    
    cdef np.ndarray[np.double_t,ndim=3] seg_holder=np.zeros([V_kernel.shape[0],V_kernel.shape[1],int(channel)])
    cdef int l=0
    cdef int k=0
    cdef int i
    cdef int j
    cdef int q
    cdef int w    
    for i in range(conv.shape[0]):
        
        for j in range(conv.shape[1]):
            k=i
            
            for q in range(seg_holder.shape[0]):
                if j!=0:
                    l= j + (stride-1)
                else:
                    l=j
                
                for w in range (seg_holder.shape[1]):
                    seg_holder[q][w][0]=img_arr[k][l][0]
                    seg_holder[q][w][1]=img_arr[k][l][1]
                    seg_holder[q][w][2]=img_arr[k][l][2]
                    l+=1
                k+=1
                
            conv[i][j][0]=np.sum(np.multiply(seg_holder[:][0],V_kernel))
            
            conv[i][j][1]=np.sum(np.multiply(seg_holder[:][1],V_kernel))
            
            conv[i][j][2]=np.sum(np.multiply(seg_holder[:][2],V_kernel))
          
    return conv