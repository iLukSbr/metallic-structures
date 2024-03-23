# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:09:52 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço AR415
fy = 41.5 #kN/cm²
fu = 52 #kN/cm²

#Perfil
a = 6.667 #cm
b = 1.905 #cm
e = 8.57 #cm
f = 7.62 #cm
d = 15.24 #cm
tw = 0.795 #cm
bf = 15.08 #cm
h = 14.04 #cm
tf = 1.2 #cm

Ag = 47.3 #cm²

#Destravado total
ltotal = 120 #cm

#Furos
db = 0.635 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

#Nt,Rd ESB
Nesb = Ag*fy/gamma_a1

#Perfil H conectado pela alma
lc = 2*f
ec=(2*tf*bf**2-4*bf*tf*tw-d*tw**2+2*tf*tw**2)/(4*(2*bf*tf+d*tw-2*tf*tw))
Ct = 1-ec/lc
if Ct>0.9:
    Ct = 0.9

#Linha de ruptura
#Perfil H calcula direto a área efetiva
Ae1 = Ag - 2*defetivo*tw
Ae2 = Ag - 2*defetivo*tw + (f**2)/(4*b)
Ae = min(Ae1,Ae2)

#Nt,Rd RSL
Nrsl = Ct*Ae*fu/gamma_a2

#Nt resultante de cálculo
Ntrd = min(Nesb,Nrsl)

#Comprimento destravado
rmin = 3.63
esbeltez = ltotal/rmin
