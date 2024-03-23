# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:26:11 2020

@author: lucas
"""

pi = 3.14159265359
gamma_a1 = 1.1

#Aço MR250
E = 20000 #kN/cm²
G = 7700 #kN/cm²
fy = 25

#Perfil HEA180
d = 17.1
bf = 18
tw = 0.6
tf = 0.95
r = 1.5
hw = d - 2*r - 2*tf
Ag = 45.3
Ix = 2510
rx = 7.5
Iy = 925
ry = 4.5
x0 = 0
y0 = 0
c = r + tf

#Índice de esbeltez <= 200?
Lb = 244.9
rmin = min(rx,ry)
K = 2

IE = K*Lb/rmin

if(IE <= 200):
    print('Esbeltez ok')
else:
    print('Esbeltez não')
   
#Flambagem local Q=1?
#Alma grupo 2
lambdae_alma = hw/tw
lambdaelim_alma = 1.49*(E/fy)**0.5

if(lambdae_alma < lambdaelim_alma):
    print('Flambagem local alma ok Qa=1')
    Qa=1
else:
    print('Flambagem local alma não')
   
#Mesa grupo 4
lambdae_mesa = bf/(2*tf)
lambdaelim_mesa = 0.56*(E/fy)**0.5

if(lambdae_mesa < lambdaelim_mesa):
    print('Flambagem local mesa ok Qs=1')
    Qs=1
else:
    print('Flambagem local mesa não')

Q = Qa*Qs

#Flambagem global qui
Lbx = Lb
Lby = Lb
Lbz = Lb

Nex = (pi**2)*E*Ix/(K*Lby)**2
Ney = (pi**2)*E*Iy/(K*Lbx)**2

r02 = rx**2 + ry**2 + x0**2 + y0**2
J = (2*bf*tf**3 + (d - 2*c)*tw**3)/3
Cw = (Iy*(d-tf)**2)/4

Nez = ((pi**2)*E*Cw/(K*Lbz)**2 + G*J)/r02

N = min(Nex,Ney,Nez)

lambda0 = (Q*Ag*fy/N)**0.5

if(lambda0 <= 1.5):
    qui = 0.658**(lambda0**2)
if(lambda0 > 1.5):
    qui = 0.877/(lambda0**2)

#Resistente de cálculo
Ncrd = qui*Q*Ag*fy/gamma_a1