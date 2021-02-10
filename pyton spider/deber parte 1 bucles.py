# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:55:22 2021

@author: USER
"""

num=int(input('Ingrese el número: '))
while num<=1:
    num=int(input('Error debe ingresar un número mayor de 1.'))
if num==2:
    print ('El numero ingresado (2) es el primer # primo.')
elif num>2:
    primo=False
    totalnumpri=0
    sumanumpri=0
    promnumpri=0
    for n in range (2,num):
        for m in range (2,n):
             if n%m==0:
                prim=False
                break
             else:
                 prim=True
        if n==2:
            primo=True
        if primo:
            totalnumpri+=1
            sumanumpri+=n
    for n in range (2,num):
        if num%n==0:
            num=('El numero no es un numero primo.')
            break
        else:
            num='El numero es un numero primo.'
            prim=True
    if prim:
            totalnumpri+=1
            sumanumpri+=n
    promnumpri=sumanumpri/totalnumpri
    print(num)
    print('EL total de numeros primos es:',sumanumpri)
    print('El promedio de los numeros primos es:',promnumpri)
# Para saber si el codigo ejecuta de manera correcta se han ingresado los numeros primos que debe arrojar el codigo como respuesta de numeros primos 
print ("Estos son los numeros primos en el rango de numero mayores que uno hasta el # 100: ")
print('2','3','5','7','11','13','17','19',
        '23','29','31','37','41','43','47',
        '53','59','61','67','71','73','79',
        '83','89','97')

        
            
            
            
            
            