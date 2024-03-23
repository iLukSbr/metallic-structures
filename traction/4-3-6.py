# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:56:43 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço A-36
fy = 25 #kN/cm²
fu = 40 #kN/cm²

#Furos
db = 2.222 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

f = 9 #cm

Ct = 1

#Solicitações
gk = 960 #kN
qk = 111 #kN
Ntsd = 1.25*gk + 1.5*qk

#Esforços de cálculo
Nesb = Ntsd
Nrsl = Ntsd

Ag = Nesb*gamma_a1/fy

Ae = Nrsl*gamma_a2/(Ct*fu)

tw = (Ag - Ae)/(2*defetivo)

hmin = Ae/tw + 2*defetivo