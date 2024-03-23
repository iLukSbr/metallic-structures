# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import sys

#Coeficientes de ponderação
gamma_a1 = 1.1
a = 0

#Propriedades do aço
E = 20000 #kN/cm²
fy = 25 #kN/cm²

#Propriedades do perfil
d = 45
tw = 0.76
tf = 1.08
print('1 = Perfil I laminado')
print('2 = Perfil C laminado fletido na maior inércia X')
print('3 = Perfil caixão soldado')
print('4 = Perfil retangular laminado')
print('5 = Perfil T laminado')
print('6 = Perfil I soldado fletido na menor inércia Y')
print('7 = Perfil C laminado fletido na menor inércia Y')
print('8 = Perfil composto por cantoneiras')
print('9 = Perfil I soldado fletido na maior inércia X')
perfil = '1'
print('perfil = ',perfil)

if perfil=='1' or perfil=='2':
    Aw = d*tw
    hw = 40.4
    lamb = hw/tw
elif perfil=='3':
    hw = d - 2*tf
    Aw = 2*hw*tw
    lamb = hw/tw
elif perfil=='4':
    curva = float(input('Qual a curvinha? '))
    hw = d - 2*tf - 2*curva
    Aw = 2*hw*tw
    lamb = hw/tw
elif perfil=='5':
    Aw = d*tw
    curva = float(input('Qual a curvinha? '))
    hw = d - tf - curva
    lamb = hw/tw
    if lamb<=260:
        print(lamb,' <= 260, ok!')
    else:
        sys.exit(lamb,' > 260, não confere')
elif perfil=='6':
    bf = float(input('bf = ? '))
    Aw = 2*bf*tf
    lamb = bf/(2*tf)
elif perfil=='7':
    bf = float(input('bf = ? '))
    Aw = 2*bf*tf  
    lamb = bf/tf
elif perfil=='8':
    Aw = 2*d*tw
    lamb = d/tw
    if lamb<=260:
        print(lamb,' <= 260, ok!')
    else:
        sys.exit(lamb,' > 260, não confere')
if perfil=='9':
    hw = d - 2*tf
    Aw = d*tw
    lamb = hw/tw
    
print('Aw = ',Aw)

#Cortante solicitante
V_Sd = 0
tem_carga_solic = 's'
if tem_carga_solic == 's':
    V_Sd = 1.3*331/2

#Resistência do perfil ao cisalhamento
tauy = 0.6*fy
Vpl = 0.6*Aw*fy
print('Vpl = ',Vpl)

enrij = 'n'
if enrij=='n' or perfil=='3' or perfil=='4':
   kv = 5
if perfil=='5' or perfil=='6' or perfil=='7' or perfil=='8':
    kv = 1.2
elif enrij=='s':
    tem_dist_enrij = input('Tenho a distância entre os enrijecedores? [s/n] ')
    if(tem_dist_enrij=='n'):
        secao = input('Qual o tipo de seção que quero? [compacta/semicompacta/esbelta] ')
        if secao=='compacta':
            kv = (lamb**2)*fy/(1.21*E)
            # a = np.sqrt(E*(tw**2)*6.05/(fy*(hw**2)-E*(tw**2)*6.05))
        elif secao=='semicompacta':
            kv = (fy/(1.21*E))*(V_Sd*lamb*gamma_a1/Vpl)**2
            # a = np.sqrt(E*(tw**2)*9.3845/(fy*(hw**2)-E*(tw**2)*9.3845))
        # if kv<=5:
        #     sys.exit('Erro de kv<=5 antes de calcular a')
        a = np.sqrt((5*hw**2)/(kv-5))
    elif(tem_dist_enrij=='s'):
        a = float(input('Qual a distância longitudinal entre 2 enrijecedores conseucutivos? [cm] '))
    if a/hw > (260*tw/hw)**2 :
        kv = 5
        print ('a/hw=',a/hw,' > (260*tw/hw)**2=',(260*tw/hw)**2,' valor de a não verifica')
    else:
        print ('a/hw=',a/hw,' <= (260*tw/hw)**2=',(260*tw/hw)**2,' valor de a verificado')
        kv = 5 + 5*(hw**2)/a**2
print('kv = ',kv)
print('a = ',a)

lamb_p = 1.1*np.sqrt(kv*E/fy)
lamb_r = 1.37*np.sqrt(kv*E/fy)

if lamb<=lamb_p:
    print('Seção compacta ',lamb,' <= ',lamb_p)
    V_Rd = Vpl/gamma_a1
elif lamb<=lamb_r:
    print('Seção semicompacta ',lamb,' <= ',lamb_r)
    V_Rd = lamb_p*Vpl/(lamb*gamma_a1)
else:
    print('Seção esbelta ',lamb,' > ',lamb_r)
    V_Rd = 1.24*((lamb_p/lamb)**2)*Vpl/gamma_a1

print('V_Rd = ',V_Rd)

if tem_carga_solic=='s':
    if V_Rd >= V_Sd:
        print(V_Rd,' >= ',V_Sd,' a peça resiste!')
    elif enrij=='n':
        print(V_Rd,' < ',V_Sd,' não resiste, colocando enrijecedores...')
        secao = input('Qual o tipo de seção que quero? [compacta/semicompacta/esbelta] ')
        if secao=='compacta':
            kv = (lamb**2)*fy/(1.21*E)
            # a = np.sqrt(E*(tw**2)*6.05/(fy*(hw**2)-E*(tw**2)*6.05))
        elif secao=='semicompacta':
            kv = (fy/(1.21*E))*(V_Sd*lamb*gamma_a1/Vpl)**2
            # a = np.sqrt(E*(tw**2)*9.3845/(fy*(hw**2)-E*(tw**2)*9.3845))
        # if kv<=5:
        #     sys.exit('Erro de kv<=5 antes de calcular a')
        a = np.sqrt((5*hw**2)/(kv-5))
        print('kv = ',kv)
        print('a = ',a)
        if a/hw > (260*tw/hw)**2 :
            kv = 5
            print ('a/hw=',a/hw,' > (260*tw/hw)**2=',(260*tw/hw)**2,' valor de a não verifica')
            print('kv = ',kv)
        else:
            print ('a/hw=',a/hw,' <= (260*tw/hw)**2=',(260*tw/hw)**2,' valor de a verificado')
            kv = 5 + 5*(hw**2)/a**2
            print('kv = ',kv)
        lamb_p = 1.1*np.sqrt(kv*E/fy)
        lamb_r = 1.37*np.sqrt(kv*E/fy)
        if lamb<=lamb_p:
            print('Seção compacta ',lamb,' <= ',lamb_p)
            V_Rd = Vpl/gamma_a1
        elif lamb<=lamb_r:
            print('Seção semicompacta ',lamb,' <= ',lamb_r)
            V_Rd = lamb_p*Vpl/(lamb*gamma_a1)
        else:
            print('Seção esbelta ',lamb,' > ',lamb_r)
            V_Rd = 1.24*((lamb_p/lamb)**2)*Vpl/gamma_a1
        print('V_Rd = ',V_Rd)
        if V_Rd >= V_Sd:
            print(V_Rd,' >= ',V_Sd,' a peça resiste!')
    if (enrij=='s' and V_Rd < V_Sd) or V_Rd < V_Sd:
        print(V_Rd,' < ',V_Sd,' não resiste mesmo, trocando perfil...')
        Vpl = V_Rd*gamma_a1
        Aw = Vpl/(0.6*fy)
        print('Nova Aw deve ser >= ',Aw)