def traspuesta (matriz):
    if isinstance (matriz,list) and matriz != []:
        return transpuesta_aux (matriz, [], [], 0, 0)
    else:
        return "Error, el dato no es una matriz"

def traspuesta_aux (matriz, filaMatriz, resultado, fila, columna):
    if columna == len(matriz[0]):
        return resultado
    elif fila == len(matriz):
        return traspuesta_aux ( matriz,[], resultado + [filaMatriz], 0, columna+1)
    else:
        return traspuesta_aux ( matriz,filaMatriz + [matriz][fila][columna], resultado, fila+1, columna)



   
