import constanteMapa
class Inimigo:
    def __init__(self, nome,x,y,depth,sentido = 0):
        self.id = nome
        self.x = x
        self.y = y
        self.XMin = x - depth
        self.YMin = y - depth
        self.XMax = x + depth
        self.YMax = y + depth
        self.sentido = sentido

    
    def step(self,mapa):
        mapa[self.x][self.y] = 2
        if(self.id == 'v'):
            if(self.sentido == 0):
                if(self.YMax == self.y or mapa[self.x][self.y + 1] <= constanteMapa.PAREDE ):
                    # print('mudou e sub')
                    self.sentido = 1
                    if(self.y - 1 > self.YMin):
                        self.y -= 1    
                else:
                    # print('add')
                    self.y += 1    
            else:
                if(self.YMin == self.y or mapa[self.x][self.y - 1] <= constanteMapa.PAREDE):
                    # print('mudou e add')
                    self.sentido = 0
                    if(self.y + 1 < self.YMax):
                        self.y += 1    
                else:
                    # print('sub')
                    self.y -= 1
            if(self.sentido == 0 ):
                mapa[self.x][self.y] = constanteMapa.INIMIGOV
            else:
                mapa[self.x][self.y] = constanteMapa.INIMIGOVV
        if(self.id == 'h'):
            if(self.sentido == 0):
                if(self.XMax == self.x or mapa[self.x + 1][self.y] <= constanteMapa.PAREDE):
                    # print('mudou e sub')
                    self.sentido = 1
                    if(self.x - 1 > self.XMin):
                        self.x -= 1    
                else:
                    # print('add')
                    self.x += 1    
            else:
                if(self.XMin == self.x or  mapa[self.x -1][self.y] <= constanteMapa.PAREDE):
                    # print('mudou e add')
                    self.sentido = 0
                    if(self.x + 1 < self.XMax):
                        self.x += 1    
                else:
                    # print('sub')
                    self.x -= 1    
            
            if(self.sentido == 0 ):
                mapa[self.x][self.y] = constanteMapa.INIMIGOH
            else:
                mapa[self.x][self.y] = constanteMapa.INIMIGOHH
        if(self.id == 'd1'):
            if(self.sentido == 0):
                if(self.XMax == self.x or mapa[self.x + 1][self.y + 1] <= constanteMapa.PAREDE):
                    # print('mudou e sub')
                    self.sentido = 1
                    if(self.x - 1 > self.XMin and self.y - 1 > self.YMin):
                        self.x -= 1    
                        self.y -= 1
                else:
                    # print('add')
                    self.x += 1
                    self.y += 1    
            else:
                if(self.XMin == self.x or  mapa[self.x -1][self.y-1] <= constanteMapa.PAREDE):
                    # print('mudou e add')
                    self.sentido = 0
                    if(self.x + 1 < self.XMax and self.y + 1 < self.YMax):
                        self.x += 1
                        self.y += 1    
                else:
                    # print('sub')
                    self.x -= 1    
                    self.y -= 1
            
            if(self.sentido == 0 ):
                mapa[self.x][self.y] = constanteMapa.INIMIGOD1
            else:
                mapa[self.x][self.y] = constanteMapa.INIMIGOD11
        if(self.id == 'd2'):
            if(self.sentido == 0):
                if(self.XMin == self.x or mapa[self.x - 1][self.y + 1] <= constanteMapa.PAREDE):
                    # print('mudou e sub')
                    self.sentido = 1
                    if(self.x + 1 < self.XMax and self.y - 1 > self.YMin and mapa[self.x + 1][self.y-1] > constanteMapa.PAREDE):
                        self.x += 1    
                        self.y -= 1
                else:
                    # print('add')
                    self.x -= 1
                    self.y += 1    
            else:
                if(self.XMax == self.x or  mapa[self.x +1][self.y-1] <= constanteMapa.PAREDE):
                    # print('mudou e add')
                    self.sentido = 0
                    if(self.x - 1 > self.XMin and self.y + 1 < self.YMax and mapa[self.x - 1][self.y+1] > constanteMapa.PAREDE):
                        self.x -= 1
                        self.y += 1    
                else:
                    # print('sub')
                    self.x += 1    
                    self.y -= 1
            
            if(self.sentido == 0 ):
                mapa[self.x][self.y] = constanteMapa.INIMIGOD1
            else:
                mapa[self.x][self.y] = constanteMapa.INIMIGOD11
            

                
                
        