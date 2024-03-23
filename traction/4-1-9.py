# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 00:20:18 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Cantoneira:
Ct = 0.75
t = 0.794 #cm

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Parafusos:
db = 1.27 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm
n_furos = 2 #na seção

#Áreas
Ag = 15.55 #cm²
Ae = Ag - defetivo*t*n_furos #cm²

#Tração resistente de cálculo
NtrdRSL = Ct*Ae*fu/gamma_a2
NtrdESB = Ag*fy/gamma_a1

Ntrd = min(NtrdRSL,NtrdESB)

#Para 2 cantoneiras:
Ntrd_total = 2*Ntrd