# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:57:47 2021

@author: USER
"""

str1='Cisco'
str2='Networking'
str3= "Academy"
space=''
print (str1+space+str2+space+str3,'\n'*3)
print (str1+str2+str3,'\n'*3)
print (str1,str2,str3,'\n'*3)
x=5
print("El valor de la var x es:"+str(x))
#print("El valor de la var x es:",x)
x=str(x)
print(type(x))
x=float(x)
print(type(x))
x=bool(x)
print(type(x))
x=int(x)
print(type(x))

pi=22/7
print(pi)
print("{:.2f}".format(pi))