# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:58:18 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Carga
gamma_g = 1.5
gamma_q = 1.5

Fgk = 115.69 #kN
Fqk = 66.72 #kN

Ntsd = gamma_g*Fgk + gamma_q*Fqk

#Seção
t = 0.953 #cm
B = 22.58 #cm

Ct = 0.85

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Parafusos:
db = 2.222 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm
n_furos = 1 #na seção

#Áreas
Ag = 16.13 #cm²
Ae = Ag - defetivo*t*n_furos #cm²

#Tração resistente de cálculo
NtrdRSL = Ct*Ae*fu/gamma_a2
NtrdESB = Ag*fy/gamma_a1

Ntrd = min(NtrdRSL,NtrdESB)