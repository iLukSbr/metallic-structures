# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço A992
fy = 34.5 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Contidos lateralmente: sem FLT

#Perfil W360x39
liga = 'laminado'
d = 35.3 #cm
hw = 33.2 #cm
Zx = 667.7 #cm³
tw = 0.65 #cm
tf = 1.07 #cm
bf = 12.8 #cm

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

L = 9.2 #m
P = Mrd*4/(100*1.5*L)

print("P <=", P ,"kN")