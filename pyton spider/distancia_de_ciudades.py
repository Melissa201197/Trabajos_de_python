# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:48:10 2021

@author: USER
"""


dt=float(334)
t= float(input('Ingrese el tiempo en horas: '))
v= float(input ('Ingrese la velocidad en km/h: '))
mul=v*t
print('La distancia recorrida al momento es: ',v,"*",t,"es:",mul,'\n')
resta=dt-mul
print('La distancia faltante a recorrer es: ',dt,"-",mul,"es:",resta,'\n')
div=resta/v
print('Usted llegara a su destino en: ',resta,"/",v,"es:",div,'\n')
