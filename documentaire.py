class Docummentaire () :
    _count = 0
    def __init__(self,T,DS) :
        self._T = T
        self._DS = DS
        Docummentaire._count = Docummentaire._count + 1

#getters
    #def getC (self) :
        #return self._C
    def getT (self) :
        return self._T
    def getDS (self) :
        return self._DS
    
#setters
   # def setC (self,C) :
        #self._C = C
    def setT (self,T) :
        self._T = T
    def setDS (self,DS) :
        self._DS = DS

#method
    def Tostring (self) :
       # print(f"le code :{(self.getC())}")
        print(f"le titre :{(self.getT())}")
        print(f"la date de sortie :{(self.getDS())}")
        print(f"le code est :{Docummentaire._count}")

    #def Equals (self,D1):
        #if (self.getC()==D1.getC()):
            #return True
        #else :
            #return False


#the child class
class Exemplaire (Docummentaire):
    def __init__(self,T,DS,N,DA):
        super(). __init__(T,DS)
        self.__N = N
        self.__DA = DA

#getters
    def getN (self):
        return self.__N 
    def getDA (self):
        return self.__DA
#setters
    def setN (self,N):
        self.__N =N
    def setDA (self,DA):
        self.__DA =DA

    def Tostring (self) :
        super().Tostring()
        print (f"le numero :{(self.getN())}")
        print (f"Date d'achat :{(self.getDA())}")





#main programme
A1= Docummentaire ("wissal","12,2004")
A1 .Tostring()

V2 = Exemplaire ("wissal","12.133","4","5")
V2 .Tostring()
