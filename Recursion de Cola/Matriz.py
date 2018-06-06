def suma_matriz (num,matriz):
    if isinstance (matriz,list) and matriz != [] and isinstance (num,int):
        return matriz_aux (num, matriz, len(matriz), len (matriz[0]) , 0, 0)
    else:
        return "Error, el dato no es una matriz"

def matriz_aux (num, matriz, num_filas, num_columnas,fila,columna):
    if fila == num_filas:
        return matriz
    elif columna == num_columnas:
        return matriz_aux (num, matriz, num_filas, num_columnas, fila + 1, 0)
    else:
        return matriz_aux (num, matriz, num_filas, num_columnas, fila, columna + 1)
