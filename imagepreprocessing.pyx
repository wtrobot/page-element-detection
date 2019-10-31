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

#convolution layer with relu
cpdef np.ndarray[np.double_t,ndim=3] convolutionlayer2d(np.ndarray[np.double_t,ndim=3] metrics,int nf,int frow,int fcol,int stride,int padding):
    cdef int j=0
    cdef int i=0
    cdef int k=0
    cdef int f
    cdef int rgb=metrics.shape[0]
    cdef np.ndarray[np.double_t,ndim=3] bconv
    cdef np.ndarray[np.double_t,ndim=3] kernel=np.random.uniform(-2,2,[nf,frow,fcol]) 
    cdef np.ndarray[np.double_t,ndim=3] xp=np.zeros([rgb,padding,metrics.shape[2]])
    metrics=np.concatenate([xp,metrics],axis=1)
    metrics=np.concatenate([metrics,xp],axis=1)
    cdef np.ndarray[np.double_t,ndim=3] yp=np.zeros([rgb,metrics.shape[1],padding])
    
    metrics=np.c_[yp,metrics]
    metrics=np.c_[metrics,yp]
    cdef int r=floor((metrics.shape[1]+(2*padding)-kernel.shape[1]+1)/stride)
    cdef int c=floor((metrics.shape[2]+(2*padding)-kernel.shape[2]+1)/stride)

    cdef np.ndarray[np.double_t,ndim=2] conv=np.zeros([nf,r*c]) 

    cdef np.ndarray[np.double_t,ndim=3] bias=np.ones([nf,r,1])
    cdef int total
    cdef int d
    while k < r*c:

        if metrics.shape[2]-(i)>=kernel.shape[2]:
            for f in range(nf): 
                total=0
                for d in range(metrics.shape[0]):
                    total+=np.sum(metrics[d][j:j+frow,i:i+fcol]*kernel[f])
                
                conv[f][k]=max(0,total)
                

            i=i+stride
            k=k+1
        else:
            i=0
            j=j+(stride)

    conv.resize((nf,r,c))
    #bconv=np.c_[conv,bias]
    return conv


#maxpool
cpdef np.ndarray[np.double_t,ndim=3] maxpool(np.ndarray[np.double_t,ndim=3] metrics,int frow,int fcol,int stride):
    cdef int k=0
    cdef int j=0
    cdef int i=0
    
    cdef int r=floor((metrics.shape[1]-frow+1)/stride)
    cdef int c=floor((metrics.shape[2]-fcol+1)/stride)
    cdef np.ndarray[np.double_t,ndim=2]pool=np.zeros([metrics.shape[0],r*c])
     
    cdef int nf=metrics.shape[0]
    
    while k < r*c:

        if metrics.shape[2]-(i)>=fcol:
            for f in range(nf): 
                
                
                pool[f][k]=max(metrics[f][j:j+frow,i:i+fcol].flatten())
                
            i=i+stride
            k=k+1
        else:
            i=0
            j=j+(stride)
            
    pool.resize((metrics.shape[0],r,c))        
    return pool

