import matplotlib.pyplot as plt
import numpy as np
import random
import Graham 
import Jarvis 
import QuickHull

lowerX=0
lowerY=0
upperX=20
upperY=20

def fillData(d,n):
    for i in range(n):
        datax=random.randint(lowerX+5,upperX-5)
        datay=random.randint(lowerY+5,upperY-5)
        d.append((datax,datay))

def plotGraphic(data,ch,name):

    datax=[x[0] for x in data]
    datay=[x[1] for x in data]
    dataxch=[x[0] for x in ch]
    dataych=[x[1] for x in ch]

    plt.plot(dataxch,dataych,'g.-',markersize=5)
    plt.plot(datax,datay,'b.',markersize=5)
    plt.axis([lowerX,upperX,lowerY,upperY])

    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.title('First Simple Plot - '+name)
    plt.show()


if __name__ == "__main__":
    data=[]
    fillData(data,10)
    #data=sorted(data,key=lambda k:k[::-1])
    plotGraphic(data,Graham.run(data,upperX,upperY),'Graham')
    plotGraphic(data,Jarvis.run(data),'Jarvis')
    plotGraphic(data,QuickHull.run(data),'Quick Hull')