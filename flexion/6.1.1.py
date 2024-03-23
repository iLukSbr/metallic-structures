# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
perfil = input("Perfil w ou vs? ")

#Aço MR250
fy = 25 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Contidos lateralmente: sem FLT

#Perfil W530x85
if perfil=='w':
    h = 53.5 #cm
    hw = 47.8 #cm
    Zx = 2100 #cm³
    tw = 1.03 #cm
    tf = 1.65 #cm
    bf = 16.6 #cm
    

#Perfil VS500x86
if perfil=='vs':
    h = 50 #cm
    hw = 46.8 #cm
    Zx = 2281 #cm³
    tw = 0.63 #cm
    tf = 1.6 #cm
    bf = 25 #cm

#FLA
lambda_fla = hw/tw
lambdap_fla = 3.76*(E/fy)**0.5
if lambda_fla<=lambdap_fla:
    print('Compacta em FLA')

#FLM
lambda_flm = (bf/2)/tf
lambdap_flm = 0.38*(E/fy)**0.5
if lambda_flm<=lambdap_flm:
    print('Compacta em FLM')

Mpl = Zx*fy
Mrd = Mpl/gamma_a1

print("Mrd =", round(Mrd/100,3) ,"kN.m")