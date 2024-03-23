# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:38:20 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Dimensões da chapa:
B = 28 #cm
t = 2 #cm

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Todos os elementos conectados
Ct = 1

#Parafusos:
db = 2 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

#Áreas
Ag = B*t

Si = 7.5 #cm
gi = 5 #cm

lr1 = B - 2*defetivo
lr2 = B - 4*defetivo + 2*(Si**2)/(4*gi)
lr3 = B - 5*defetivo + 4*(Si**2)/(4*gi)

lr = min(lr1,lr2,lr3)

Ae = lr*t

#Tração resistente de cálculo
NtrdRSL = Ct*Ae*fu/gamma_a2
NtrdESB = Ag*fy/gamma_a1

Ntrd = min(NtrdRSL,NtrdESB)