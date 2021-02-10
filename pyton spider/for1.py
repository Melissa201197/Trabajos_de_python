# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:37:03 2021

@author: USER
"""

result=0
n=50
for i in range(0,n+1,10):
    print(i)
    result+=i
    #this^^ is the shortand for
    #result=result+i
print("El resutado acumlado es: ",result)