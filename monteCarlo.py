# estado['U': 1.0, 'UCount': 22,..., 'UL': 11.0, 'ULCount': 3]: {
#   up: 2.255774,
#   down: -2,
#   left: 0,
#   rigth: 0,
# 
# }
import timeit
import constanteMapa
import random
import json
import pickle
import matplotlib.pyplot as plt 
import numpy as np
import os



V_S_INICIAL = 10000

ACTIONS = [
    # constanteMapa.MOV_STOP,
    constanteMapa.MOV_UP,
    constanteMapa.MOV_DOWN, 
    constanteMapa.MOV_LEFT, 
    constanteMapa.MOV_RIGHT] # up,down, left and right

class MonteCarlo:
    # # def __init__(self,name, prefix, EPSILON, DESCONTO):
    def __init__(self,name, prefix, EPSILON,DESCONTO):
        print("inicializou")
        self.maiorPontuacao = 0
        self.name = name
        self.prefix = prefix
        self.createdAt = timeit.default_timer()
        self.qtdChegouNoObjetivo = 0
        self.episode = 0
        # dados para gerar grafico
        self.qtdPassos = 0
        self.passosPorObjetivo = []
        self.ganhoPorEpisodio = []
        self.TAMANHO_JANELA_MOVEL = 100
        #
        self.EPSILON = EPSILON
        self.DESCONTO = DESCONTO
        self.POLITICA = {}
        self.Q_A = {}
        self.S_A = {} # {S1: [G1,G2,G3]}f
        self.stepsHistory = []
        self.isLoadSteps = False
    def increaseEpisode(self):
        self.qtdPassos = 0
        self.stepsHistory = []
        if(self.isLoadSteps): self.loadSteps()
        self.episode += 1
        self.notUseRandomAction = True
    #manipulating the first Axes 
    def plotarGrafico1(self):
        for indice in range(0,50,10):
            fig,ax=plt.subplots(figsize=(10,5)) 
            y = np.asarray(self.passosPorObjetivo.copy())
            x = [i + indice for i  in range(1,len(y[indice:]) + 1)] 
            ax.plot(x,y[indice:])
            ax.set_xlabel('N-ésima vez que chegou no objetivo') 
            ax.set_ylabel('Quantidade de Passos para chegar no objetivo') 
            ax.set_title('Número de passos até chegar no objetivo') 
            #save and display the plot 
            plt.savefig('./MC_SAVED/' + self.prefix + '_' +self.name+ '_grafico1_' + str(indice) + '.png',dpi=200,bbox_inches='tight')
            plt.close('all')
        
    def runningMeanFast(self,array, N):
        myArray = np.asarray(array)
        arrayRunningMean = []
        arrayRunningMax = []  
        arrayRunningIndiceML = []
        for i in range(0,len(myArray),N):
            if(i+N >= len(myArray) ):
                return arrayRunningMean, arrayRunningMax, arrayRunningIndiceML
            arrayAnalized = myArray[i:i+N].copy()
            arrayRunningMean.append(np.mean(arrayAnalized))
            arrayRunningMax.append(np.max(arrayAnalized))
            arrayAnalized.sort()
            arrayRunningIndiceML.append(arrayAnalized[-10:-5].mean()) # tiro os  melhores e faço uma media dos 5melhores que sobrou
            
            
        return np.convolve(x, np.ones((N,))/N)[(N-1):]
    def plotarGrafico2(self):
        fig,ax=plt.subplots(figsize=(25,10)) 
        ganhoPorEpisodio = self.ganhoPorEpisodio.copy()
        
        yMean, yMax, yIndiceML = self.runningMeanFast(ganhoPorEpisodio,self.TAMANHO_JANELA_MOVEL)
        x = [i*self.TAMANHO_JANELA_MOVEL for i in range(1,len(yMax)+1)] 
        
        plt.plot(x, yMean, "-b", label="mean")
        plt.plot(x, yMax, "-r", label="max")
        plt.plot(x, yIndiceML, "-g", label="IndiceML")
        plt.legend(loc="upper left")
        # plt.savefig('./teste.png',dpi=300,bbox_inches='tight')
        # ax.plot(x,yMean)
        # ax.plot(x,yMax)
        ax.set_xlabel('N-ésimo Episódio') 
        ax.set_ylabel('Ganho') 
        ax.set_title('Ganho por Episodio') 
        #save and display the plot 
        path = './MC_SAVED/rodada_' + self.prefix + '/'
        if(not(os.path.isdir(path))):
            os.mkdir(path)
        plt.savefig( path +self.name+ '_grafico2.png',dpi=300,bbox_inches='tight')
        plt.close('all')
        return np.asarray(yIndiceML)
    def salvarMC(self):
        config = {
            "Q_A": self.Q_A,
            "S_A": self.S_A,
            "POLITICA": self.POLITICA,
            "EPSILON": self.EPSILON,
            "DESCONTO": self.DESCONTO
            }
        arquivo = open("MC_SAVED/config.pkl", "wb")
        pickle.dump(config, arquivo)
        arquivo.close()
        
        fim = timeit.default_timer()
        duracao = (fim - self.createdAt)/60
        file_object = open('MC_SAVED/logs.txt', 'a')
        file_object.write(f'Chegou ao alvo no episodio: {self.episode}  aos {duracao} minutos \n')
        file_object.close()
        # arquivo = open("MC_SAVED/S_A.pkl", "wb")
        # pickle.dump(self.S_A, arquivo)
        # arquivo.close()
        # arquivo = open("MC_SAVED/POLITICA.pkl", "wb")
        # pickle.dump(self.POLITICA, arquivo)
        # arquivo.close()
        # arquivo = open("MC_SAVED/POLITICA.pkl", "wb")
        # pickle.dump(self.POLITICA, arquivo)
        # arquivo.close()
    
    def loadMC(self): 
        arquivo = open("MC_SAVED/config.pkl", "rb")
        config = pickle.load(arquivo)
        arquivo.close()
        self.Q_A = config['Q_A']
        self.S_A = config['S_A']
        self.POLITICA = config['POLITICA']
        self.DESCONTO = config['DESCONTO']
        self.EPSILON = config['EPSILON']
    
    def calculateDistance(self, point1, point2):
        return pow(pow(point2['x'] - point1['x'],2) + pow(point2['y'] - point1['y'],2),1/2)
    def loadSteps(self):
        self.isLoadSteps = True
        arquivoloaded = open("MC_SAVED/steps.npy", "rb")
        # arquivoloaded = open("MC_SAVED/chegouObjetivo.npy", "rb")
        self.stepsHistory = np.load(arquivoloaded)
    def loadStepsParte2(self):
        self.isLoadSteps = True
        # arquivoloaded = open("MC_SAVED/steps.npy", "rb")
        arquivoloaded = open("MC_SAVED/chegouObjetivo.npy", "rb")
        self.stepsHistory = np.load(arquivoloaded)
        # self.qtdPassos = 0
    def saveSteps(self,name='steps'):
        arquivo = open("MC_SAVED/"+name+".npy", "wb")
        np.save(arquivo, np.array(self.stepsHistory))
    def getRecompense(self, point):
        recompensaSecundaria = self.calculateDistance(point,{'x': constanteMapa.xMaxMap + 7, 'y': constanteMapa.yMinMap } )
        if point['x'] < constanteMapa.xMinMap:
            pontoIdeal = {'x': constanteMapa.xMinMap, 'y': constanteMapa.yMaxMap }
        elif point['x'] >= constanteMapa.xMinMap :
            recompensaSecundaria = 0
            pontoIdeal = {'x': constanteMapa.xMaxMap +7 , 'y': constanteMapa.yMinMap }
        
        recompensa = self.calculateDistance(point,pontoIdeal )
        if(recompensa + recompensaSecundaria == 0):
            # print("chegou no objetivo")
            self.passosPorObjetivo.append(self.qtdPassos)
            self.qtdPassos = 0
            if(self.notUseRandomAction): 
                print("nao usou randomAction")
            print("chegou no objetivo")
            # self.saveSteps('chegouObjetivo')
            return 11111111111111
        if(1/(recompensa + recompensaSecundaria) > self.maiorPontuacao):
            print('atingiu maior pontuação')
            self.maiorPontuacao = 1/(recompensa + recompensaSecundaria)
            # self.saveSteps('maiorPontuacao')
        return 1/(recompensa + recompensaSecundaria)
    def spaceIsEmpty(self,x,y,mapa):
        return mapa[x][y] == constanteMapa.INICIO or mapa[x][y] == constanteMapa.LIVRE
    def validaMovimento(self, action, estado, mapa):
        if(action == constanteMapa.MOV_DOWN):
            return self.spaceIsEmpty(estado["x"],estado["y"] +1,mapa)
        if(action == constanteMapa.MOV_LEFT):
            return self.spaceIsEmpty(estado["x"]-1,estado["y"],mapa)
        if(action == constanteMapa.MOV_UP):
            return self.spaceIsEmpty(estado["x"],estado["y"] - 1,mapa)
        if(action == constanteMapa.MOV_RIGHT):
            return self.spaceIsEmpty(estado["x"] + 1,estado["y"],mapa)
    def nextAction(self, action, ACTIONS):
        return (action + 1)%len(ACTIONS)
    # @estado: {string}
    def bestRandomAction(self, ACTIONS, estado, mapa):
        action = random.randrange(0, len(ACTIONS), 1)
        countAction = 1
        while(not(self.validaMovimento(ACTIONS[action], json.loads(estado), mapa))  and countAction!=4):
            countAction += 1
            if estado in self.Q_A:
                self.Q_A[estado][ACTIONS[action]] = -9991
            else:
                self.Q_A[estado] = {ACTIONS[action]: -999}
                
            action = self.nextAction(action, ACTIONS )
        if(countAction==4):
            print('nenhuma ação disponivel')
        return action
    def movimentaAgente(self, estado, mapa):
        self.qtdPassos += 1
        if(self.isLoadSteps):
            if(self.qtdPassos-1 < len(self.stepsHistory) - 3):
                return self.stepsHistory[self.qtdPassos-1]
            else:
                print('não mais carrega passos')
                self.stepsHistory = self.stepsHistory.tolist()
                self.isLoadSteps = False
            
        if(random.random() < self.EPSILON):
            # print('escolheu randomico')
            self.notUseRandomAction = False
            action = self.bestRandomAction(ACTIONS, estado, mapa)
            # action = random.randrange(0, len(ACTIONS), 1)
            # countAction = 1
            # while(not(self.validaMovimento(ACTIONS[action], json.loads(estado), mapa))  and countAction!=4):
            #     countAction += 1
            #     action = self.nextAction(action, ACTIONS )
            # if(countAction==4):
            #     print('nenhuma ação disponivel')
        elif (estado in self.POLITICA):
            # print('tem estado')
            action = self.POLITICA[estado]
            if(V_S_INICIAL > self.Q_A[estado][action] and len(self.Q_A[estado]) != len(ACTIONS) ):
                # print('Nao     escolheu maior valor')
                self.notUseRandomAction = False
                action = self.bestRandomAction(ACTIONS, estado, mapa)
                # action = random.randrange(0, len(ACTIONS), 1)
            else:
                # print('escolheu maior valor')
                self.stepsHistory.append(action)
                return action
        else:
            # print('nao tem estado')
            self.notUseRandomAction = False
            action = self.bestRandomAction(ACTIONS, estado, mapa)
            # action = random.randrange(0, len(ACTIONS), 1)
        self.stepsHistory.append(ACTIONS[action])
        return ACTIONS[action]