import numpy as np 
import matplotlib.pyplot as plt 


#manipulating the first Axes 
def plotarGraficoY(y,address):
    fig,ax=plt.subplots(figsize=(20,5)) 
    y = y
    x = [i for i in range(1,len(y)+1)] 
    ax.plot(x,y)
    ax.set_xlabel('N-ésima vez que chegou no objetivo') 
    ax.set_ylabel('Quantidade de Passos para chegar no objetivo') 
    ax.set_title('Número de passos até chegar no objetivo') 

    #save and display the plot 
    plt.savefig(address,dpi=300,bbox_inches='tight') 
