#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:46:19 2019

@author: nikhil133
"""
import imagepreprocessing as ip
def main():
    img,m,n,c=ip.readImage("image/studentregistrationform.png")
    print(img)
    print("row : ",m," column : ",n," channel : ",c)
if __name__=="__main__":
    main()
