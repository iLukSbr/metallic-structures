# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:24:22 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35
gamma_g = 1.5
fy = 25 #kN/cm²
fu = 40 #kN/cm²
t = 2.2 #cm
B = 30 #cm
N = 300 #kN
db = 2.22 #cm
Ct = 1

Ntsd = gamma_g*N

Ag = B*t
df = db + 0.15 #cm
defet = df + 0.2 #cm
lr = B-4*defet
Ae = lr*t #cm²

NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)

FS = Ntsd/Ntrd