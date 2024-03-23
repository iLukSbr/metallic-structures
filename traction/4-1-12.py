# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 02:22:44 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Seção
Ag = 43.87 #cm²
t = 1.27 #cm
Ct = 1

#Furos
db = 2.223 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

Ae1 = Ag - 2*defetivo*t

Ae2 = Ag + t*(-4*defetivo + (3.81**2)/(4*6.35) + (3.81**2)/(4*12.07) + (3.81**2/(4*7.62)))

Ae3 = Ag + t*(-4*defetivo + (3.81**2)/(4*6.35) + (3.81**2)/(4*12.07))

Ae4 = Ag + t*(-4*defetivo + (3.81**2)/(4*7.62))

Ae = min(Ae1,Ae2,Ae3,Ae4)

NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)