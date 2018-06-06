def mayores (num,lista):
    if isinstance (num,int) and (lista,list):
        return mayores_aux(num,lista,0,0)
    else:
        return "error"

def mayores_aux (num,lista,indice,resultado):
    if indice == len (lista)-1:
        return resultado
    elif lista [indice] > num:
        return mayores_aux (num,lista,indice + 1, resultado + 1)
    else:
        return mayores_aux (num,lista,indice + 1, resultado)
