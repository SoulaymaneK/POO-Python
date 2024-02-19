import matplotlib.pyplot as plt 
from scipy.interpolate import make_interp_spline
from numpy import cos,array,linspace  
from os import path
from pandas import DataFrame,read_csv

def x_cos():
    list_x = [i for i in range(-5,6)]
    list_cos = [cos(i) for i in range(-5,6)]
    return list_x, list_cos


def ecrire() :
    a,b = x_cos()
    for i in range(-5,6):
        file = DataFrame({"x": a, "cos(x)":b},index = None,columns = ["x","cos(x)"])
    file.to_csv("math.csv")
    #sinon on peut retirer la colonne a et la mettre en index 

        
def lire():
    if path.isfile("math.csv") :
        file = read_csv("math.csv")
        a = array(file[file.columns[1]])
        b = array(file[file.columns[2]])
        courbe = make_interp_spline(a, b)
        
        x = linspace(a[0],a[len(a)-1],100)
        y = courbe(x)
        plt.plot(x,y)
       
        plt.xticks(linspace(-4,4,5))
        plt.yticks(linspace(-1,1,9))
        plt.title("cos(x) sur [-5;5]")
        plt.xlabel("x")
        plt.ylabel("cos(x)")
        
        plt.show() 
    else : 
        raise FileNotFoundError("Le fichier n'a pas été trouvé!")
    


def main() :
    ecrire()
    lire() 

main()






        
        
    

        



    