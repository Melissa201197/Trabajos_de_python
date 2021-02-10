# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:51:31 2021

@author: USER
"""

def esPrimo(num):
    if num<  2:
        return False
    elif num == 2:
        return True
    else:
        for N in range(2, num):
            if num % N == 0:
                return False
        return True            

def app():
    num = int(input('Ingrese un numero: '))
    result = esPrimo(num)

    if result is True:
        print('El número es primo')
    else:
        print('El número no es primo')

if __name__ == '__main__':
    app()