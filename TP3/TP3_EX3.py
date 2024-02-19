from math import sqrt 

class Point : 
    def __init__(self,abs,ord):
        self.abs = abs 
        self.ord = ord 
        
    @property 
    def abs(self):
        return self.__abs 
    
    @abs.setter 
    def abs(self,abs):
        if not (isinstance(abs, float) or isinstance(abs,int)):
            raise TypeError ("L'abscisse doit être de type float")
        self.__abs = abs 
        
    @property 
    def ord(self):
        return self.__ord
    
    @ord.setter 
    def ord(self,ord):
        if not (isinstance(ord, float) or isinstance(ord,int)):
            raise TypeError ("L'abscisse doit être de type float")
        self.__ord = ord
    
    def calculeDistance(self,p):
        return sqrt((p.abs - self.abs)**2 + (p.ord - self.ord)**2)
    
    def calculeMilieu(self,p):
        return Point( (self.abs + p.abs) / 2 , (self.ord + p.ord) / 2)

    #en plus
    def __str__(self):
        return f"abscisse : {self.abs} , ordonnee : {self.ord}"
    
    
class TroisPoints:
    def __init__(self, p1 , p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @property 
    def p1(self):
        return self.__p1
    
    @p1.setter 
    def p1(self,p1):
        if not isinstance(p1, Point):
            raise TypeError ("Le point p1 doit être de type Point")
        self.__p1 = p1
        
    @property 
    def p2(self):
        return self.__p2
    
    @p2.setter 
    def p2(self,p2):
        if not isinstance(p2, Point):
            raise TypeError ("Le point p1 doit être de type Point")
        self.__p2 = p2
    
    @property 
    def p3(self):
        return self.__p3
    
    @p3.setter 
    def p3(self,p3):
        if not isinstance(p3, Point):
            raise TypeError ("Le point p1 doit être de type Point")
        self.__p3 = p3
    
    def sontAligne(self):
        p1p2 = self.p1.calculeDistance(self.p2)
        p2p3 = self.p2.calculeDistance(self.p3)
        p1p3 = self.p1.calculeDistance(self.p3)
        if (p1p2 == p2p3 + p1p3) or (p2p3 == p1p2 + p1p3) or (p1p3 == p1p2 + p2p3):
            return True 
        else :
            return False 
    
    def estIsocele(self):
        p1p2 = self.p1.calculeDistance(self.p2)
        p2p3 = self.p2.calculeDistance(self.p3)
        p1p3 = self.p1.calculeDistance(self.p3)
        if p1p2 == p2p3 or p1p2 == p1p3 or p2p3 == p1p3 :
            return True
        else :
            return False 
        
     
p1 = Point(0,0)
p2 = Point(2,0)
p3 = Point(1,2)

p = TroisPoints(p1, p2, p3)
print(p.sontAligne())
print(p.estIsocele())



        
        
        
    
        
