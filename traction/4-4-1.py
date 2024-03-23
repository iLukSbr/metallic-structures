# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:24:06 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1;35

N = 133/2 #kN
mi_perfil = 75 #kg/m

#Aço CA50
fy = 50 #kN/cm²
fu = 55 #kN/cm²

Ntsd = 1.5*N + 1.25*mi_perfil*(2*3 + 2*1.5) #kN

Nesb = Ntsd
Nrsl = Ntsd

Ag1 = Nesb*gamma_a1/fy

Ct = 1

Ag2 = Nrsl*gamma_a2/(Ct*fu*0.75)

Ag = max(Ag1,Ag2)

pi = 3.14159265359

d = 2*(Ag/pi)**0.5

defetivo = 0.75*d
