import numpy as np
import matplotlib.pyplot as plt

def cercle(x0,y0,r):
    plt.xticks(np.linspace(0,20,5))#afficher les valeurs de x uniquement entre 0 et 20 
    plt.yticks(np.linspace(0,20,9))#pareille pour y 
    plt.axis("equal")#ajuster les dimensions des traits d'unité du plan
    theta = np.linspace(0,2*np.pi)
    x = r * np.cos(theta) + x0
    y = r * np.sin(theta) + y0     
    plt.plot(x,y)


def ex1():
    for i in range(9):
        cercle(10,10,1 + i)
    plt.show() 
    
def ex2():
    for i in range(10):
        for j in range(10-i):
            cercle(i+2*j,2*i,1)
    plt.show() 

def main() :
    ex1()
    
  
    
    


main() 
