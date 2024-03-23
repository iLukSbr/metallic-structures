# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 03:16:05 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço MR250 ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²


#Furos
db = 2.54 #cm
dfuro = db +0.15 #cm
defetivo = dfuro + 0.2 #cm

#Carregamentos
gk = 222.411 #kN
qk = 444.822 #kN
vk = 200.17 #kN

Ntsd = 1.25*gk + 1.3*qk + 1.4*vk

Ntrd = Ntsd

Ag = Ntrd*gamma_a1/fy