# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 03:35:14 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço AR-350
fy = 35 #kN/cm²
fu = 45 #kN/cm²

#Da tabela de perfis
d = 30.48 #cm
tw = 1.3 #cm
bf = 8.05 #cm
tf = 1.27 #cm
Ag = 56.9 #cm²

#Parafusado
lc = 20 #cm
ec = (4*bf*tf**2+tw*d**2-4*tw*tf**2)/(4*(2*bf*tf+d*tw-2*tf*tw))
Ct = 1 - ec/lc

#Furos
db = 2.54 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

lr = d - tf + 2*bf - tw - 2*defetivo

Ae = (d - tf)*tw + 2*(bf - 0.5*tw)*tf

NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)
