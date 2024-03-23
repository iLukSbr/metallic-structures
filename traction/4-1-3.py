# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:59:25 2020

@author: lucas
"""

fy = 25 #kN/cm²

B = 12.7 #cm

t = 1.27 #cm

db =  1.588 #cm

df = db + 0.15 #cm

dfe = df + 0.2 #cm

lcr = B - 2*dfe #cm

Ae = lcr*t

gamma_a1 = 1.2
gamma_a2 = 1.35

Ct = 1

Ag = B*t

Ntrd = Ag*fy/gamma_a1

fu = 40 #kN/cm²

Ntsd = Ct*Ae*fu/gamma_a2

N = min(Ntrd,Ntsd)