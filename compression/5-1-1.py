# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:09:27 2020

@author: lucas
"""

KLb=350 #cm
E=20000 #kN/cm²
fy=25 #kN/cm²

if(perfil=1):
    Ime=1800.13 #cm4
    Ag=38.34 #cm²
    rme=6.85 #cm
    b=20 #cm
    t=0.63 #cm
    lambdaelim=1.4*(E/fy)**0.5

if(perfil=2):
    Ime=1497.98 #cm4
    Ag=38.48 #cm²
    rme=6.24 #cm
    b=15.9 #cm
    t=0.63 #cm
    lambdaelim=1.49*(E/fy)**0.5

if(perfil=3):
    Ime=117.87 #cm4
    Ag=38.49 #cm²
    rme=1.75 #cm
    b=7 #cm
    t=7 #cm
    lambdaelim=

if(perfil=4):
    Ime=123.93 #cm4
    Ag=38.56 #cm²
    rme=1.79 #cm
    b=6.21 #cm
    t=6.21 #cm
    lambdaelim=

if(perfil=5):
    Ime=2.77 #cm4
    Ag=38.4 #cm²
    rme=0.27 #cm
    b=40 #cm
    t=4 #cm
    lambdaelim=

if(perfil=6):
    Ime=668.34 #cm4
    Ag=38.62 #cm²
    rme=4.16 #cm
    b=2.08 #cm
    t=0.95 #cm

if(perfil=7):
    Ime=249.7 #cm4
    Ag=38.81 #cm²
    rme=2.54 #cm
    b=13 #cm
    t=1.58 #cm
    lambdaelim=

KLb_rme=KLb/rme

if(KLb_rme<=200):
    print("Ok!")
else:
    print("Muito esbelto!")

lambdae=b/t
lambdaelim=
Q=
lambda0=
qui=
FE=