import pygame, sys
from pygame.locals import *
import numpy as np 
import matplotlib.pyplot as plt
from player import Player
import time
import constanteMapa
import json
from monteCarlo import MonteCarlo
from maps import Mapa
import maps
import random
import os

MAX_RODADA = 800

SCREENW = constanteMapa.WIDTH*constanteMapa.SIZE_OBJECT
SCREENH =  constanteMapa.HEIGHT*constanteMapa.SIZE_OBJECT
clock = pygame.time.Clock()
def showFreeSpace(DISPLAY, x,y, color1 =constanteMapa.WHITE, color2 =constanteMapa.GRAY):
    if(x%2 != y%2):
        pygame.draw.rect(DISPLAY,color1,(x*constanteMapa.SIZE_OBJECT,y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT))
    else:    
        pygame.draw.rect(DISPLAY,color2,(x*constanteMapa.SIZE_OBJECT,y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT))
    
def showPlayer(DISPLAY, p1):
    if(p1.vida == 0):
        pygame.draw.rect(DISPLAY,(128,128,128),(p1.x*constanteMapa.SIZE_OBJECT,p1.y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT))
    else:
        pygame.draw.rect(DISPLAY,(255,0,0),pygame.Rect(p1.x*constanteMapa.SIZE_OBJECT,p1.y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT))
        pygame.draw.rect(DISPLAY,(0,0,0),pygame.Rect(p1.x*constanteMapa.SIZE_OBJECT,p1.y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT),2)
def showMap(DISPLAY,matrixMap,players,verbose,SPEED,bestPlayer = 0):
    if(verbose == True):
        count = 0
        for linha , x in zip(matrixMap,range(constanteMapa.WIDTH)):
            for elemento, y in zip(linha,range(constanteMapa.HEIGHT)):
                if(elemento == constanteMapa.INICIO):
                    pygame.draw.rect(DISPLAY,constanteMapa.LIGHT_GREEN,(x*constanteMapa.SIZE_OBJECT,y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT))
                if(elemento == constanteMapa.PAREDE):
                    pygame.draw.rect(DISPLAY,constanteMapa.LIGHT_PURPLE,(x*constanteMapa.SIZE_OBJECT,y*constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT,constanteMapa.SIZE_OBJECT))
                if(elemento == constanteMapa.LIVRE):
                    showFreeSpace(DISPLAY,x,y)
                if(elemento > constanteMapa.INIMIGO):
                    showFreeSpace(DISPLAY,x,y)
                    pygame.draw.circle(DISPLAY, constanteMapa.BLACK, (x*constanteMapa.SIZE_OBJECT + constanteMapa.SIZE_OBJECT/2, y*constanteMapa.SIZE_OBJECT + constanteMapa.SIZE_OBJECT/2), 6,1)
                    pygame.draw.circle(DISPLAY, constanteMapa.BLUE, (x*constanteMapa.SIZE_OBJECT + constanteMapa.SIZE_OBJECT/2, y*constanteMapa.SIZE_OBJECT + constanteMapa.SIZE_OBJECT/2), 5)                            
        for p1, index in zip(players,range(len(players))):
            # apagar essa linha caso não queira exibir os sensores
            p1.readSensor(DISPLAY, matrixMap,-1)
            if(matrixMap[p1.x][p1.y] > constanteMapa.INIMIGO):
                p1.vida = 0
            showPlayer(DISPLAY, p1)
        if(verbose == True):
            pygame.display.update()
    else:
        for p1, index in zip(players,range(len(players))):
            if(matrixMap[p1.x][p1.y] > constanteMapa.INIMIGO):
                p1.vida = 0
    return 1

 

def criaMapa(WIDTH,HEIGHT):
    mapa = np.loadtxt(open("mapa1.csv", "rb"), delimiter=",")
    mapa = np.transpose(mapa)
    return mapa
def movimentaPlayer(p1,mapa,movimento):
    return p1.step(mapa, movimento)
def inicializaPlayers(size, name, prefix, desconto, epsilon):
    players = []
    MCs = []
    
    for _ in range(size):
        players.append(Player(1,13))
        # players.append(Player(36,16))
        MCs.append(MonteCarlo(name, prefix, desconto, epsilon))
    return players, MCs
def loadMC(MCs):
    for i in range(len(MCs)):
        MCs[i].loadMC()
def mainGame(DISPLAY, players,isMaquina,verbose,MCs,enemy,SPEED, bestPlayer=-1) :

    stateHistory = []
    actionHistory = []
    recompenseHistory = []
    goalY = []
    goalY2 = []

    # mapa
    mapa = criaMapa(constanteMapa.WIDTH,constanteMapa.HEIGHT)
    count = 0
    fimJogo = False
    NUMERO_RODADA = 0

    while not(fimJogo):
        if(isMaquina and NUMERO_RODADA > MAX_RODADA ):
            # recompenseHistory[-1] -= 50000*NUMERO_RODADA
            for p1,MC in zip(players, MCs):
                if(p1.vida == 1): 
                    p1.vida = 0
            break
        #Vez do player
        print('vez do player')
        print(players[0].x,players[0].y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); #sys.exit() if sys is imported
            if event.type == pygame.KEYDOWN:
                isMaquina = False
                print(event.key)
                # pause = p
                if event.key == 112:                    
                    print(players[0].__dict__)
                if event.key == 105:                    
                    players[0].readSensor(DISPLAY, mapa,-1)# já configura os sensoress
                if(movimentaPlayer(players[0],mapa,event.key) == 0): 
                    fimJogo = True
        # Vez da Maquina
        if(isMaquina):
            for p1,MC,index in zip(players,MCs,range(len(players))):        
                if(p1.vida == 1):
                    estado = {}
                    estado['sensor'] = p1.readSensor(DISPLAY, mapa,-1)
                    estado['x'] = p1.x
                    estado['y'] = p1.y
                    action = MC.movimentaAgente(json.dumps(estado), mapa)
                    actionHistory.append(action)
                    recompense = None
                    if(movimentaPlayer(p1,mapa,action) == 0): 
                        fimJogo = True
                    if not(json.dumps(estado) in stateHistory):
                        recompense = MC.getRecompense({'x': p1.x, 'y':p1.y})
                    else:
                        recompense = 0
                    stateHistory.append(json.dumps(estado))
                    recompenseHistory.append(recompense)
        # Vez do inimigo                    
        for a in enemy:
            a.step(mapa)
        if(fimJogo): break
        fimJogo = True
        for p1 in players:
            if(p1.vida == 1): 
                fimJogo = False
                # recompenseHistory[-1] -= 30
        
        showMap(DISPLAY,mapa,players,verbose,bestPlayer) 
        if(SPEED != 0):
            time.sleep(SPEED)
        NUMERO_RODADA += 1
    stateHistory.reverse()
    actionHistory.reverse()
    recompenseHistory.reverse()
    MCs[0].ganhoPorEpisodio.append(recompenseHistory[0])
    G = 0
    for p1,MC in zip(players,MCs):
        for state,action,recompense, t in zip(stateHistory, actionHistory,recompenseHistory, range(len(stateHistory))):
            # if(t + 1 < len(stateHistory)):
                G = MC.DESCONTO*G + recompenseHistory[t]
                if True:
                    if state in MC.S_A:
                        if action in MC.S_A[state]:
                            MC.S_A[state][action] = np.insert(MC.S_A[state][action],0, G)
                        else:
                            # print('inseririu novo')
                            MC.S_A[state][action] =  np.asarray([G])
                    else:
                        MC.S_A[state] = {action: np.asarray([G])}

                    if(state in MC.Q_A):
                        if(action in MC.Q_A[state]):
                            MC.Q_A[state][action] = MC.S_A[state][action].mean()
                        else:
                            MC.Q_A[state][action] =  MC.S_A[state][action].mean()
                    else:
                        MC.Q_A[state] = {action: MC.S_A[state][action].mean()}
                
                    MC.POLITICA[state] = max(MC.Q_A[state], key=MC.Q_A[state].get)
                    # for actionsAnalized in MC.Q_A[state]:
                    #     print(actionsAnalized)
                    #     maxValue = -9999
                    #     maxAction = max(actionsAnalized, key=actionsAnalized.get)
                    #     if( maxAction > maxValue):
                    #         maxValue = maxAction
                    #         MC.POLITICA[state] = actionsAnalized.argmax()
    return 1
    
def saveAllGraphs(configuracoes, MC, rodada):
    print('salvando todas as configurações')
    fig,ax=plt.subplots(figsize=(25,10)) 
    
    firstKey = list(configuracoes.keys())[0]
    x = [i*MC.TAMANHO_JANELA_MOVEL for i in range(1,len(configuracoes[firstKey])+1)]
    
    fig,ax=plt.subplots(figsize=(20,15))
    ax.set_xlabel('N-ésimo Episódio') 
    ax.set_ylabel('Ganho') 
    ax.set_title('Ganho por Episodio') 
    info = {}
    for key in configuracoes:
        arrayMean = configuracoes[key]/rodada
        arrayIndexEqualMax = np.where(arrayMean > 1)[0]
        if(len(arrayIndexEqualMax) > 0):
            info[key] = arrayIndexEqualMax[0]*MC.TAMANHO_JANELA_MOVEL
        else:
            info[key] = 99999999
        
        plt.plot(x, arrayMean, label=key)
        del arrayMean

    sorted_dict = {}
    sorted_keys = sorted(info, key=info.get)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = info[w]
    fo = open("./MC_SAVED/info.txt", "a")
    fo.write( "\nRODADA " +str(rodada) + "\n")
    fo.write(str(sorted_dict))
    fo.close()
    plt.legend(loc="upper left")
    #save and display the plot 
    plt.savefig('./MC_SAVED/' + str(rodada) + '_allSettings.png',dpi=300,bbox_inches='tight')
    
def main():
    #caso queira jogar só
    pygame.init()
    pygame.font.init() 
    pygame.display.set_caption('O Jogo Mais Difícil Do Mundo')
    DISPLAY = pygame.display.set_mode((SCREENW,SCREENH))
    
    players = []   
    episodio = 0
    mapa = Mapa()
    configuracoes = {}

    TAXA_FRAME = 1
    # SPEED = 0.2
    
    # TAXA_FRAME = 1000
    SPEED = 0
        
    # TOTAL_EPISODE = 3000
    # DESCONTOS = [0.3, 0.5, 0.6, 0.7, 0.9]
    # EPSILONS = [0.03,0.1, 0.2,0,3]    
    TOTAL_EPISODE = 50000
    DESCONTOS = [0.9, 0.8]
    EPSILONS = [0.1, 0.2]
    for rodada in range(1,2):
        print('rodada: ' + str(rodada))
        for desconto in DESCONTOS:
            for epsilon in EPSILONS:
                prefix = 'i_' + str(rodada) + '_'
                name = 'd_' + str(desconto) + '_e_' + str(epsilon)
                numPlayers = 1
                players, MCs  = inicializaPlayers(numPlayers,name, prefix, epsilon, desconto )
                loadMC(MCs)
                while(MCs[0].episode < TOTAL_EPISODE):
                    MCs[0].increaseEpisode()
                    enemy = maps.setMap1() # cria inimigos 1, 2 e 3
                    MCs[0].loadSteps()

                    # enemy = mapa.loadMap4() # cria inimigos 4, 5 e 6
                    isNeedSalve = MCs[0].episode%10000 == 0
                    verbose = episodio % TAXA_FRAME == 0
                    if(verbose): print('episódio: ', episodio)
                    players[0].vida = True
                    players[0].reset()
                    mainGame(DISPLAY, players,True,verbose, MCs, enemy, SPEED)
                    episodio += 1
                    if(isNeedSalve):
                        print('salvou MC')
                        MCs[0].salvarMC()
                if(rodada==1):
                    configuracoes[MCs[0].name] = MCs[0].plotarGrafico2()
                else:
                    configuracoes[MCs[0].name] += MCs[0].plotarGrafico2()
                del MCs, players
        saveAllGraphs(configuracoes,MonteCarlo('','',1,1),rodada)
main()