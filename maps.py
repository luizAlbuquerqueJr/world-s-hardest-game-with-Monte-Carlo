from inimigo import Inimigo
import constanteMapa
import random
import numpy as np
import copy

def setMap0(_):
    return
def setMap1():
    enemy = []
    enemy.append(Inimigo('v',6,25,50,0))
    enemy.append(Inimigo('v',8,25,50,0))
    enemy.append(Inimigo('v',10,25,50,0))
    enemy.append(Inimigo('v',12,25,50,0))
    enemy.append(Inimigo('v',14,25,50,0))
    enemy.append(Inimigo('v',16,25,50,0))
    enemy.append(Inimigo('v',18,25,50,0))
    enemy.append(Inimigo('v',20,25,50,0))
    enemy.append(Inimigo('v',22,25,50,0))
    enemy.append(Inimigo('v',24,25,50,0))
    enemy.append(Inimigo('v',26,25,50,0))
    enemy.append(Inimigo('v',28,25,50,0))
    enemy.append(Inimigo('v',30,25,50,0))
    enemy.append(Inimigo('v',32,25,50,0))
    enemy.append(Inimigo('v',34,25,50,0))
    enemy.append(Inimigo('v',36,25,50,0))
    enemy.append(Inimigo('v',38,25,50,0))
    enemy.append(Inimigo('v',40,25,50,0))
    enemy.append(Inimigo('v',42,25,50,0))
    return enemy

def setMap2():
    enemy = []
    enemy.append(Inimigo('v',6,25,50,0))
    enemy.append(Inimigo('v',8,25,50,0))
    enemy.append(Inimigo('v',10,25,50,0))
    enemy.append(Inimigo('v',12,25,50,0))
    enemy.append(Inimigo('v',14,25,50,0))
    enemy.append(Inimigo('v',16,25,50,0))
    enemy.append(Inimigo('v',18,25,50,0))
    enemy.append(Inimigo('v',20,25,50,0))
    enemy.append(Inimigo('v',22,25,50,0))
    enemy.append(Inimigo('v',24,25,50,0))
    enemy.append(Inimigo('v',26,25,50,0))
    enemy.append(Inimigo('v',28,25,50,0))
    enemy.append(Inimigo('v',30,25,50,0))
    enemy.append(Inimigo('v',32,25,50,0))
    enemy.append(Inimigo('v',34,25,50,0))
    enemy.append(Inimigo('v',36,25,50,0))
    enemy.append(Inimigo('v',38,25,50,0))
    enemy.append(Inimigo('v',40,25,50,0))
    enemy.append(Inimigo('v',42,25,50,0))

    enemy.append(Inimigo('v',6,20,50,0))
    enemy.append(Inimigo('v',8,20,50,0))
    enemy.append(Inimigo('v',10,20,50,0))
    enemy.append(Inimigo('v',12,20,50,0))
    enemy.append(Inimigo('v',14,20,50,0))
    enemy.append(Inimigo('v',16,20,50,0))
    enemy.append(Inimigo('v',18,20,50,0))
    enemy.append(Inimigo('v',20,20,50,0))
    enemy.append(Inimigo('v',22,20,50,0))
    enemy.append(Inimigo('v',24,20,50,0))
    enemy.append(Inimigo('v',26,20,50,0))
    enemy.append(Inimigo('v',28,20,50,0))
    enemy.append(Inimigo('v',30,20,50,0))
    enemy.append(Inimigo('v',32,20,50,0))
    enemy.append(Inimigo('v',34,20,50,0))
    enemy.append(Inimigo('v',36,20,50,0))
    enemy.append(Inimigo('v',38,20,50,0))
    enemy.append(Inimigo('v',40,20,50,0))
    enemy.append(Inimigo('v',42,20,50,0))

    enemy.append(Inimigo('v',6,20,50,1))
    enemy.append(Inimigo('v',8,20,50,1))
    enemy.append(Inimigo('v',10,20,50,1))
    enemy.append(Inimigo('v',12,20,50,1))
    enemy.append(Inimigo('v',14,20,50,1))
    enemy.append(Inimigo('v',16,20,50,1))
    enemy.append(Inimigo('v',18,20,50,1))
    enemy.append(Inimigo('v',20,20,50,1))
    enemy.append(Inimigo('v',22,20,50,1))
    enemy.append(Inimigo('v',24,20,50,1))
    enemy.append(Inimigo('v',26,20,50,1))
    enemy.append(Inimigo('v',28,20,50,1))
    enemy.append(Inimigo('v',30,20,50,1))
    enemy.append(Inimigo('v',32,20,50,1))
    enemy.append(Inimigo('v',34,20,50,1))
    enemy.append(Inimigo('v',36,20,50,1))
    enemy.append(Inimigo('v',38,20,50,1))
    enemy.append(Inimigo('v',40,20,50,1))
    enemy.append(Inimigo('v',42,20,50,1))

    enemy.append(Inimigo('v',6,15,50,1))
    enemy.append(Inimigo('v',8,15,50,1))
    enemy.append(Inimigo('v',10,15,50,1))
    enemy.append(Inimigo('v',12,15,50,1))
    enemy.append(Inimigo('v',14,15,50,1))
    enemy.append(Inimigo('v',16,15,50,1))
    enemy.append(Inimigo('v',18,15,50,1))
    enemy.append(Inimigo('v',20,15,50,1))
    enemy.append(Inimigo('v',22,15,50,1))
    enemy.append(Inimigo('v',24,15,50,1))
    enemy.append(Inimigo('v',26,15,50,1))
    enemy.append(Inimigo('v',28,15,50,1))
    enemy.append(Inimigo('v',30,15,50,1))
    enemy.append(Inimigo('v',32,15,50,1))
    enemy.append(Inimigo('v',34,15,50,1))
    enemy.append(Inimigo('v',36,15,50,1))
    enemy.append(Inimigo('v',38,15,50,1))
    enemy.append(Inimigo('v',40,15,50,1))
    enemy.append(Inimigo('v',42,15,50,1))

    enemy.append(Inimigo('v',6,30,50,1))
    enemy.append(Inimigo('v',8,30,50,1))
    enemy.append(Inimigo('v',10,30,50,1))
    enemy.append(Inimigo('v',12,30,50,1))
    enemy.append(Inimigo('v',14,30,50,1))
    enemy.append(Inimigo('v',16,30,50,1))
    enemy.append(Inimigo('v',18,30,50,1))
    enemy.append(Inimigo('v',20,30,50,1))
    enemy.append(Inimigo('v',22,30,50,1))
    enemy.append(Inimigo('v',24,30,50,1))
    enemy.append(Inimigo('v',26,30,50,1))
    enemy.append(Inimigo('v',28,30,50,1))
    enemy.append(Inimigo('v',30,30,50,1))
    enemy.append(Inimigo('v',32,30,50,1))
    enemy.append(Inimigo('v',34,30,50,1))
    enemy.append(Inimigo('v',36,30,50,1))
    enemy.append(Inimigo('v',38,30,50,1))
    enemy.append(Inimigo('v',40,30,50,1))
    enemy.append(Inimigo('v',42,30,50,1))

    

    enemy.append(Inimigo('v',20,25,50,1))
    enemy.append(Inimigo('v',21,25,50,1))
    enemy.append(Inimigo('v',22,25,50,1))
    enemy.append(Inimigo('v',23,25,50,1))
    enemy.append(Inimigo('v',24,25,50,1))
    enemy.append(Inimigo('v',25,25,50,1))
    enemy.append(Inimigo('v',26,25,50,1))
    enemy.append(Inimigo('v',27,25,50,1))
    return enemy
    
def setMap3():
    enemy = []
    qtd_enemy = random.randrange(2, 15, 1)
    backupInimigo = []
    for i in range(qtd_enemy):
        x = random.randrange(constanteMapa.xMinMap, constanteMapa.xMaxMap + 1, 2)
        y = random.randrange(constanteMapa.yMinMap, constanteMapa.yMaxMap + 1, 2)
        depth = random.randrange(0, 50, 1)
        sentido = random.randrange(0, 2, 1)
        index = random.randrange(0, 4, 1) 
        tipos = ['v','h','d1','d2']
        enemy.append(Inimigo(tipos[index],x,y,depth,sentido))
        backupInimigo.append({'x':x,'y':y,'depth':depth, 'sentido':sentido, 'tipo': tipos[index] })
    return enemy


def setMap4(enemy):
    path = './MC_SAVED/map4/data_100.npy'
    qtd_enemy = 100
    backupInimigo = []
    for i in range(qtd_enemy):
        x = random.randrange(constanteMapa.xMinMap, constanteMapa.xMaxMap + 1, 2)
        y = random.randrange(constanteMapa.yMinMap, constanteMapa.yMaxMap + 1, 2)
        depth = random.randrange(0, 50, 1)
        sentido = random.randrange(0, 2, 1)
        index = random.randrange(0, 4, 1) 
        tipos = ['v','h','d1','d2']
        enemy.append(Inimigo(tipos[index],x,y,depth,sentido))
        backupInimigo.append({'x':x,'y':y,'depth':depth, 'sentido':sentido, 'tipo': tipos[index] })
    np.save(path, backupInimigo,  allow_pickle=True) # save
def setMap5(enemy):
    path = './MC_SAVED/map5/data_200.npy'
    qtd_enemy = 200
    backupInimigo = []
    for i in range(qtd_enemy):
        x = random.randrange(constanteMapa.xMinMap, constanteMapa.xMaxMap + 1, 2)
        y = random.randrange(constanteMapa.yMinMap, constanteMapa.yMaxMap + 1, 2)
        depth = random.randrange(0, 50, 1)
        sentido = random.randrange(0, 2, 1)
        index = random.randrange(0, 4, 1) 
        tipos = ['v','h','d1','d2']
        enemy.append(Inimigo(tipos[index],x,y,depth,sentido))
        backupInimigo.append({'x':x,'y':y,'depth':depth, 'sentido':sentido, 'tipo': tipos[index] })
    np.save(path, backupInimigo,  allow_pickle=True) # save
def setMap6(enemy):
    path = './MC_SAVED/map6/data_300.npy'
    qtd_enemy = 300
    backupInimigo = []
    for i in range(qtd_enemy):
        x = random.randrange(constanteMapa.xMinMap, constanteMapa.xMaxMap + 1, 2)
        y = random.randrange(constanteMapa.yMinMap, constanteMapa.yMaxMap + 1, 2)
        depth = random.randrange(0, 50, 1)
        sentido = random.randrange(0, 2, 1)
        index = random.randrange(0, 4, 1) 
        tipos = ['v','h','d1','d2']
        enemy.append(Inimigo(tipos[index],x,y,depth,sentido))
        backupInimigo.append({'x':x,'y':y,'depth':depth, 'sentido':sentido, 'tipo': tipos[index] })
    np.save(path, backupInimigo,  allow_pickle=True) # save

class Mapa():
    def __init__(self):
        self.mapa4 = {}
        self.haveMap4 = False
        self.mapa5 = {}
        self.haveMap5 = False
        self.mapa6 = {}
        self.haveMap6 = False
        
    def loadMap4(self):
        if not(self.haveMap4):   
            self.haveMap4 = True         
            enemy =[]
            path = './MC_SAVED/map4/data_100.npy'
            #load
            new_num_arr = np.load(path,  allow_pickle=True) # load
            print(new_num_arr)
            for inimigo in new_num_arr:
                enemy.append(Inimigo(inimigo['tipo'],inimigo['x'],inimigo['y'],inimigo['depth'],inimigo['sentido']))
            self.mapa4 = enemy
            return self.mapa4
        else:
            print("atalho")
            return self.mapa4
    def loadMap5(self):
        if not(self.haveMap5):   
            self.haveMap5 = True         
            enemy =[]
            path = './MC_SAVED/map5/data_200.npy'
            #load
            new_num_arr = np.load(path,  allow_pickle=True) # load
            print(new_num_arr)
            for inimigo in new_num_arr:
                enemy.append(Inimigo(inimigo['tipo'],inimigo['x'],inimigo['y'],inimigo['depth'],inimigo['sentido']))
            self.mapa5 = enemy
            
            return copy.deepcopy(self.mapa5)
        else:
            # print("atalho")
            return copy.deepcopy(self.mapa5)
    def loadMap6(self):
        if not(self.haveMap6):   
            self.haveMap6 = True         
            enemy =[]
            # path = './MC_SAVED/map6/data_300.npy'
            path = './MC_SAVED/map6/data_300_parte_2.npy'
            #load
            new_num_arr = np.load(path,  allow_pickle=True) # load
            print(new_num_arr)
            for inimigo in new_num_arr:
                enemy.append(Inimigo(inimigo['tipo'],inimigo['x'],inimigo['y'],inimigo['depth'],inimigo['sentido']))
            self.mapa6 = enemy
            
            return copy.deepcopy(self.mapa6)
        else:
            return copy.deepcopy(self.mapa6)
      
def setMapTeste(enemy):
    enemy.append(Inimigo('v',constanteMapa.xMinMap,constanteMapa.yMaxMap,100,0))