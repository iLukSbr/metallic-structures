# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import sys
print(' ')

#=============================================================================
#Propriedades do aço AR415
gamma_a1 = 1.1 #NORMAL
gamma_a2 = 1.35 #NORMAL
fy = 41.5 #kN/cm²
fu = 52 #kN/cm²

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
comprimentoefetivo = 's'
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
tiposolda = 'perfil4'
#Perna
w = 0.82 #cm
#Garganta efetiva
tw_ef = 0.5*w*np.sqrt(2)
#Comprimento do cordão
Lw = 4.944 #cm
#Ligação sobreposta
borda = w #cm MÍNIMA
lso = 0 #cm

#=============================================================================
#Consideração para rasgamento
Cts = 1 #Tração UNIFORME

#=============================================================================
#Propriedades das chapas
t1 = 2 #cm
t2 = 0 #cm
b = 0 #cm
a = 0 #cm
c = 0 #cm

#Propriedades  do perfil 
bf = 6.18 #cm
tf = 0.99 #cm
tw = 1 #cm
d = 20.32 #cm
Ag = 30.8 #cm

#Perfil L
tl = 0 #cm

if tiposolda == 'chapa1':
    tmin = min(t1,t2) #cm
    tborda = t1
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    n_chapas1 = 1
    n_chapas2 = 1
    n_soldas = 1
    At_MB = 0 #cm²
    Av_MB = n_chapas2*t2*lw*2 #cm²
    Av = 2*(lw + borda)*t2 #cm²
    At1 = (a - c)*t2 #cm²
    At2 = c*t2 #cm²
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
elif tiposolda == 'chapa2':
    tmin = min(t1,t2) #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    n_chapas1 = 2
    n_chapas2 = 1
    n_soldas = 2
    At_MB = 0 #cm²
    Av_MB = n_chapas2*t2*lw*2 #cm²
    Av = 2*(lw + borda)*t2 #cm²
    At1 = (a - c)*t2 #cm²
    At2 = c*t2 #cm²
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
elif tiposolda == 'chapa3':
    tmin = min(t1,t2) #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    n_chapas1 = 1
    n_chapas2 = 2
    n_soldas = 2
    At_MB = 0 #cm²
    Av_MB = n_chapas2*t2*lw*2 #cm²
    Av = 4*(lw + borda)*t2 #cm²
    At1 = 2*(a - c)*t2 #cm²
    At2 = 2*c*t2 #cm²
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
elif tiposolda == 'chapa4':
    tmin = min(t1,t2) #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    n_chapas1 = 2
    n_chapas2 = 3
    n_soldas = 4
    At_MB = 0 #cm²
    Av_MB = n_chapas2*t2*lw*2 #cm²
    Av = 6*(lw + borda)*t2 #cm²
    At1 = 3*(a - c)*t2 #cm²
    At2 = 3*c*t2 #cm²
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
elif tiposolda == 'chapa5':
    tmin = min(t1,t2) #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    n_chapas1 = 2
    n_chapas2 = 2
    n_soldas = 3
    At_MB = 0 #cm²
    Av_MB = n_chapas2*t2*lw*2 #cm²
    Av = 4*(lw +  borda)*t2 #cm²
    At1 = 2*(a - c)*t2 #cm²
    At2 = 2*c*t2 #cm²
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
elif tiposolda == 'perfil1':
    tmin = tf #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
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
    Av = 4*tf*(lw + borda) #cm²
    At1 = 0 #cm²
    At2 = 2*(bf - b)*tf #cm²
    lw_min = b #cm
elif tiposolda == 'perfil2':
    tmin = tw #cm
    tborda = t1 #cm
    beta = 1.2 - 0.002*(Lw/w)
    if beta > 1:
        beta = 1
    elif beta < 0.6:
        print('Modificar a solda, beta=',beta,'< 0,6')
        sys.exit(0)
    lw = Lw*beta #cm
    n_soldas = 4
    At_MB = 0 #cm²
    Av_MB = tw*lw*2 #cm²
    ec = (2*(bf**2)*tf - 4*bf*tf*tw -d*tw**2 + 2*tf*tw**2)/(4*(2*bf*tf + d*tw - 2*tf*tw)) #cm
    lc = lw #cm
    Ct = 1 - ec/lc
    if Ct > 0.9:
        Ct = 0.9
    elif Ct < 0.6:
        print('Não se permite Ct=',Ct,'< 0,6, deve-se alterar a ligação.')
        sys.exit(0)
    Av = 2*tw*(lw + borda) #cm²
    At1 = b*tw #cm²
    At2 = 0 #cm²
    lw_min = b #cm
elif tiposolda == 'perfil3':
    tmin = min(tw,t1) #cm
    tborda = 0 #cm
    lw = Lw #cm
    n_soldas = 2
    At_MB = tw*lw #cm²
    Av_MB = t1*lw*2 #cm²
    Ac = lw*tw #cm²
    Ct = Ac/Ag
    Av = 0 #cm²
    At1 = 0 #cm²
    At2 = 0 #cm²
    lw_min = max(4*w,4) #cm
elif tiposolda == 'perfil4':
    tmin = min(tf,t1) #cm
    tborda = 0 #cm
    lw = Lw #cm
    n_soldas = 2
    At_MB = 0 #cm²
    Av_MB = t1*lw*2 #cm²
    Ac = 2*lw*tf #cm²
    Ct = Ac/Ag
    Av = 0 #cm²
    At1 = 0 #cm²
    At2 = 0 #cm²
    lw_min = max(4*w,4) #cm
elif tiposolda == 'perfil5':
    tmin = min(tl,t1) #cm
    tborda = 0 #cm
    lw = Lw #cm
    n_soldas = 4
    At_MB = tl*lw*2 #cm²
    Av_MB = t1*lw*4 #cm²
    Ac = 2*lw*tl #cm²
    Ct = Ac/Ag
    Av = 0 #cm²
    At1 = 0 #cm²
    At2 = 0 #cm²
    lw_min = max(4*w,4) #cm

#=============================================================================
#Área efetiva
Aw = tw_ef*lw #cm²

#=============================================================================
if perna == 's':
#Limitação mínima pela espessura do metal base na junta
    if tmin <= 0.635:
        wmin = 0.3 #cm
    elif tmin > 0.635 and tmin <= 1.25:
        wmin = 0.5 #cm
    elif tmin > 1.25 and tmin <= 1.9:
        wmin = 0.6 #cm
    elif tmin > 1.9:
        wmin = 0.8 #cm
#Limitação máxima pela espessura das bordas soldadas
    if tborda < 0.635 and tborda > 0:
        wmax = tborda - 0.001 #cm
    elif tborda >= 0.635 and tborda < 1.9:
        wmax = tborda #cm
    elif tborda >= 1.9:
        wmax = tborda - 0.15 #cm
#Verificando a perna
    if w >= wmin and w <= wmax and tborda > 0:
        print('A perna w=',w,'respeita os limites mínimo wmin=',wmin,'e máximo wmax=',wmax)
    elif w >= wmin and w <= wmax and tborda == 0:
        print('A perna w=',w,'respeita o limite mínimo wmin=',wmin)
    elif w < wmin:
        print('A perna w=',w,'não respeita o limite mínimo wmin=',wmin)
    elif w > wmax and tborda > 0:
        print('A perna w=',w,'não respeita o limita máximo wmax=',wmax)
    print(' ')

#=============================================================================
if comprimentoefetivo == 's':
    if lw >= lw_min:
        print('O comprimento efetivo lw=',lw,'respeita o limite mínimo lw_min=',lw_min)
    elif lw < lw_min:
        print('O comprimento efetivo lw=',lw,'não respeita o limite mínimo lw_min=',lw_min)
    print(' ')

#=============================================================================
if sobreposicao == 's':
    lso_min = max(8*tmin,2.5)
    bordamin = w #cm
    if lso >= lso_min:
        print('O comprimento de sobreposição =',lso,'respeita o limite mínimo lso_min=',lso_min)
    elif lso < lso_min:
        print('O comprimento de sobreposição lso=',lso,'não respeita o limite mínimo lso_min=',lso_min)
    if borda >= bordamin:
        print('O espaço na borda =',borda,'respeita o limite mínimo =',bordamin)
    elif borda < bordamin:
        print('O espaço na borda =',borda,'não respeita o limite mínimo =',bordamin)
    print(' ')

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
if acharNsd == 's':
    Nsd_calc = Frd #kN
    gamma = max(gamma_g,gamma_q)
    Nk = Nsd_calc/gamma #kN
    print('Nk_máx=',Nk)
    print(' ')