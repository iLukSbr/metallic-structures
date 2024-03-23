# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#Propriedades do aço do PERFIL
fu = 25 #kN/cm² AÇO TIPO ASTM A36

#Carga cortante
Ng = 200 #kN PERMANENTE
Nq = 100 #kN VARIÁVEL
gamma_g = 1.4 #PESO PRÓPRIO DE ELEMENTO CONSTRUTIVO INDUSTRIALIZADO
gamma_q = 1.5 #CARGA DE USO
Fvsd_calc = gamma_g*Ng + gamma_q*Nq
Ftsd = 0
if Fvsd_calc < 4.5:
    Fvsd_calc = 4.5 #kN

#Tipos de solicitação
cortante = 's'
tracao = 'n'
alavanca = 'n'

#Parafusos
fub = 41.5 #kN/cm² AÇO TIPO A307
gamma_a2 = 1.35
Cpc = 0.4 #COMUM
db = 2.2 #cm
Ab = np.pi*db**2/4
n_parafusos = 6
n_planoscorte = 2

#Furos
df = db + 0.15 #cm
dfe = df + 0.2 #cm
#LIMITAÇÃO PARA FORÇAS DE SERVIÇO
Cpl = 1.2
Cfp = 2.4
#Comprimentos de fissuração
lf_borda = 5.1 - dfe/2
lf_interno = 7- dfe

#Chapas, MODIFICAR DE ACORDO COM DESENHO
t2 = 0.95 #cm
t1 = 1.27 #cm
lpega = t1 + 2*t2
lc = 7 + 5.1 + 5.1 + 7 + dfe
n_chapas1 = 1
n_chapas2 = 2

#Tensão de rasgamento CONSTANTE
Cts = 1

#Área líquida sujeita à tração
Ant1 = (6.4 + 6.4 - 2*dfe)*t1*n_chapas1
Ant2 = (6.4 + 6.4 - 2*dfe)*t2*n_chapas2

#Área bruta sujeita ao cisalhamento
Agv1 = (7 + 5.1)*t1*n_chapas1
Agv2 = (7 + 5.1)*t2*n_chapas2

#Área líquida sujeita ao cisalhamento
Anv1 = Agv1 - 1.5*dfe*t1*n_chapas1
Anv2 = Agv2 - 1.5*dfe*t2*n_chapas2

#Força resistente de cisalhamento
if cortante == 's':
    print('Parafuso:')
    Fvrd1 = Cpc*Ab*fub/gamma_a2
    Fvrd_calc = n_parafusos*n_planoscorte*Fvrd1
    if lpega > 5*db:
        print('lpega=',lpega,'> 5*db=',5*db)
        Fvrd = (1-0.01*(lpega - 5*db)/0.15)*Fvrd_calc
    else:
        Fvrd = Fvrd_calc
    if lc > 127:
        Fvsd = 1.25*Fvsd_calc
    else:
        Fvsd = Fvsd_calc
    if Fvrd >= Fvsd:
        print('Fvrd=',Fvrd,'>= Fsd=',Fvsd,'resiste ao cisalhamento!')
    else:
        print('Fvrd=',Fvrd,'< Fsd=',Fvsd,'NÃO resiste ao cisalhamento!')
    print(' ')

#Força resistente de contato, CHAPA 1 interna
    print('Chapa tipo 1, interna:')
    Fcrda = (Cpl*fu/gamma_a2)*t1*(n_parafusos/2)*(lf_borda + lf_interno)
    Fcrdb = (Cfp*fu/gamma_a2)*t1*n_parafusos*db
    Fcrd1 = n_chapas1*min(Fcrda , Fcrdb)
    if Fcrd1 >= Fvsd:
        print('Fvrd=',Fcrd1,'>= Fsd=',Fvsd,'resiste ao contato!')
    else:
        print('Fvrd=',Fcrd1,'< Fsd=',Fvsd,'NÃO resiste ao contato!')
    print(' ')

#Força resistente de contato, CHAPA 2 externa
    print('Chapa tipo 2, externa:')
    Fcrdc = (Cpl*fu/gamma_a2)*t2*(n_parafusos/2)*(lf_borda + lf_interno)
    Fcrdd = (Cfp*fu/gamma_a2)*t2*n_parafusos*db
    Fcrd2 = n_chapas2*min(Fcrdc , Fcrdd)
    if Fcrd2 >= Fvsd:
        print('Fvrd=',Fcrd2,'>= Fsd=',Fvsd,'resiste ao contato!')
    else:
        print('Fvrd=',Fcrd2,'< Fsd=',Fvsd,'NÃO resiste ao contato!')
    print(' ')

#Força resistente ao rasgamento
    print('Chapa tipo 1, interna:')
    Frrd1_1 = (0.6*fu*Anv1 + Cts*fu*Ant1)/gamma_a2
    Frrd2_1 = (0.6*fu*Agv1 + Cts*fu*Ant1)/gamma_a2
    Frrd_1 = min(Frrd1_1,Frrd2_2)
    if Frrd_1 >= Fvsd:
        print('Fvrd=',Frrd_1,'>= Fsd=',Fvsd,'resiste ao contato!')
    else:
        print('Fvrd=',Frrd_1,'< Fsd=',Fvsd,'NÃO resiste ao contato!')
    print(' ')
    print('Chapa tipo 2, externa:')
    Frrd1_2 = (0.6*fu*Anv2 + Cts*fu*Ant2)/gamma_a2
    Frrd2_2 = (0.6*fu*Agv2 + Cts*fu*Ant2)/gamma_a2
    Frrd_2 = min(Frrd1_1,Frrd2_2)
    if Frrd_2 >= Fvsd:
        print('Fvrd=',Frrd_2,'>= Fsd=',Fvsd,'resiste ao contato!')
    else:
        print('Fvrd=',Frrd_2,'< Fsd=',Fvsd,'NÃO resiste ao contato!')
    print(' ')

#Tração
if tracao == 's':
    Ftrd = 0.75*Ab*fub/gamma_a2
    if Ftrd >= Ftsd:
        print('Fvrd=',Ftrd,'>= Fsd=',Ftsd,'resiste ao contato!')
    else:
        print('Fvrd=',Ftrd,'< Fsd=',Ftsd,'NÃO resiste ao contato!')
    print(' ')

#Alavanca
if alavanca == 's':
    b = 0
    a = 0
    Ae = 0
    Ag = 0
    delta = Ae/Ag
    Ftsd = Ntsd*(1 + alfa*delta*b/((1+alfa*delta)*a)