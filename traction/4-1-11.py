# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:04:43 2020

@author: lucas
"""

t = 1.27 #cm

#Furos:
db = 2.22 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

lr1 = 3.8 +  7.6 + 11.53 + 3.8 - 2*defetivo
lr2 = 3.8 +  7.6 + 11.53 + 3.8 - (7.6**2)/(4*11.53) - (7.6**2)/(4*7.6)

lr = min(lr1,lr2)

Ae = lr*t #cm²

#-------------------------------------------------------------

r_min = 2.21 #cm
l = 300*r_min #cm