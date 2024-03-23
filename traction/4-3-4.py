# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:50:34 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço A-500
fy = 31.7 #kN/cm²
fu = 42.7 #kN/cm²

#Perfil C254x22,7
d = 25.4 #cm
tw = 0.61 #cm
bf = 6.6 #cm
h = 23.18 #cm
tf = 1.11 #cm

Ag = 29 #cm²

#Nt,Rd ESB
Nesb = Ag*fy/gamma_a1

#Coeficiente de redução
lc = 7.62 + 6.35 #cm
ec = 1.61 #cm
Ct = 1 - ec/lc
if Ct>0.9:
    Ct = 0.9
    
#Furos
db = 1.91 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

#Área efetiva
Ae1 = Ag - 2*defetivo*tw
Ae2 = Ag + (-3*defetivo + 2*(6.35**2)/(4*6.35))*tw
Ae = min(Ae1,Ae2)

#Nt,Rd RSL
Nrsl = Ct*Ae*fu/gamma_a2

Ntrd = min(Nesb,Nrsl)