#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:14:08 2019

@author: nikhil
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy
setup(
      ext_modules=cythonize("imagepreprocessing.pyx"),
      include_dirs=[numpy.get_include()]
)