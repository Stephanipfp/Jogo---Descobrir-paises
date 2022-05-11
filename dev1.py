import json
import random
from math import *

with open('base.json', 'r') as arquivo:
    texto = arquivo.read()

dic = json.loads(texto)

def normaliza(dic):
    dicnormal={}
    for continente, p in dic.items():
        for namep,infop in p.items():
            dicnormal[namep]=infop
            infop['continente']=continente
    return dicnormal

print('==============================')
print('|                            |')
print('|BEM VINDO AO JOGO DOS PAÍSES|')
print('|                            |')
print('=========by:Ste & Mel=========')

print('Comandos:')
print('dica       -> abre o mercado de dicas')
print('desisto    -> desiste da rodada')
print('inventario -> exibe sua posição')

raio = 6371

print('Tente adivinhar o país escolhido!')
print('Você tem 20 tentativa(s)')

palpite=input('Qual o seu palpite? ')
tentativas=20
while palpite!='desisto':
    if palpite=='dica':
        print('Mercado de Dicas')
        print('----------------------------------------')
        print('0. Sem dica')
        print('1. Cor da bandeira  -> custa 4 tentativas')
        print('2. Letra da capital -> custa 3 tentativas')
        print('3. Área             -> custa 6 tentativas')
        print('4. População        -> custa 5 tentativas')
        print('5. Continente       -> custa 7 tentativas')
        print('----------------------------------------')
        opcao=input('Escolha sua opção [0|1|2|3|4|5]: ')
        if opcao=='0':
            tentativas=tentativas
        elif opcao=='1':
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
    
    

