# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:59:34 2020

@author: lucas
"""

fy = 25 #kN/cm²

gamma_a1 = 1.1

Ntrd = 100 #kN

B = 10 #cm

Ag = gamma_a1*Ntrd/fy #cm²

t = Ag/B #cm

t_mm = t*10 #mm