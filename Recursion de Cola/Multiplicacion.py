def multiplicacion (lista):
    if isinstance (lista, list) and lista != []:
        return multiplicacion_aux (lista, 1)
    else:
        return "ERROR"

def multiplicacion_aux (lista, resultado):
    if lista == []:
        return resultado
    elif isinstance (lista[0], list):
        return multiplicacion_aux (lista[0], resultado)
    else:
        return multiplicacion_aux (lista[1:], resultado * lista[0])


    
