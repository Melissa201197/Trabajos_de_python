# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:48:30 2021

@author: USER
"""

lista2=[]
lista=['R1','R2','R3',
       'R4','S1','S2',
       'S3','S4']
for a in lista:
    if "S" in a:
        lista2.append(a)
print(lista2)
for a in lista:
    if "R" in a:
        lista2.append(a)
print(lista2)
lista3=[]
lista=['R1','R2','R3',
       'R4','S1','S2',
       'S3','S4']
for a in lista:
    if "R" in a:
        lista3.append(a)
print(lista3)
#1 punto extra