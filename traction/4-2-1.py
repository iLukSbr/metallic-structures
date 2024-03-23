# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 02:25:28 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²


#Seção
B = 17.78 #cm
t = 0.95 #cm

Ag = B*t

NtrdESB = Ag*fy/gamma_a1

#Furos
db = 2.54 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

lr = B - defetivo
Ae = lr*t

Ct = 1

NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)