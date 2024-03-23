# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
print(' ')

#================================================================
#Propriedades do aço do PERFIL
fy = 25 #kN/cm² aço tipo A36
fu = 40 #kN/cm²

#================================================================
#Carga cortante
Fg = 0 #kN permanente
Fq = 0 #kN variável
gamma_g = 0 #CARGA DE 
gamma_q = 0 #CARGA DE 
Fsd_calc = gamma_g*Fg + gamma_q*Fq
if Fsd_calc < 45:
    Fsd = 45 #kN
else:
    Fsd = Fsd_calc

#================================================================
#Tipos de solicitação (s = sim ; n = não)
corrosao = 'n'
espacamento = 's'
cortante = 's'
tracao = 'n'
contato = 's'
rasgamento = 's'
alavanca = 'n'

#================================================================
#Propriedades e dimensões dos parafusos
#Resistência última
fub = 41.5 #kN/cm² parafuso tipo A307
gamma_a2 = 1.35
#Diâmetro do parafuso
db = 1.905 #cm
#Área da seção transversal do parafuso
Ab = np.pi*db**2/4 #cm²
#N° de parafusos
n_parafusos = 6

#================================================================
#Dimensões dos furos
#Diâmetro
df = db + 0.15 #cm
dfe = df + 0.2 #cm

#================================================================
#Distâncias para verificação dos espaçamentos
#Menor distância vertical ou diagonal entre eixos
dv = 6.35 #cm
#Menor distância horizontal ou diagonal entre eixos
dh = 7.62 #cm
#Menor distância entre borda do furo e borda da chapa tipo 1
dext1 = 3.81 - dfe/2 #cm
#Menor distância entre borda do furo e borda da chapa tipo 2
dext2 = 0 #cm
#Distância mínima entre borda da chapa e do furo, tabelada, para diâmetro do parafuso até abaixo daquele db
beta = 0
db_tabela = db*(1 + beta) #cm
#~~~~~~~~~~~~~~~~~~~~~~~
#Tipo de corte dos furos
#Borda cortada com serra ou tesoura = impreciso
#Borda laminada ou cortada a maçarico = preciso
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tipo_corte = 'impreciso'

#Tabela das distâncias mínimas
if tipo_corte == 'impreciso':
    if db_tabela <= 1.6:
        dmin = 2.9 #cm
    elif db_tabela <= 2:
        dmin = 3.5 #cm
    elif db_tabela <= 2.2:
        dmin = 3.8 #cm
    elif db_tabela <= 2.4:
        dmin = 4.2 #cm
    elif db_tabela <= 2.7:
        dmin = 5 #cm
    elif db_tabela <= 3:
        dmin = 5.3 #cm
    elif db_tabela <= 3.6:
        dmin = 6.4 #cm
    elif db_tabela > 3.6:
        dmin = 1.75*db_tabela #cm
elif tipo_corte == 'preciso':
    if db_tabela <= 1.6:
        dmin = 2.2 #cm
    elif db_tabela <= 2:
        dmin = 2.7 #cm
    elif db_tabela <= 2.2:
        dmin = 2.9 #cm
    elif db_tabela <= 2.4:
        dmin = 3.1 #cm
    elif db_tabela <= 2.7:
        dmin = 3.8 #cm
    elif db_tabela <= 3:
        dmin = 3.9 #cm
    elif db_tabela <= 3.6:
        dmin = 4.6 #cm
    elif db_tabela > 3.6:
        dmin = 1.25*db_tabela #cm

#================================================================
#Dimensões das chapas, MODIFICAR DE ACORDO COM DESENHO
t1 = 1.27 #cm
t2 = 0 #cm
#Comprimento do fuste dentro das chapas
lpega = t1 + t2 #cm
#Distância entre bordas mais externas do primeiro e último furos
lc = 7.62*2 + dfe #cm
#N° de chapas tipo 1
n_chapas1 = 1
#N° de chapas tipo 2
n_chapas2 = 0
#N° de planos de corte (entre chapas)
n_planoscorte = n_chapas1 + n_chapas2

#================================================================
#Parâmetro para dimensionamento ao cisalhamento dos parafusos
#~~~~~~~~~~~
#Coeficiente
#Parafusos tipo AR: ASTM A325, ISO-4016 Classe 8.8, ASTM A490 e ISO-4016 Classe 10.9
#Parafusos comuns: ASTM A307 e ISO 898-1 Classe 4.6
#Parafuso AR com corte na rosca ou parafuso comum: Cpc=0,4
#Parafuso AR com corte no fuste: Cpc=0,5
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cpc = 0.4 #COMUM

#================================================================
#Parâmetros para dimensionamento ao efeito alavanca nos parafusos
#Distância da face da chapa tracionada à borda do parafuso
b = 0
#Distância dessa mesma borda do parafuso à borda da chapa perpendicular à carga
a = 0
#Área bruta da seção
Ag = 0
#Área efetiva da seção, descontados os furos
Ae = Ag - dfe*t1

alfa = 1
if Ae != 0 and Ag !=0:
    delta = Ae/Ag
else:
    delta = 0

#================================================================
#Parâmetros para dimensionamento por contato nas chapas
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Limitações da pressão de contato
#Limitado para forças de serviço: Cpl=1,2 e Cfp=2,4
#Não limitado para forças de serviço: Cpl=1,5 e Cfp = 3
#Furos muito alongados na direção perpendicular à força: Cpl=1 e Cfp=2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cpl = 1.2 #SERVIÇO
Cfp = 2.4
#Comprimentos de fissuração
#Distância reta da borda do furo à borda da chapa
lf_borda = 3.81 - dfe/2 #cm VER DESENHO
#Distância reta da borda de um furo à borda de outro furo
lf_interno = 7.62 - dfe #cm VER DESENHO
#Fissuração total
lf = (n_parafusos - 1)*lf_interno + lf_borda

#================================================================
#Parâmetros para dimensionamento ao rasgamento das chapas:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Coeficiente de tensão de rasgamento:
#Diagrama constante: Cts=1 (em geral)
#Diagrama variável: Cts=0,5 (carga excêntrica a mais de uma linha de parafusos)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cts = 1 #CONSTANTE

#Área líquida sujeita à tração (medida transversal à carga)
Ant1 = (3.81 - dfe/2)*t1*n_chapas1 #cm² VER DESENHO
Ant2 = 0 #cm² VER DESENHO

#Área bruta sujeita ao cisalhamento (medida paralela à carga)
Agv1 = (7.62*2 + 3.81)*t1*n_chapas1 #cm² VER DESENHO
Agv2 = 0 #cm² VER DESENHO

#Área líquida sujeita ao cisalhamento (medida paralela à carga)
Anv1 = Agv1 - 2.5*dfe*t1*n_chapas1 #cm² VER DESENHO
Anv2 = 0 #cm² VER DESENHO

#================================================================
#Verificação dos espaçamentos mínimos e máximos dos furos
if espacamento == 's':
#Espaçamento entre bordas internas dos furos
    print('Espaçamento entre bordas internas dos furos')
    if lf_interno >= db:
        print('lf_interno=',lf_interno,'>= db=',db,', espaçamento entre furos atende ao mínimo.')
    else:
        print('lf_interno=',lf_interno,'< db=',db,', espaçamento entre furos NÃO atende ao mínimo.')
    print(' ')

#Espaçamento entre borda da chapa e borda externa do furo
    print('Espaçamento entre borda da chapa e borda externa do furo')
    #Chapa tipo 1:
    print('Chapa tipo 1:')
    if dext1 <= min(12*t1,15) and dext1 >= dmin:
        if 12*t1 <= 15:
            print('dmin=',dmin,'<= dexterna1=',dext1,'<= 12*t1=',12*t1,', espaçamento entre borda da chapa e borda do furo atende ao mínimo e máximo')
        else:
            print('dmin=',dmin,'<= dexterna1=',dext1,'<= 15, espaçamento entre borda da chapa e borda do furo atende ao mínimo e máximo')
    elif 15 <= 12*t1 and dext1 >= dmin:
        print('dexterna1=',dext1,'> 1,5, espaçamento entre borda da chapa e borda do furo NÃO atende ao máximo')
    elif 12*t1 < 15 and dext1 >= dmin:
        print('dexterna1=',dext1,'> 12*t1=',12*t1,', espaçamento entre borda da chapa e borda do furo NÃO atende ao máximo')
    else:
        print('dexterna1=',dext1,'< dmin=',dmin,', NÃO atende ao mínimo')
    print(' ')

    #Chapa tipo 2:
    if n_chapas2 > 0:
        print('Chapa tipo 2:')
        if dext2 <= min(12*t1,15) and dext2 >= dmin:
            if 12*t2 <= 15:
                print('dmin=',dmin,'<= dexterna2=',dext2,'<= 12*t1=',12*t2,', espaçamento entre borda da chapa e borda do furo atende ao mínimo e máximo')
            else:
                print('dmin=',dmin,'<= dexterna2=',dext2,'<= 15, espaçamento entre borda da chapa e borda do furo atende ao mínimo e máximo')
        elif 15 < 12*t2 and dext1 >= dmin:
            print('dexterna2=',dext2,'> 15, espaçamento entre borda da chapa e borda do furo NÃO atende ao máximo')
        elif 12*t1 < 15 and dext1 >= dmin:
            print('dexterna2=',dext2,'> 12*t2=',12*t2,', espaçamento entre borda da chapa e borda do furo NÃO atende ao máximo')
        else:
            print('dexterna2=',dext2,'< dmin=',dmin,', NÃO atende ao mínimo')
        print(' ')

#Parâmetros de espaçamento máximo entre eixos
    print('Parâmetros de espaçamento máximo entre eixos')
#Espessura mínima
    if t2 == 0:
        tmin = t1
        print('tmin = t1=',t1)
    else:
        tmin = min(t1,t2)
        if t1 < t2:
            print('tmin = t1=',t1)
        else:
            print('tmin = t2=',t2)
#Exposição à corrosão atmosférica
    if corrosao == 's':
        dmax = min(14*tmin,18)
        if 14*tmin < 18:
            print('dmax = 14*tmin=',14*tmin)
        else:
            print('dmax = 18')
    else:
        if 14*tmin < 1.8:
            print('dmax = 24*tmin=',24*tmin)
        else:
            print('dmax = 30')
        dmax = min(24*tmin,30)
    print(' ')

#Espaçamento vertical ou diagonal entre eixos dos furos
    print('Espaçamento vertical ou diagonal entre eixos dos furos')
    if dv >= 3*db and dv <= dmax:
        print('3*db=',3*db,'<= dvertical=',dv,'<= dmax=',dmax,', entre eixos vertical dos furos atende ao mínimo e máximo.')
    elif dv == 0:
       print('Não há parafusos seguidos na vertical.')
    elif dv < 3*db:
        print('dvertical=',dv,'< 3*db=',3*db,', entre eixos vertical dos furos NÃO atende ao mínimo.')
    elif dv > dmax:
        print('dvertical=',dv,'> dmáximo=',dmax,', entre eixos vertical dos furos NÃO atende ao máximo.')
    print(' ')

#Espaçamento horizontal ou diagonal entre eixos dos furos
    print('Espaçamento horizontal ou diagonal entre eixos dos furos')
    if dh >= 3*db and dh <= dmax:
        print('3*db=',3*db,'<= dhorizontal=',dh,'<= dmax=',dmax,', entre eixos horizontal dos furos atende ao mínimo e máximo.')
    elif dh == 0:
       print('Não há parafusos seguidos na vertical.')
    elif dh < 3*db:
        print('dhorizontal=',dh,'< 3*db=',3*db,', entre eixos vertical dos furos NÃO atende ao mínimo.')
    elif dh > dmax:
        print('dhorizontal=',dh,'> dmáximo=',dmax,', entre eixos vertical dos furos NÃO atende ao máximo.')
    print(' ')

#================================================================
#Efeito alavanca
if alavanca == 's':
    print('Força de tração solicitante de cálculo pelo efeito alavanca')
    Fsd = (Fsd_calc/n_parafusos)*(1 + alfa*delta*b/((1+alfa*delta)*a))

#================================================================
#Força resistente ao cisalhamento nos parafusos
if cortante == 's':
    print('Força resistente de cisalhamento dos parafusos:')
    Fvrd1 = Cpc*Ab*fub/gamma_a2
    Fvrd_calc = n_parafusos*n_planoscorte*Fvrd1
    if lpega > 5*db:
        print('lpega=',lpega,'> 5*db=',5*db)
        Fvrd = (1-0.01*(lpega - 5*db)/0.15)*Fvrd_calc
    else:
        Fvrd = Fvrd_calc
    if lc > 127:
        Fsd = 1.25*Fsd_calc
    if Fvrd >= Fsd:
        print('Fvrd=',Fvrd,'>= Fsd=',Fsd,'resiste ao cisalhamento!')
    else:
        print('Fvrd=',Fvrd,'< Fsd=',Fsd,'NÃO resiste ao cisalhamento!')
print(' ')

#================================================================
#Força resistente à tração nos parafusos
if tracao == 's':
    print('Força resistente à tração dos parafusos:')
    Ftrd = 0.75*Ab*fub/gamma_a2
    if Ftrd >= Fsd:
        print('Ftrd=',Ftrd,'>= Fsd=',Fsd,'resiste ao contato!')
    else:
        print('Ftrd=',Ftrd,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    print(' ')

#================================================================
#Força resistente ao contato nas chapas
if contato == 's':
    print('Força resistente ao contato das chapas:')
#Chapa tipo 1
    print('Chapa tipo 1:')
    Fcrda = (Cpl*fu/gamma_a2)*t1*(n_parafusos/2)*lf
    Fcrdb = (Cfp*fu/gamma_a2)*t1*n_parafusos*db
    Fcrd1 = n_chapas1*min(Fcrda , Fcrdb)
    if Fcrd1 >= Fsd:
        print('Fcrd=',Fcrd1,'>= Fsd=',Fsd,'resiste ao contato!')
    else:
        print('Fcrd=',Fcrd1,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    print(' ')
#Chapa tipo 2
    if n_chapas2 > 0:
        print('Chapa tipo 2:')
        Fcrdc = (Cpl*fu/gamma_a2)*t2*(n_parafusos/2)*(lf_borda + lf_interno)
        Fcrdd = (Cfp*fu/gamma_a2)*t2*n_parafusos*db
        Fcrd2 = n_chapas2*min(Fcrdc , Fcrdd)
        if Fcrd2 >= Fsd:
            print('Fcrd=',Fcrd2,'>= Fsd=',Fsd,'resiste ao contato!')
        else:
            print('Fcrd=',Fcrd2,'< Fsd=',Fsd,'NÃO resiste ao contato!')
        print(' ')

#================================================================
#Força resistente ao rasgamento nas chapas
if rasgamento == 's':
    print('Força resistente ao rasgamento das chapas:')
#Chapa tipo 1
    print('Chapa tipo 1:')
    Frrd1_1 = (0.6*fu*Anv1 + Cts*fu*Ant1)/gamma_a2
    Frrd2_1 = (0.6*fy*Agv1 + Cts*fu*Ant1)/gamma_a2
    Frrd_1 = min(Frrd1_1,Frrd2_1)
    if Frrd_1 >= Fsd:
        print('Frrd=',Frrd_1,'>= Fsd=',Fsd,'resiste ao rasgamento!')
    else:
        print('Frrd=',Frrd_1,'< Fsd=',Fsd,'NÃO resiste ao rasgamento!')
    print(' ')
#Chapa tipo 2
    if n_chapas2 > 0:
        print('Chapa tipo 2:')
        Frrd1_2 = (0.6*fu*Anv2 + Cts*fu*Ant2)/gamma_a2
        Frrd2_2 = (0.6*fy*Agv2 + Cts*fu*Ant2)/gamma_a2
        Frrd_2 = min(Frrd1_2,Frrd2_2)
        if Frrd_2 >= Fsd:
            print('Frrd=',Frrd_2,'>= Fsd=',Fsd,'resiste ao rasgamento!')
        else:
            print('Frrd=',Frrd_2,'< Fsd=',Fsd,'NÃO resiste ao rasgamento!')
        print(' ')

#================================================================
#Verificação da menor resistência
#Chapa tipo 1
Frd1 = n_chapas1*min(Fvrd,Fcrd1,Frrd_1)
print('Verificação da menor resistência na chapa tipo 1:')
print('Frd1=',Frd1)
if min(Fvrd,Fcrd1,Frrd_1) == Fvrd:
    print('Resistência limitada pelo cisalhamento dos parafusos.')
elif min(Fvrd,Fcrd1,Frrd_1) == Fcrd1:
    print('Resistência limitada pelo contato das chapas.')
elif min(Fvrd,Fcrd1,Frrd_1) == Frrd_1:
    print('Resistência limitada pelo rasgamento das chapas.')
print(' ')
#Chapa tipo 2
if n_chapas2 > 0:
    Frd2 = n_chapas2*min(Fvrd,Fcrd2,Frrd_2)
    print('Verificação da menor resistência na chapa tipo 2:')
    print('Frd2=',Frd2)
    if min(Fvrd,Fcrd2,Frrd_2) == Fvrd:
        print('Resistência limitada pelo cisalhamento dos parafusos.')
    elif min(Fvrd,Fcrd2,Frrd_2) == Fcrd2:
        print('Resistência limitada pelo contato das chapas.')
    elif min(Fvrd,Fcrd2,Frrd_2) == Frrd_2:
        print('Resistência limitada pelo rasgamento das chapas.')
    print(' ')
    print('Verificação da menor resistência geral:')
    Frd = min(Frd1,Frd2)
    print('Frd=',Frd)