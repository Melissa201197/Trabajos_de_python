# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:51:05 2021

@author: USER
"""

print ("INICIO")
numpri=['2','3','5','7','11','13','17','19',
        '23','29','31','37','41','43','47',
        '53','59','61','67','71','73','79',
        '83','89','97']
numnopri=['1','4']
num=int(input('Ingrese el número: '))
while num<=1:
    num=int(input('Error debe ingresar un número mayor de 1.'))
if num==2:
    print ('El numero ingresado (2) es el primer # primo.')
elif num>2:
    for n in range (2,N):
        for m in range (2,n):
               if i%r==0:
                prim=False
                break
            else:
                prim=True