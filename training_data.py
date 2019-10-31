#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:33:58 2019

@author: nikhil
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import random

dataDir="/Users/bon/wtbot/page-element-detection/training"
categories=["textbox"]


def create_training_data(path,categories):
    training_data=[]
    for category in categories:
        path=os.path.join(dataDir,category)
        class_num=categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img))
                newarray =cv2.resize(img_array,(50,50))
                training_data.append([newarray,class_num])
            except Exception as e:
                print("Exception ",e)
    return training_data            
        
data=create_training_data(dataDir,categories)
random.shuffle(data)

X=[]
Y=[]
for x,y in data:
    X.append(x)
    Y.append(y) 

X=np.asarray(X).reshape(-1,50,50,3)


import pickle
pickle_out=open("X.pickel","wb")
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out=open("Y.pickel","wb")
pickle.dump(X,pickle_out)
pickle_out.close()
