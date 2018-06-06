def suma_promedio (matriz):
    if isinstance (matriz,list) and matriz != []:
        return suma_promedio_aux (matriz, len(matriz), len (matriz[0]), 0, 0,0)
    else:
        return "Error, el dato no es una matriz"

def suma_promedio_aux (matriz,num_filas,num_columnas,fila,columna, suma):
    if fila == num_filas:
        return suma // (num_filas * num_columnas)
    elif columna == num_columnas:
        return suma_promedio_aux (matriz, num_filas, num_columnas, fila + 1, 0, suma)
    else:
        return suma_promedio_aux (matriz, num_filas, num_columnas, fila, columna + 1, suma + matriz[fila][columna])

