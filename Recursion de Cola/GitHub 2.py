def traspuesta (matriz):
    if isinstance (matriz,list) and matriz != []:
        return traspuesta_aux (matriz, len(matriz), len (matriz[0]), 0, 0,0)
    else:
        return "Error, el dato no es una matriz"

def transpuesta (matriz1,matriz2,num_filas,num_columnas,fila,columna):
    if fila == num_filas:
        return
    elif traspuesta
