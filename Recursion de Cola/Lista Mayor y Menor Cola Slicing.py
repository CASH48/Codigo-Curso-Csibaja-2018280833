def mayorYmenor (lista):
    if isinstance (lista,list) and lista != []:
        return mayor_aux (lista, lista [0]) , menor_aux (lista, lista [0])
    else:
        return "Error"

def mayor_aux (lista,resultado):
    if lista == []:
        return resultado
    elif (lista [0]) < resultado:
        return mayor_aux (lista [1:], resultado)
    else:
        return mayor_aux (lista [1:], lista [0])


def menor_aux (lista,resultado):
    if lista == []:
        return resultado
    elif (lista [0]) > resultado:
        return menor_aux (lista [1:], resultado)
    else:
        return menor_aux (lista [1:], lista [0])
