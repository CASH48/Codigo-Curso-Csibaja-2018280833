def positivos(lista):
    if isinstance (lista, list) and lista != []:
        negativo = lambda x: x < 0
        return aux(lista, negativo)
    else: return "Error"
           
def aux (lista, condicion):
    if lista == []:
        return True
    elif condicion (lista[0]):
        return False
    else: return aux (lista[1:], condicion)
    
