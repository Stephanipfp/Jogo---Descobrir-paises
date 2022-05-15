import json
from pickle import TRUE
import random
from math import *

with open('base.json', 'r') as arquivoj:
    texto = arquivoj.read()
dic = json.loads(texto)

def normaliza(dic):
    dicnormal={}
    for continente, p in dic.items():
        for namep,infop in p.items():
            dicnormal[namep]=infop
            infop['continente']=continente
    return dicnormal

def sorteia_pais(dicn):
    listapais=[]
    for k in dicn:
        listapais.append(k)
    pais=random.choice(listapais)
    return pais

def cor_bandeira(dicnp):
    cores=dicnp['bandeira']
    listacor=[]
    for k,v in cores.items():
        if v!=0:
            listacor.append(k)
    return listacor
    
def letra_capital(dicnp):
    capital=dicnp['capital']
    listacap=[]
    for l in capital:
        listacap.append(l)
    return listacap

def info_geo(dicnp,dicnpp):
    geo1=dicnp['geo']
    geo2=dicnpp['geo']
    la1=geo1['latitude']
    lo1=geo1['longitude']
    la2=geo2['latitude']
    lo2=geo2['longitude']
    listageo=[la1,lo1,la2,lo2]
    return listageo

def haversine(r,listageo):
    la1r=radians(listageo[0])
    lo1r=radians(listageo[1])
    la2r=radians(listageo[2])
    lo2r=radians(listageo[3])
    a=sin((la2r-la1r)/2)
    b=sin((lo2r-lo1r)/2)
    d=2*r*asin(sqrt(a*2 + cos(la1r) * cos(la2r) * b*2))
    return d


dicnormal=normaliza(dic)
pais=sorteia_pais(dicnormal)
dicpais=dicnormal[pais]
inventcor=[]
inventcap=[]
inventdis=['Distâncias:']

raio = 6371

print('==============================')
print('|                            |')
print('|BEM VINDO AO JOGO DOS PAÍSES|')
print('|                            |')
print('=========by:Ste & Mel=========')
print(' ')
print('Comandos:')
print(' ')
print('dica       -> abre o mercado de dicas')
print('desisto    -> desiste da rodada')
print('inventario -> exibe sua posição')
print(' ')
print('Tente adivinhar o país escolhido!')
print(' ')
print('Você tem 20 tentativa(s)')
print(' ')

mercdicas=['Mercado de Dicas','----------------------------------------','0. Sem dica','1. Cor da bandeira  -> custa 4 tentativas','2. Letra da capital -> custa 3 tentativas','3. Área             -> custa 6 tentativas','4. População        -> custa 5 tentativas','5. Continente       -> custa 7 tentativas','----------------------------------------']

palpite=input('Qual o seu palpite? ')
tentativas=20

while palpite!='desisto' and tentativas!=0:
    dicpaispal=dicnormal[palpite]
    listageo=info_geo(dicpais,dicpaispal)
    d=str(int(haversine(raio,listageo)))
    ds='{}km'.format(d)
    dispais=[ds,palpite]
    dispaisok=' -> '.join(dispais)
    inventdis.append(dispaisok)
    if palpite not in dicnormal:
        print('País desconhecido')   
    if palpite=='dica':
        if tentativas<3:
            print('Você não tem pontos suficientes')
            palpite=input('Qual o seu palpite? ')
            opcao=0  
        elif tentativas<5:
            if '4. População        -> custa 5 tentativas' in mercdicas:
                del mercdicas[mercdicas.index('4. População        -> custa 5 tentativas')]
        elif tentativas<6:
            if '3. Área             -> custa 6 tentativas' in mercdicas:
                del mercdicas[mercdicas.index('3. Área             -> custa 6 tentativas')]
        elif tentativas<7:
            if '5. Continente       -> custa 7 tentativas' in mercdicas:
                del mercdicas[mercdicas.index('5. Continente       -> custa 7 tentativas')]
        if tentativas>3:
            merc='\n'.join(mercdicas)
            print(merc)
            opcao=input('Escolha sua opção: ')
        if int(opcao)<0 or int(opcao)>5:
            print('Essa opção não existe')       
        elif opcao=='0':
            tentativas=tentativas
        elif opcao=='1':
            if tentativas<4:
                print('Número de tentativas insuficiente')
                opcao=0
            if inventcor==[]:
                listacor=cor_bandeira(dicpais)
                cor=random.choice(listacor)
                inventcor.append(cor)
                print('Cores da bandeira: {}'.format(','.join(inventcor)))
                listacor2=listacor
                del listacor2[listacor.index(cor)]              
            else:
                if listacor2!=[]:
                    cor=random.choice(listacor2)
                    inventcor.append(cor)
                    print('Cores da bandeira: {}'.format(','.join(inventcor)))
                    del listacor2[listacor2.index(cor)]
                else:
                    print('Cores esgotadas')
                    del mercdicas[mercdicas.index('1. Cor da bandeira  -> custa 4 tentativas')]
                    opcao=0
            tentativas-=4
        elif opcao=='2':
            if inventcap==[]:
                listacap=letra_capital(dicpais)
                letra=random.choice(listacap)
                inventcap.append(letra)
                print('Letras da capital: {}'.format(','.join(inventcap)))
                listacap2=listacap
                del listacap2[listacap.index(letra)]
            else:
                if listacap2!=[]:
                    letra=random.choice(listacap2)
                    inventcap.append(letra)
                    print('Letras da capital: {}'.format(','.join(inventcap)))
                    del listacap2[listacap2.index(letra)]
                else:
                    print('Letras esgotadas')
                    del mercdicas[mercdicas.index('2. Letra da capital -> custa 3 tentativas')]
                    opcao=0
            tentativas-=3
        elif opcao=='3':
            if '3. Área             -> custa 6 tentativas' in mercdicas:
                area=dicpais['area']
                print('{} km'.format(area))
                del mercdicas[mercdicas.index('3. Área             -> custa 6 tentativas')]
                tentativas-=6
            else:
                print('Você já usou essa dica')
        elif opcao=='4':
            if '4. População        -> custa 5 tentativas' in mercdicas:
                populacao=dicpais['populacao']
                print('{} habitantes'.format(populacao))
                del mercdicas[mercdicas.index('4. População        -> custa 5 tentativas')]
                tentativas-=5
            else:
                print('Você já usou essa dica')
        elif opcao=='5':
            if '5. Continente       -> custa 7 tentativas' in mercdicas:
                continente=dicpais['continente']
                print(continente)                
                del mercdicas[mercdicas.index('5. Continente       -> custa 7 tentativas')]
                tentativas-=7
            else:
                print('Você já usou essa dica')
    else:
        tentativas-=1
        dis='\n'.join(inventdis)
        print(dis)
        print('Você tem {} tentativas'.format(tentativas))
    palpite=input('Qual o seu palpite? ')
    
    

