# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 02:02:40 2020

@author: lucas
"""

Ag = 24.65 #cm²
t = 1.11 #cm

#Furos
db = 1.588 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

#Área efetiva
Ae1 = Ag - defetivo*t

Ae2 = Ag + t*(-2*defetivo + (5.08**2)/(4*7.62))

Ae = min(Ae1,Ae2)