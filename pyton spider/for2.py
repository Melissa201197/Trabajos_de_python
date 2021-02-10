# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:20:25 2021

@author: USER
"""

lista=['R1','R2','R3'
      ,'S1',"S2",'S3',
      '6','5','AP']
for a in lista:
    if "R" in a:
        print("Los routers son: ",a)
    elif "S" in a:
        print("Los switch son:",a)
    else:
        print("No son equipos de red:",a)
        
    