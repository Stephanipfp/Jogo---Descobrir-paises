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

def haversine(r,listageo):
    la1r=radians(listageo[0])
    lo1r=radians(listageo[1])
    la2r=radians(listageo[2])
    lo2r=radians(listageo[3])
    a=sin((la2r-la1r)/2)
    b=sin((lo2r-lo1r)/2)
    d=2*r*asin(sqrt(a**2 + cos(la1r) * cos(la2r) * b**2))
    return d

def adiciona_em_ordem(nome,d,lista):
    if [nome, d] in lista:
        return lista
    elif lista==[]:
        lista.append([nome,d])
        return lista
    else:
        lista2=[]
        for pais in lista:
            if [nome, d] in lista2:
                lista2.append(pais)
            elif pais[1]>d:
                lista2.append([nome,d])
                lista2.append(pais)
            else:
                lista2.append(pais)

        if lista2==lista:
            lista2.append([nome,d])
            
    return lista2

def esta_na_lista(nome,lista):
    for i in lista:
        if nome in i:
            return True
    return False

def sorteia_letra(p,lista):
    caracesp=['.', ',', '-', ';', ' ']
    lista2=[]
    for l in p.lower():
        if l not in caracesp and l not in lista:
            lista2.append(l)
    letra=random.choice(lista2)
    return letra

def cor_bandeira(dicnp):
    cores=dicnp['bandeira']
    listacor=[]
    for k,v in cores.items():
        if v!=0:
            listacor.append(k)
    return listacor

def soma_cor(dicnp):
    cores=dicnp['bandeira']
    somacor=0
    for k,v in cores.items():
        if v!=0:
            somacor+=1
    return somacor

def info_geo(dicnp,dicnpp):
    geo1=dicnp['geo']
    geo2=dicnpp['geo']
    la1=geo1['latitude']
    lo1=geo1['longitude']
    la2=geo2['latitude']
    lo2=geo2['longitude']
    listageo=[la1,lo1,la2,lo2]
    return listageo    
    
def inventario(lista):
    listainvent=[]
    for l in lista:
        if len(l)>1:
            listainvent.append(''.join(l))
    return listainvent

raio = 6371

jogar=0

while jogar!='n':
    dicnormal=normaliza(dic)
    pais=sorteia_pais(dicnormal)
    print(pais)
    dicpais=dicnormal[pais]
    inventcor=['Cores da bandeira: ']
    inventcap=['Letras da Capital: ']
    inventarea=['Área: ']
    inventpop=['População: ']
    inventcont=['Continente: ']
    inventdis=['Distâncias: ']
    invent=[inventdis,inventcor,inventcap,inventarea,inventpop,inventcont]
    inventdicas=['Dicas:',inventcor,inventcap,inventarea,inventpop,inventcont]

    listacap=[]
    listadis=[]
    listapaises=[]

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

    tentativas=20
    certeza=0
    mercdicas=['Mercado de Dicas','----------------------------------------','0. Sem dica','1. Cor da bandeira  -> custa 4 tentativas','2. Letra da capital -> custa 3 tentativas','3. Área             -> custa 6 tentativas','4. População        -> custa 5 tentativas','5. Continente       -> custa 7 tentativas','----------------------------------------']
    if jogar=='s':
        jogar=0
    while certeza!='s' and jogar!='s':
        palpite=input('Qual o seu palpite? ')
        print(' ')
        if palpite.lower()==pais:
            print('Parabéns, você acertou o país!')
            jogar=input('Deseja jogar novamente? [s|n] ')
            if jogar=='n':
                certeza='s'                    
            if jogar.lower()!='s' and jogar.lower()!='n':
               print('Essa resposta não é válida')

        while palpite!='desisto' and tentativas!=0 and palpite!=pais:
            if palpite.lower()=='dica':
                if tentativas<3:
                    print('Você não tem pontos suficientes')
                    opcao=0
                if tentativas<4:
                    if '1. Cor da bandeira  -> custa 4 tentativas' in mercdicas:
                        del mercdicas[mercdicas.index('1. Cor da bandeira  -> custa 4 tentativas')] 
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
                    if opcao!='0' and opcao!='1' and opcao!='2' and opcao!='3' and opcao!='4' and opcao!='5':
                        print('Essa opção não é válida')        
                if opcao=='0':
                    tentativas=tentativas
                elif opcao=='1':
                    if tentativas<4:
                        print('Número de tentativas insuficiente')
                    elif len(inventcor)==1:
                        listacor=cor_bandeira(dicpais)
                        cor=random.choice(listacor)
                        corok='{}'.format(cor)
                        inventcor.append(corok)
                        print(''.join(inventcor))
                        listacor2=listacor
                        del listacor2[listacor.index(cor)]  
                        tentativas-=4              
                    else:
                        if listacor2!=[]:
                            cor=random.choice(listacor2)
                            corok=', {}'.format(cor)
                            inventcor.append(corok)
                            print(''.join(inventcor))
                            del listacor2[listacor2.index(cor)]
                            tentativas-=4
                        else:
                            if '1. Cor da bandeira  -> custa 4 tentativas' in mercdicas:
                                del mercdicas[mercdicas.index('1. Cor da bandeira  -> custa 4 tentativas')]
                            print('Cores esgotadas')
                            tentativas=tentativas
                elif opcao=='2':
                    capital=dicpais['capital']
                    if len(inventcap)-1<len(capital):
                        letra=sorteia_letra(capital,listacap)
                        listacap.append(letra)
                        letraok='{},'.format(letra)
                        inventcap.append(letraok)
                        print(''.join(inventcap))
                    else:
                        print('Letras esgotadas')
                        del mercdicas[mercdicas.index('2. Letra da capital -> custa 3 tentativas')]
                        opcao=0
                    tentativas-=3
                elif opcao=='3':
                    if '3. Área             -> custa 6 tentativas' in mercdicas:
                        area=dicpais['area']
                        areaok='{} km'.format(area)
                        inventarea.append(areaok)
                        print(''.join(inventarea))
                        del mercdicas[mercdicas.index('3. Área             -> custa 6 tentativas')]
                        tentativas-=6
                    else:
                        print('Você já usou essa dica')
                elif opcao=='4':
                    if '4. População        -> custa 5 tentativas' in mercdicas:
                        populacao=dicpais['populacao']
                        populacaok='{} habitantes'.format(populacao)
                        inventpop.append(populacaok)
                        print(''.join(inventpop))
                        del mercdicas[mercdicas.index('4. População        -> custa 5 tentativas')]
                        tentativas-=5
                    else:
                        print('Você já usou essa dica')
                elif opcao=='5':
                    if '5. Continente       -> custa 7 tentativas' in mercdicas:
                        continente=dicpais['continente']
                        inventcont.append(continente)
                        print(''.join(inventcont))
                        del mercdicas[mercdicas.index('5. Continente       -> custa 7 tentativas')]
                        tentativas-=7
                    else:
                        print('Você já usou essa dica')
            elif palpite.lower()=='inventario':
                inventok=inventario(invent)
                print('\n'.join(inventok))
            elif palpite.lower() not in dicnormal:
                print('País desconhecido')
            else:
                verifica=esta_na_lista(palpite,listadis)
                if verifica==False:
                    dicpaispal=dicnormal[palpite.lower()]
                    listageo=info_geo(dicpais,dicpaispal)
                    d=int(haversine(raio,listageo))
                    listadisordem=adiciona_em_ordem(palpite.lower(),d,listadis)
                    listadis=listadisordem
                    for k in listadisordem:
                        ds=str(k[1])
                        dok='{}km'.format(ds)
                        dispais=[dok,k[0]]                
                        dispaisok=' -> '.join(dispais)
                        if dispaisok not in inventdis:
                            inventdis.append(dispaisok)
                    dis='\n'.join(inventdis)
                    invent[0]=dis
                    print(dis)
                    inventdicasok=inventario(inventdicas)
                    print('\n'.join(inventdicasok))
                    inventdis=['Distâncias: ']
                    tentativas-=1
                else:
                    print('Esse palpite já foi dado')
            if palpite.lower()!=pais:
                print('Você tem {} tentativas'.format(tentativas))
            if tentativas!=0 and palpite.lower()!=pais:
                palpite=input('Qual o seu palpite? ')
        if tentativas==0 and palpite!=pais:
            print('Você não adivinhou o país, o correto era {}'.format(pais))
        elif palpite.lower()=='desisto':
            certeza=input('Tem certeza que deseja desistir da rodada? [s|n] ')
            if certeza.lower()=='s':
                print('O país era {}'.format(pais))
                jogar=input('Deseja jogar novamente? [s|n] ')                    
                if jogar.lower()!='s' and jogar.lower()!='n':
                    print('Essa resposta não é válida')  
            elif certeza.lower()!='s' and certeza.lower()!='n':
                print('Essa resposta não é válida')
        elif tentativas==0 and palpite==pais:
            print('Parabéns, você acertou o país!')

print('Até a próxima!')