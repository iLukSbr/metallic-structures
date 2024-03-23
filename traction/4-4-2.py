# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:03:51 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

t = 0.95 #cm

#Aço MR-250
fy = 25 #kN/cm²
fu = 40 #kN/cm²

Ntsd = (((1.5*650 + 1.25*240 + 1.5*350 - 1.35*200)/1000)**2 + (1.4*1)**2)**0.5 #kN

Ag = Ntsd*gamma_a1/fy #cm²

B = Ag/t #cm