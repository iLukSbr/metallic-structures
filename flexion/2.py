# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pi = 3.14159265359

#Carga
l = 1079.3 #cm
carga = 1.5*0.15 #kN/cm
W = l*carga/2
Ma = -1*W*(l/4)*(-1*(l**2)+(4/3)*(l/4)**2)/(4*l)
Mb = -1*W*(l/2)*(-1*(l**2)+(4/3)*(l/2)**2)/(4*l)
# Mc = (-1/12)*W*(3*l/4)**2+(3/4)*W*l*(3*l/4)-W*(3*l/4)**2+W*((3*l/4)**3)/(3*l)
Mc = Ma
Mmax = Mb
Rm = 1

#Aço AR415
fy = 41.5 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Não contido lateralmente: com FLT

#Perfil H102x20,5
liga = 'laminado'
d = 10.16 #cm
c = 1.68 #cm
hw = d - 2*c #cm
Zx = 100.1 #cm³
tw = 0.795 #cm
tf = 0.92 #cm
bf = 10.16 #cm
ry = 2.38 #cm
Wmin = 28.8 #cm³
Iy = 146.1 #cm4
r = (d - 2*tf - hw)/2

c = r + tf

J = (2*bf*tf**3 + (d - 2*c)*tw**3)/3
Cw = (Iy*(d-tf)**2)/4

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

#FLT
Lbx = 1079.3 #cm
lambda_flt = Lbx/ry
lambdap_flt = 1.76*(E/fy)**0.5
if lambda_flt<=lambdap_flt:
    print('Compacta em FLT')
# elif lambda_flm>lambdap_flm and lambda_flm<=lambdar_flm:
    # print('Semicompacta em FLM')
# else:
    # print('Esbelta em FLM')

Mrdlim = 1.5*Wmin*fy/gamma_a1

Mpl = Zx*fy


Cb = 12.5*Mmax*Rm/(2.5*Mmax + 3*Ma + 4*Mb + 3*Mc)
if Cb > 3:
    Cb = 3

Mcr = Cb*(pi**2)*E*Iy*(((Cw/Iy)*(1+0.039*J*(Lbx**2)/Cw))**0.5)/(Lbx**2)

Mrd = Mcr/gamma_a1

print("Mrd =", round(Mrd/100,3) ,"kN.m")