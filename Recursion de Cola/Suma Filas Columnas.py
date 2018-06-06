def suma_filas (matriz):
    if isinstance (matriz,list) and (matriz != []):
        return
    else:
        return "Error, el dato no es una matriz"

def suma_filas_aux (matriz,indice1,indice2,resultado):
    if indice1 == len(matriz):
        return resultado
