# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:47:12 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Seção
Ag = 64.2 #cm²
t = 1 #cm

l = 7.5 #cm
ec = 2 #cm
Ct = 1 - ec/l

#Furos
db = 2.2 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

Ae = Ag - 4*defetivo*t

#Esforços de tração resistentes de cálculo
NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)