# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:18:43 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço MR-250
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Perfil L152x102x9,5
b_maior = 15.2 #cm
b_menor = 10.2 #cm
t = 0.95 #cm
rmin = 2.24 #cm
ec = 2.39 #cm

Ag = 23.29 #cm²

#Nt,Rd ESB
Nesb = Ag*fy/gamma_a1

#Nt,Sd
gk = 138 #kN
qk = 203 #kN
Ntsd = 1.25*gk + 1.5*qk

#Furos
db = 1.91 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

#Coeficiente de redução da área
lc = 2*3.81
Ct = 1 - ec/lc
if Ct>0.9: Ct = 0.9

#Área efetiva
lr = b_maior + b_menor - t - 2*defetivo
Ae = lr*t

#Nt,Rd RSL
Nrsl = Ct*Ae*fu/gamma_a2

Ntrd = min(Nesb,Nrsl)