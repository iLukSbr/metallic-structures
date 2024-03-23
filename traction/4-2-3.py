# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 02:45:17 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Seção
t = 0.95 #cm
b = 15.24 #cm
lw = 25 #cm

Ag = b*t #cm²

#Sem furos
Ae = Ag #cm²

if lw >= 2*b:
    Ct = 1
if lw >= 1.5*b:
    Ct = 0.87
if lw < 1.5*b:
    Ct = 0.75

NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)