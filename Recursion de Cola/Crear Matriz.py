def crearMatriz (num):
    if isinstance (num,int) and (num > 0):
        return crearMatriz_aux (num, [], [], 0, 0)
    else:
        return "Error"

def crearMatriz_aux (num, matriz, fila, indiceFila, indiceColumna):
    if indiceFila == num:
        return matriz
    elif indiceColumna == num:
        return crearMatriz_aux (num, matriz + [fila], fila + [], indiceFila + 1, 0)
    elif indiceFila == 0 or indiceFila == (num-1):
        return crearMatriz_aux (num, matriz, fila + ["*"], indiceFila, indiceColumna +1)
    elif indiceColumna == 0 or indiceColumna == (num-1):
        return crearMatriz_aux (num, matriz, fila + ["*"], indiceFila, indiceColumna +1)
    else:
        return crearMatriz_aux (num, matriz, fila + [0], indiceFila, indiceColumna+1)
