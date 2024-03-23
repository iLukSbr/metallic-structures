# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:09:55 2020

@author: lucas
"""
pi = 3.14159265359

#Aço AR350
E = 20000 #kN/cm²
G = 7700 #kN/cm²
fy = 35
fu = 45

#Perfil HEA300
d = 29
bf = 30
tw = 0.85
tf = 1.4
Ag = 112 #cm²
rx = 12.7
ry = 7.5
Ix = 18260 #cm4
Iy = 6310 #cm4
x0 = 0
y0 = 0
r = 2.7
c = r + tf

Q = 1
Lbx = 982.8
Lby = 372.5
Lbz = 372.5
K = 0.8

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