# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 02:35:01 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço A242 C
fy = 31.5 #kN/cm²
fu = 46 #kN/cm²

#Seção
B = 20.32 #cm
t = 1.27 #cm

Ag = B*t

#Furos
db = 2.22 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

NtrdESB = Ag*fy/gamma_a1

Ct = 1

lr = B - 2*defetivo
Ae = lr*t

NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)