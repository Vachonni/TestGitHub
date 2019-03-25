#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:41:36 2019

@author: nicholas
"""

import numpy as np

a = [1,2,3,4,5, 10, 11, 100]
b = [1,3,5,6, 11]
c = [1,2]
print(list(set(a).intersection(b)))
print(list(set(a).union(b)))
print(set(c) < set(a))

