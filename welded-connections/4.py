# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import sys
print(' ')

#=============================================================================
#Propriedades do aço AR350
gamma_a1 = 1.1 #NORMAL
gamma_a2 = 1.35 #NORMAL
fy = 35 #kN/cm²
fu = 45 #kN/cm²

#=============================================================================
#Carregamento
Fg = 0 #kN
Fq = 2197 #kN
gamma_g = 0 #
gamma_q = 1.5 #USO E OCUPAÇÃO
Fsd = gamma_g*Fg + gamma_q*Fq

#=============================================================================
#Verificações [s ou n]
cisalhamento_solda = 's'
cisalhamento_metalbase = 's'
rasgamento = 's'

#=============================================================================
#Propriedades da solda E60XX
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Combinações normais, especiais ou de construção: gamma_w2 = 1.35
#Combinações excepcionais: gamma_w2 = 1.15
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gamma_w2 = 1.35 #Combinação NORMAL
fw = 41.5 #kN/cm²
tiposolda = 'chapa1'
#Perna
w = 1.47 #cm
#Garganta efetiva
tw_ef = 0.5*w*np.sqrt(2)

#=============================================================================
#Consideração para rasgamento
Cts = 1 #Tração UNIFORME

#=============================================================================
#Propriedades das chapas
t1 = 2.37 #cm
t2 = 1.68 #cm
b = 16.3 #cm
a = 32.5 #cm
c = 0 #cm

if tiposolda == 'chapa1':
    tmin = min(t1,t2) #cm
    tborda = t1
    n_chapas1 = 1
    n_chapas2 = 1
    n_soldas = 2
    # if lw >= 2*b:
    Ct = 1
    # elif lw >= 1.5*b and lw < 2*b:
    #     Ct = 0.87
    # elif lw >= b and lw < 1.5*b:
    #     Ct = 0.75

#=============================================================================
if cisalhamento_solda == 's':
    lw_solda = Fsd*gamma_w2/(n_soldas*0.6*tw_ef*fw)

#=============================================================================
if cisalhamento_metalbase == 's':
    lw_esc = Fsd*gamma_a1/(0.6*n_chapas2*t2*2*fy)
    lw_rup = Fsd*gamma_a2/(0.6*Ct*n_chapas2*t2*2*fu)

lw = max(lw_solda,lw_esc,lw_rup)

Lw = 0
while True:
    Lw = Lw + 0.001
    buff = 0.002*(Lw**2)/w - 1.2*Lw + lw
    if not ((buff >= 0.01 and buff <= 10000) or (buff <= -0.01 and buff >= -10000)):
        break
beta = 1.2-0.002*Lw/w