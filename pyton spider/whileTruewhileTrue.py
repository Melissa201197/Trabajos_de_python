# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:36:19 2021

@author: USER
"""

while True:
    x=input("Ingrese el # que debe contar: ")
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y > x:
            break