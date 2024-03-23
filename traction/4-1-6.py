# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:17:36 2020

@author: lucas
"""

B = 40.64 #cm
t = 1.905 #cm
db = 2.54 #cm
dfuro = db + 0.15 #cm
defetivo = dfuro + 0.2 #cm

lcr1 = B - 2*defetivo

lcr2 = B - 3*defetivo + 2*(7.62**2)/(4*12.7)

lcr = min(lcr1,lcr2)

Ae = lcr*t