import json
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
    

dicnormal=normaliza(dic)
pais=sorteia_pais(dicnormal)
dicpais=dicnormal[pais]
inventcor=''

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
palpite=input('Qual o seu palpite? ')
tentativas=20
while palpite!='desisto' and tentativas!=0:
    if palpite=='dica':
        if tentativas<3:
            print('Você não tem pontos suficientes')
            palpite=input('Qual o seu palpite? ')
            opcao=0
        elif tentativas<4:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('0. Sem dica')
            print('2. Letra da capital -> custa 3 tentativas')
            print('----------------------------------------')
            print(' ')
            opcao=input('Escolha sua opção [0|1|2]: ')
        elif tentativas<5:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('0. Sem dica')
            print('1. Cor da bandeira  -> custa 4 tentativas')
            print('2. Letra da capital -> custa 3 tentativas')
            print('----------------------------------------')
            print(' ')
            opcao=input('Escolha sua opção [0|1|2]: ')
        elif tentativas<6:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('0. Sem dica')
            print('1. Cor da bandeira  -> custa 4 tentativas')
            print('2. Letra da capital -> custa 3 tentativas')
            print('4. População        -> custa 5 tentativas')
            print('----------------------------------------')
            print(' ')
            opcao=input('Escolha sua opção [0|1|2|4]: ')
        elif tentativas<7:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('0. Sem dica')
            print('1. Cor da bandeira  -> custa 4 tentativas')
            print('2. Letra da capital -> custa 3 tentativas')
            print('3. Área             -> custa 6 tentativas')
            print('4. População        -> custa 5 tentativas')
            print('----------------------------------------')
            print(' ')
            opcao=input('Escolha sua opção [0|1|2|3|4]: ')
        else:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('0. Sem dica')
            print('1. Cor da bandeira  -> custa 4 tentativas')
            print('2. Letra da capital -> custa 3 tentativas')
            print('3. Área             -> custa 6 tentativas')
            print('4. População        -> custa 5 tentativas')
            print('5. Continente       -> custa 7 tentativas')
            print('----------------------------------------')
            print(' ')
            opcao=input('Escolha sua opção [0|1|2|3|4|5]: ')
        if int(opcao)<0 or int(opcao)>5:
            print('Essa opção não existe')       
        elif opcao=='0':
            tentativas=tentativas
        elif opcao=='1':
            if tentativas<4:
                print('Número de tentativas insuficiente')
                opcao=input('Escolha sua opção [0|2|3|4|5]: ')
            if inventcor=='':
                listacor=cor_bandeira(dicpais)
                cor=random.choice(listacor)
                inventcor+=cor
                print('Cores da bandeira: {}'.format(inventcor))
                listacor2=listacor
                del listacor2[listacor.index(cor)]                
            else:
                if listacor2!=[]:
                    cor=random.choice(listacor2)
                    inventcor+=', '+cor
                    print('Cores da bandeira: {}'.format(inventcor))
                    del listacor2[listacor.index(cor)]
                else:
                    print('Cores esgotadas')
            tentativas-=4
        elif opcao=='2':
            tentativas-=3
        elif opcao=='3':
            tentativas-=6
        elif opcao=='4':
            tentativas-=5
        elif opcao=='5':
            tentativas-=7
    else:
        tentativas-=1
    print('Você tem {} tentativas'.format(tentativas))
    palpite=input('Qual o seu palpite? ')
    
    

