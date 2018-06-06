def matriz:
    def __init__(self):
        pass

def crearMatriz (self,num):
    if isinstance (num,int) and (num > 0):
        return self.crearMatriz_aux (num, [], [], 0, 0)
    else:
        return "Error"

def crearMatriz_aux (self, num, matriz, fila, indiceFila, indiceColumna):
    if indiceFila == num:
        return matriz
    elif indiceColumna == num:
        return self.crearMatriz_aux (num, matriz + [fila], fila + [], indiceFila + 1, 0)
    elif indiceFila == 0 or indiceFila == (num-1):
        return self.crearMatriz_aux (num, matriz, fila + ["*"], indiceFila, indiceColumna +1)
    elif indiceColumna == 0 or indiceColumna == (num-1):
        return self.crearMatriz_aux (num, matriz, fila + ["*"], indiceFila, indiceColumna +1)
    else:
        return self.crearMatriz_aux (num, matriz, fila + [0], indiceFila + 1, indiceColumna)
