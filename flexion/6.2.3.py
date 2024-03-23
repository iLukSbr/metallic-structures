# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:58:02 2020

@author: lucas
"""
pesoprop = input('Peso próprio? [s/n] ')

qk = 111.21 #kN
Fqk = 1.5*qk
gk = 0.74 #kN/m
L = 6 #m
Fgk = 1.25*gk
Rm = 1

if pesoprop == 'n':
    Mmax = 250.223 #kN.m
    Mb = Mmax
    Ma = 125.111 #kN.m
    Mc = Ma

if pesoprop == 's':
    Mmax = 254.385 #kN.m
    Mb = Mmax
    Ma = 128.233 #kN.m
    Mc = Ma

#Com contenção lateral contínua
# Cb = 3 - (2/3)*(M1/M0)-(8*M2/3)/(M0+M1)

#Sem contenção lateral contínua
Cb = 12.5*Mmax*Rm/(2.5*Mmax + 3*Ma + 4*Mb + 3*Mc)
if Cb > 3:
    Cb = 3
    
print('Cb =', Cb)