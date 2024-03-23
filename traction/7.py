# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 07:52:33 2020

@author: lucas
"""

a=2.76
b=2.66
e=9.6
f=7.39
bf=8.75
tf=0.91
tw=0.871
Ag=28
d=15.24
furo = 0.635 + 0.15 + 0.2

Ae1 = Ag - 2*furo*tw

Ae2 = Ag - 2*furo*tw + tw*(f**2)/(4*b)