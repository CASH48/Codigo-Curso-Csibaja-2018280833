def busqueda_lineal (num,lista):
    if isinstance (num,int) and (lista, list):
        return busqueda_lineal_aux (num,lista,0)
    else:
        return "error"


def busqueda_lineal_aux (num,lista,indice):
    if indice == len (lista):
        return False
    elif num == lista [indice]:
        return True
    else: return busqueda_lineal_aux (num,lista,indice+1)
    
