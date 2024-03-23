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
#Propriedades da solda 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Combinações normais, especiais ou de construção: gamma_w2 = 1.35
#Combinações excepcionais: gamma_w2 = 1.15
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gamma_w2 = 1.35 #Combinação NORMAL
fw = 41.5 #kN/cm²
tiposolda = 'perfil1'
#Perna
w = 0.67 #cm
#Garganta efetiva
tw_ef = 0.5*w*np.sqrt(2)
#Comprimento do cordão
Lw = 22.4 #cm
#Ligação sobreposta
lso = 28 #cm

#=============================================================================
#Consideração para rasgamento
Cts = 1 #Tração UNIFORME

#=============================================================================
#Propriedades das chapas
t1 = 0.67 #cm
t2 = 0 #cm
b = 14.48 #cm
a = 0 #cm
c = 0 #cm

#Propriedades  do perfil I 508 x 134
bf = 18.1 #cm
tf = 2.33 #cm
tw = 1.84 #cm
d = 50.8 #cm
Ag = 170.7 #cm

#Perfil L
tl = 0 #cm

if tiposolda == 'perfil1':
    tmin = tf #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    borda = (lso - lw)/2 #cm CENTRALIZADA
    n_soldas = 4
    At_MB = 0 #cm²
    Av_MB = tf*lw*4 #cm²
    ec = (4*bf*tf**2 + (d**2)*tw - 4*(tf**2)*tw)/(4*(2*bf*tf + d*tw - 2*tf*tw)) #cm
    lc = lw #cm
    Ct = 1 - ec/lc
    if Ct > 0.9:
        Ct = 0.9
    elif Ct < 0.6:
        print('Não se permite Ct=',Ct,'< 0,6, deve-se alterar a ligação.')
        sys.exit(0)
    Av = tf*(lw + borda) #cm²
    At1 = 0 #cm²
    At2 = (bf - b)*tf #cm²
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
    Fr_Rd1 = (0.6*fy*Av*4 + Cts*fu*At1*2)/gamma_a2 #kN
    Fr_Rd2 = (0.6*fy*Av*4 + Cts*fu*At2*2)/gamma_a2 #kN
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

#=============================================================================
if At_MB > 0 and Av > 0:
    Frd = min(Vw_Rd,Nt_MB_Rd,V_MB_Rd,Fr_Rd) #kN
elif At_MB > 0 and Av <= 0:
    Frd = min(Vw_Rd,Nt_MB_Rd,V_MB_Rd) #kN
elif At_MB <= 0 and Av > 0:
    Frd = min(Vw_Rd,V_MB_Rd,Fr_Rd) #kN
else:
    Frd = min(Vw_Rd,V_MB_Rd) #kN
print('Frd=',Frd)
print(' ')