import numpy as np
import pygame, sys
import constanteMapa
class Player:
    #constantes do mapa
    # X_INITIAL = 1
    # Y_INITIAL = 13
    X_INITIAL = constanteMapa.xMinMap-1
    Y_INITIAL = constanteMapa.yMaxMap-1
    def __init__(self, x= X_INITIAL, y = Y_INITIAL):
        self.X_INITIAL = x
        self.y_INITIAL = y
        self.x = x
        self.y = y
        self.vida = 1
        self.fitness = 999
        self.sensor = {
            'U':0,
            'UCount':0,
            'L':0,
            'LCount':0,
            'R':0,
            'RCount':0,
            'D':0,
            'DCount':0,
            'UR':0,
            'URCount':0,
            'DR':0,
            'DRCount':0,
            'DL':0,
            'DLCount':0,
            'UL':0,
            'ULCount':0
        }
        # mapa[x][y] = self.PLAYER
    # def setMap(self,mapa):
    #     self.mapaPlayer = np.zeros((len(mapa),len(mapa)))
    def reset(self):
        self.x = self.X_INITIAL
        self.y = self.y_INITIAL
    def readSensor(self,DISPLAY,matrixMap,sensores):
        LIMTI_COUNT = 3
        count = 0
        # print(len(players),len(sensores))
        # for self, sensor, index  in zip(players,sensores,range(len(players))):
        # if(bestIndviduo!=-1):
        #     print('Atualizando sensor ',index,"   melhor ind sensor",bestIndviduo, sensores[bestIndviduo])
    
        count = 0
        while(self.x+count < 50 and matrixMap[self.x+count][self.y] != constanteMapa.PAREDE and matrixMap[self.x+count][self.y] < constanteMapa.INIMIGO):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), (self.x*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT), ((self.x+ count)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['R'] = matrixMap[self.x + count][self.y]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['RCount'] = count
        # if(bestIndviduo == index and bestIndviduo != -1):
        #     print("melhor ind sensor R",count)
        
        

        count = 0
        while(matrixMap[self.x-count][self.y] != constanteMapa.PAREDE and matrixMap[self.x-count][self.y] < constanteMapa.INIMIGO):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x-count)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['L'] = matrixMap[self.x-count][self.y]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['LCount'] = count
        
        
        count = 0
        while(matrixMap[self.x][self.y + count] != constanteMapa.PAREDE and matrixMap[self.x][self.y + count] < constanteMapa.INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x)*constanteMapa.SIZE_OBJECT, (self.y+count)*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['D'] = matrixMap[self.x][self.y+count]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self. sensor['DCount'] = count

        count = 0
        while(matrixMap[self.x][self.y - count] != constanteMapa.PAREDE and matrixMap[self.x][self.y - count] < constanteMapa.INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x)*constanteMapa.SIZE_OBJECT, (self.y-count)*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['U'] = matrixMap[self.x][self.y - count]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['UCount'] = count
        # if(index == 5):
            # print("UCount",sensor['UCount'])

        count = 0
        while(matrixMap[self.x - count][self.y + count] != constanteMapa.PAREDE and matrixMap[self.x-count][self.y + count] < constanteMapa.INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x-count)*constanteMapa.SIZE_OBJECT, (self.y+count)*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['DL'] = matrixMap[self.x-count][self.y + count]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['DLCount'] = count

        count = 0
        while(matrixMap[self.x + count][self.y + count] != constanteMapa.PAREDE and matrixMap[self.x+count][self.y + count] < constanteMapa.INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x+count)*constanteMapa.SIZE_OBJECT, (self.y+count)*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['DR'] = matrixMap[self.x+count][self.y + count]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['DRCount'] = count
        
        count = 0
        while(matrixMap[self.x + count][self.y - count] != constanteMapa.PAREDE and matrixMap[self.x+count][self.y - count] < constanteMapa.INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x + count)*constanteMapa.SIZE_OBJECT, (self.y-count)*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['UR'] = matrixMap[self.x+count][self.y - count]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['URCount'] = count

        count = 0
        while(matrixMap[self.x - count][self.y - count] != constanteMapa.PAREDE and matrixMap[self.x-count][self.y - count] < constanteMapa.INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((self.x - count)*constanteMapa.SIZE_OBJECT, (self.y-count)*constanteMapa.SIZE_OBJECT), ((self.x)*constanteMapa.SIZE_OBJECT, self.y*constanteMapa.SIZE_OBJECT))
        self.sensor['UL'] = matrixMap[self.x-count][self.y - count]
        if(count > LIMTI_COUNT): count = LIMTI_COUNT
        self.sensor['ULCount'] = count
        # print(self.sensor)
        pygame.display.update()
        return self.sensor
    
    def step(self,mapa,movimento):
        if movimento == 97 or movimento == 1073741904:
            movimento = constanteMapa.MOV_LEFT
        elif movimento == 100 or movimento == 1073741903:
            movimento = constanteMapa.MOV_RIGHT     
        elif movimento == 119 or movimento == 1073741906:
            movimento = constanteMapa.MOV_UP
        elif movimento == 115 or movimento == 1073741905:
            movimento = constanteMapa.MOV_DOWN
        
        if(movimento == constanteMapa.MOV_DOWN):
            if(mapa[self.x][self.y+1] == constanteMapa.PAREDE):
                self.vida = 0
                return False
            else:
                self.y += 1
                if(mapa[self.x][self.y] == constanteMapa.INIMIGOVV):
                    return False
        if(movimento == constanteMapa.MOV_RIGHT):
            if(mapa[self.x +1 ][self.y] == constanteMapa.PAREDE):
                self.vida = 0
                return False
            else:
                if(self.x != len(mapa[0])):
                   self.x += 1 
                if(mapa[self.x][self.y] == constanteMapa.INIMIGOHH):
                    return False
        if(movimento == constanteMapa.MOV_UP):
            if(mapa[self.x][self.y-1] == constanteMapa.PAREDE ): 
                self.vida = 0
                return False
            else:
                self.y -= 1
                if(mapa[self.x][self.y] == constanteMapa.INIMIGOV):
                    return False
        if(movimento == constanteMapa.MOV_LEFT):
            if(mapa[self.x -1 ][self.y] == constanteMapa.PAREDE):
                self.vida = 0
                return False
            else:
                if(self.x != 0):
                    self.x -= 1
                if(mapa[self.x][self.y] == constanteMapa.INIMIGOH):
                    return False
        
        
        return True
    