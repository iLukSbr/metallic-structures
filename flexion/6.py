# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:14:38 2020

@author: lucas
"""

#Sem contenção lateral contínua
P = 71.46 #kN
a = 4.837 #m
b = 6.68 #m
l = 11.517 #m

Ma = P*b*(l/4)/l
Mb = P*a-P*a*(l/2)/l
Mc = P*a-P*a*(3*l/4)/l
Rm = 1
Mmax = P*b*a/l

Cb = 12.5*Mmax*Rm/(2.5*Mmax + 3*Ma + 4*Mb + 3*Mc)
if Cb > 3:
    Cb = 3
    
print('Cb =', Cb)