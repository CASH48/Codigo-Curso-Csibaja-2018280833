def busqueda_binaria (num,lista):
    if isinstance (num,int) and (lista,list):
        return busqueda_binaria_aux (num,lista)
    else:
        return "error"

def busqueda_binaria_aux (num,lista,medio):
    if lista == []:
        return False
    elif lista [medio] == num:
        return True
    elif lista [medio] < num:2
        return (busqueda_binaria_aux (num, lista [medio + 1):], (len(lista [(medio + 1):]
                                                                      )-1 // 2))
    else:
        return (busqueda_binaria_aux (num, lista [medio):], (len(lista [(medio):]
                                                                      )-1 // 2))
