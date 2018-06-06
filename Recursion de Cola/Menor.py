def menor(lista):
    if isinstance (lista, list):
        return menor_aux(lista, 1, lista[0])
    else:
        return "Error"


def menor_aux(lista, indice, menor):
    if indice == len(lista):
        return menor
    elif lista[indice] <= menor:
        return menor_aux(lista, indice + 1, lista[indice])
    else:
        return menor_aux(lista, indice + 1, menor)
