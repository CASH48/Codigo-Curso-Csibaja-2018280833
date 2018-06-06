def eliminar_lista(lista,num):
    if isinstance (lista, list) and isinstance(num,int):
        return (lista,num)
    else: return "Error"

def eliminar_lista_aux(lista,num):
    if lista == []:
        return []
    elif lista[0] == num:
        return eliminar_lista_aux(lista[1:],num)
    else:
        return [lista [0]] + eliminar_lista_aux(lista[1:],num)
    
