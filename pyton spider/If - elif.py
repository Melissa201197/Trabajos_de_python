# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:30:39 2021

@author: USER
"""

print ("INICIO")
acl=int(input('Ingrese el # de ACL: '))
if acl >=1 and acl <=99:
    print ("Es una ACL estandar")
elif acl >=100 and acl <= 199:
    print ('Es una ACL extendida')
else:
    print ('El # ingresado no es de una ACl')
print ('FIN')