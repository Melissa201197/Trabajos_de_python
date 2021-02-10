# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:46:08 2021

@author: USER
"""

import random
print (random.randint(100,200))
m=[[100,105,110,115],[120,125,130,135],[140,145,150,155],
   [160,165,170,175],[180,185,190,195]]
for f in range(5):
    for c in range (4):
        print(m[f][c], end='')
    print()
sumaDiagonales=0
for x in range (100,200):
    sumaDiagonales=sumaDiagonales+m[f][c]
    if (x>100):
        sumaDiagonales= sumaDiagonales+m[f][2-c]
print:("La suma de sus diagonales es: "+str(sumaDiagonales))   
print(m)   