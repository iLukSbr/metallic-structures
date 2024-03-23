# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 02:49:40 2020

@author: lucas
"""

#a)
#Chapa plana com solda longitudinal
ba = 1.59
lwa = 12.7
b2a = ba*2
b15a = ba*1.5
if lwa >= b2a:
    Cta = 1
if lwa >= b15a:
    Cta = 0.87
if lwa < b15a:
    Cta = 0.75
Aea = ba*10.2
Produtoa = Cta*Aea

#b)
#Chapa plana com solda longitudinal
bb = 10.16
lwb = 12.7
b2b = bb*2
b15b = bb*1.5
if lwb >= b2b:
    Ctb = 1
if lwb >= b15b:
    Ctb = 0.87
if lwb < b15b:
    Ctb = 0.75
Aeb = bb*0.95
Produtob = Ctb*Aeb

#c)
#Solda longitudinal + transversal
Ctc = 1
Aec = 12.7*1.59
Produtoc = Ctc*Aec

#d)
#Parafusos
Ctd = 1
lrd = 13.97 - (1.91 + 0.15 + 0.2)
Aed = lrd*1.27
Produtod = Ctd*Aed

#e)
#Parafusos
Cte = 1
lre = 15.24 - (2.22 + 0.15 + 0.2)
Aee = lre*1.59
Produtoe = Cte*Aee