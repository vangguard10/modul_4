# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:26:21 2022

@author: fariz
"""

x = int(input('masukan nilai: '))
for i in range(x,0,-1):
    for k in range(i):
        print(i,end='')
    print('')