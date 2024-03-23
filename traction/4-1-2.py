# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:19:56 2020

@author: lucas
"""

gamma_q = 1.5 #tabela cap 2 pg 21

Nk = 100 #kN

fy = 25 #kN/cm²

gamma_a1 = 1.1

B = 10 #cm

Ntsd = gamma_q*Nk

Ag = Ntsd*gamma_a1/fy #cm²

t = Ag/B #cm