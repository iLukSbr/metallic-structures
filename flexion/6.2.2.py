# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço MR250
fy = 25 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Contidos lateralmente: sem FLT

#Perfil VS650x98
liga = 'soldado'
d = 65 #cm
hw = 62.5 #cm
Zx = 3172 #cm³
tw = 0.8 #cm
tf = 1.25 #cm
bf = 30 #cm

#FLA
lambda_fla = hw/tw
lambdap_fla = 3.76*(E/fy)**0.5
lambdar_fla = 5.7*(E/fy)**0.5
if lambda_fla<=lambdap_fla:
    print('Compacta em FLA')
elif lambda_fla>lambdap_fla and lambda_fla<=lambdar_fla:
    print('Semicompacta em FLA')
else:
    print('Esbelta em FLA')

#FLM
lambda_flm = (bf/2)/tf
lambdap_flm = 0.38*(E/fy)**0.5
if liga == 'laminado':
    Cls = 0.83
if liga == 'soldado':
    kc = 4/((hw/tw)**0.5)
    if kc<0.35 or kc>0.76:
        print('Problema no kc, modificar perfil')
    Cls = 0.95*kc**0.5
lambdar_flm = Cls*(E/(0.7*fy))**0.5
if lambda_flm<=lambdap_flm:
    print('Compacta em FLM')
elif lambda_flm>lambdap_flm and lambda_flm<=lambdar_flm:
    print('Semicompacta em FLM')
else:
    print('Esbelta em FLM')

Mpl = Zx*fy
Mrd = Mpl/gamma_a1

print("Mrd =", round(Mrd/100,3) ,"kN.m")