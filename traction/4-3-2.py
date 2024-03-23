# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 06:14:06 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço A-992-P
fy = 34.5 #kN/cm²
fu = 45 #kN/cm²

#Perfil
b_maior = 8.9
b_menor = 6.4
t = 0.63
Ag = 9.29

#Carregamento
gk = 53.4
qk = 160.14
Ntsd = 1.4*gk + 1.3*qk

#Furos
defetivo = 1.91 + 0.15 + 0.2

lc = 20
ec = 1.55
Ct = 1 - ec/lc
if Ct>0.9:
    Ct = 0.9

Ae = Ag - defetivo*t

NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)