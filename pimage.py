#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:46:44 2019

@author: bon
"""
import numpy as np
from math import floor


def convolution3D(img_arr,row,col,channel,padding=0,stride=1):
    
    V_kernel=np.array([(1,1,1),(1,-8,1),(1,1,1)])
    H_kernel=V_kernel.T
    r=floor((row+2*padding-V_kernel.shape[0]+1)/stride)
    c=floor((col+2*padding-V_kernel.shape[1]+1)/stride)
    
    conv = np.zeros([r,c,channel])
    
    #H_conv = np.zeros([r,c,channel])
    #cdef float conv = np.zeros([r,c,channel])
    seg_holder=np.zeros([V_kernel.shape[0],V_kernel.shape[1],channel])
    l=0
    k=0
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
           # print("seg_holder ",seg_holder[:][0])
           # print("V_conv ",V_conv[i][j][0])
            #H_conv[i][j][0]=np.sum(np.multiply(seg_holder[:][0],H_kernel))
            
            conv[i][j][1]=np.sum(np.multiply(seg_holder[:][1],V_kernel))
            #H_conv[i][j][1]=np.sum(np.multiply(seg_holder[:][1],H_kernel))
            
            conv[i][j][2]=np.sum(np.multiply(seg_holder[:][2],V_kernel))
            #H_conv[i][j][2]=np.sum(np.multiply(seg_holder[:][2],H_kernel))
    #conv=np.sqrt(pow(V_conv,2.0) + pow(H_conv,2.0))        
    #,H_conv
    
    return conv 