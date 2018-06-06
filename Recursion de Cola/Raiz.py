import math

def raiz (lista):
    if isinstance (lista,list):
        return raiz_aux (lista, 0 ,0)
    else:
        return "Error"

def raiz_aux (lista,resultado,indice):
    if indice == len(lista):
        return resultado
    else:
        return raiz_aux ( lista, resultado + math.sqrt (lista[indice]), indice+1) 
    
    
