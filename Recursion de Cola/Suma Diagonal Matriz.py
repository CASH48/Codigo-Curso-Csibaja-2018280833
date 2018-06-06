def diagonal (matriz):
    if isinstance (matriz,list) and (matriz != []) and len (matriz) == len (matriz[0]):
        return diagonal_aux (matriz, len (matriz),0,0)
    else:
        return "Error, el dato no es una matriz"

def diagonal_aux (matriz, filas, indice, resultado):
    if indice == filas:
        return resultado
    else:
        return (diagonal_aux(matriz, filas, indice + 1) , resultado + matriz[indice][indice]) 
