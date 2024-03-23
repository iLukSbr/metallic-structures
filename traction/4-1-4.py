# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:27:45 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35
gamma_g = 1.4
Nk = 150 #kN
fy = 25 #kN/cm²
fu = 40 #kN/cm²

Ntsd = gamma_g*Nk #kN

Ntrd = Ntsd #kN

Ct = 1

Ag1 = Ntrd*gamma_a1/fy #cm²
Ag2 = Ntrd*gamma_a2/(Ct*fu*0.75)

Agcr = max(Ag1,Ag2)

pi = 3.14159265359

d = 2*(Agcr/pi)**0.5