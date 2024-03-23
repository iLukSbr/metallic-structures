# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 07:16:23 2020

@author: lucas
"""

gamma_a1 = 1.1
gamma_a2 = 1.35

#Aço A-992-P
fy = 34.5 #kN/cm²
fu = 45 #kN/cm²


#Perfil
d = 41
bf = 17.9
tw = 0.88
tf = 1.44
hw = 35.7
Ag = 86.3

lc = 3*7.62
ec=(2*tf*bf**2-4*tf*bf*tw-d*tw**2+2*tf*tw**2)/(4*(2*bf*tf+d*tw-2*tf*tw))
Ct = 1 - ec/lc

Ae = Ag - 4*2.222*tf

NtrdESB = Ag*fy/gamma_a1
NtrdRSL = Ct*Ae*fu/gamma_a2

Ntrd = min(NtrdESB,NtrdRSL)