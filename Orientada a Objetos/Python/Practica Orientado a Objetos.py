import math

class fig:
    def __init__ (self,x,y):
        self. __x = x
        self. __y = y
    def getX (self):
        return self. __x
    def setX (self,x):
        if x >= 0 and x <= 1023:
            self .__x = x
        else: print  ("El valor de x debe ser mayor o igual a 0 y menor a 1024.")

    def getY (self):
        return self.__y
    def setY (self,y):
        if y >= 0 and y <= 768:
            self.__y = y
        else: print ("El valor de y debe ser mayor o igual 0 y menor a 768.")


    class Circulo (Fig):
        def __init__ (self, x, y, r):
            super (). __init__ (x, y)
            self. __ radio = r
        def getRadio (self):
            return self.__ radio
        def setRadio (self, r):
            self.__radio = r
            
        def calcularArea (self):
            return math.pi * (self.__radio ** 2)

        class Rectangulo (Fig):
            def __init__ (self , x, y, alto, ancho):
                super (). __init__ (x,y)
                self.__alto = alto
                self.__ancho = ancho
            def getAlto (self):
                return self.__ alto
            def setAlto (self, alto):
                self.__alto = alto
            def getAncho (self):
                return self.__ ancho
            def setAncho (self, alto):
                self.__ancho = ancho
                
            def calcularArea (self):
                return self.__alto * self.__ancho

                
        class 
        
