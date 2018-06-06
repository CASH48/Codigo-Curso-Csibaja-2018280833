def contiene_cero(lista):
    if isinstance (lista, list):
        return contiene_cero_aux(lista)
    else: return "Error"

def contiene_cero_aux(lista):
    if lista == []:
        return False
    elif lista[0] == 0:
        return True
    else:
        return contiene_cero (lista[1:])
