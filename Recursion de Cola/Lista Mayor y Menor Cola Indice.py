def mayorYmenor (lista):
    if isinstance (lista,list) and lista != []:
        return mayor_aux (lista, 0, lista [0]) , menor_aux (lista, 0, lista [0])
    else:
        return "Error"

def mayor_aux (lista,indice,resultado):
    if indice == len(lista) - 1:
        return resultado
    elif (lista [indice + 1]) < resultado:
        return mayor_aux (lista, indice + 1, resultado)
    else:
        return mayor_aux (lista, indice + 1, lista [indice + 1])


def menor_aux (lista,indice,resultado):
    if indice == len(lista) - 1 :
        return resultado
    elif (lista [indice + 1]) > resultado:
        return menor_aux (lista, indice + 1, resultado)
    else:
        return menor_aux (lista, indice + 1, lista [indice + 1])
