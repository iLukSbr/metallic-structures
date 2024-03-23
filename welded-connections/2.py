# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import sys
print(' ')

#=============================================================================
#Propriedades do aço A500
gamma_a1 = 1.1 #NORMAL
gamma_a2 = 1.35 #NORMAL
fy = 31.7 #kN/cm²
fu = 42.7 #kN/cm²

#=============================================================================
#Carregamento
Fg = 0 #kN
Fq = 0 #kN
gamma_g = 0 #
gamma_q = 0 #USO E OCUPAÇÃO
Fsd = gamma_g*Fg + gamma_q*Fq

#=============================================================================
#Verificações [s ou n]
perna = 'n'
comprimentoefetivo = 'n'
sobreposicao = 'n'
tracao = 's'
cisalhamento_solda = 's'
cisalhamento_metalbase = 's'
rasgamento = 's'
acharNsd = 'n'

#=============================================================================
#Propriedades da solda E70XX
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Combinações normais, especiais ou de construção: gamma_w2 = 1.35
#Combinações excepcionais: gamma_w2 = 1.15
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gamma_w2 = 1.35 #Combinação NORMAL
fw = 48.5 #kN/cm²
tiposolda = 'chapa4'
#Perna
w = 1.07 #cm
#Garganta efetiva
tw_ef = 0.5*w*np.sqrt(2)
#Comprimento do cordão
Lw = 59.92 #cm
#Ligação sobreposta
lso = 85.6 #cm

#=============================================================================
#Consideração para rasgamento
Cts = 1 #Tração UNIFORME

#=============================================================================
#Propriedades das chapas
t1 = 1.95 #cm
t2 = 2.1 #cm
b = 23.5 #cm
a = 26.2 #cm

if tiposolda == 'chapa4':
    tmin = min(t1,t2) #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    borda = (lso - lw)/2 #cm CENTRALIZADA
    n_chapas1 = 2
    n_chapas2 = 3
    n_soldas = 8
    At_MB = 0 #cm²
    Av_MB = n_chapas2*t2*lw*2 #cm²
    Av = 6*(lw + borda)*t2 #cm²
    At1 = 3*(a - b)*t2 #cm²
    At2 = 3*b*t2 #cm²
    if lw >= 2*b:
        Ct = 1
    elif lw >= 1.5*b and lw < 2*b:
        Ct = 0.87
    elif lw >= b and lw < 1.5*b:
        Ct = 0.75
    else:
        print('O comprimento efetivo lw=',lw,'não pode ser menor que b=',b)
        sys.exit(0)
    lw_min = b #cm

#=============================================================================
#Área efetiva
Aw = tw_ef*lw #cm²

#=============================================================================
if cisalhamento_solda == 's':
    Vw_Rd = n_soldas*0.6*Aw*fw/gamma_w2 #kN
    if Vw_Rd >= Fsd:
        print('Vw_Rd=',Vw_Rd,'>= Fsd=',Fsd,', a solda resiste ao cisalhamento.')
    elif Vw_Rd < Fsd:
        print('Vw_Rd=',Vw_Rd,'< Fsd=',Fsd,', o metal base não resise ao cisalhamento.')
    print(' ')

#=============================================================================
if tracao == 's' and At_MB > 0:
    Nt_MB_Rd_esc = At_MB*fy/gamma_a1 #kN
    Nt_MB_Rd_rup = Ct*At_MB*fu/gamma_a2 #kN
    Nt_MB_Rd = min(Nt_MB_Rd_esc,Nt_MB_Rd_rup) #kN
    if Nt_MB_Rd >= Fsd:
        print('Nt_MB_Rd=',Nt_MB_Rd,'>= Fsd=',Fsd,', o metal base resiste à tração.')
    elif Nt_MB_Rd < Fsd:
        print('Nt_MB_Rd=',Nt_MB_Rd,'< Fsd=',Fsd,', o metal base não resiste à tração.')
    print(' ')

#=============================================================================
if cisalhamento_metalbase == 's':
    V_MB_Rd_esc = 0.6*Av_MB*fy/gamma_a1 #kN
    V_MB_Rd_rup = 0.6*Ct*Av_MB*fu/gamma_a2 #kN
    V_MB_Rd = min(V_MB_Rd_esc,V_MB_Rd_rup) #kN
    if V_MB_Rd >= Fsd:
        print('V_MB_Rd=',V_MB_Rd,'>= Fsd=',Fsd,', o metal base resiste ao cisalhamento.')
    elif V_MB_Rd < Fsd:
        print('V_MB_Rd=',V_MB_Rd,'< Fsd=',Fsd,', o metal base não resiste ao cisalhamento.')
    print(' ')

#=============================================================================
if rasgamento == 's' and Av > 0:
    Fr_Rd1 = (0.6*fy*Av + Cts*fu*At1)/gamma_a2 #kN
    Fr_Rd2 = (0.6*fy*Av + Cts*fu*At2)/gamma_a2 #kN
    if Fr_Rd2 <= 0:
        Fr_Rd = Fr_Rd1 #kN
    elif Fr_Rd1 <= 0:
        Fr_Rd = Fr_Rd2 #kN
    else:
        Fr_Rd = min(Fr_Rd1,Fr_Rd2) #kN
    if Fr_Rd >= Fsd:
        print('Fr_Rd=',Fr_Rd,'>= Fsd=',Fsd,', resiste ao rasgamento.')
    elif Fr_Rd < Fsd:
        print('Fr_Rd=',Fr_Rd,'< Fsd=',Fsd,', não resiste ao rasgamento.')
    print(' ')