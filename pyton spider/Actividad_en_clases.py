# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:23:03 2021

@author: USER
"""

leer1= input('Ingrese su nombre: ')
leer2= input ('Ingrese su apellido: ') 
leer3= input('Ingrese su localizacion: ')
leer4= input ('Ingrese su edad: ')
print ('Inicio')
leer4=int(input('Ingrese su edad: '))
if leer4  >=0 and leer4 <=1:
    print('Es un bebe')
elif leer4  >=2 and leer4 <= 11:
    print('Es un niño')
else:
    print('El numero ingresado no es de un bebe o de un niño')
if leer4  >=12 and leer4 <=17:
    print('Es joven')
elif leer4  >=18 and leer4 <= 59:
    print('Es Adulto')
else:
    print('El numero ingresado no es de un joven o de un adulto')
