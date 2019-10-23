#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:54:38 2019

@author: bon
"""

import numpy
cimport numpy

cpdef numpy.ndarray[numpy.double_t,ndim=1]test():
    cdef numpy.ndarray[numpy.double_t,ndim=3] out
    out = numpy.zeros([100,100,3],dtype=numpy.double)
    return out