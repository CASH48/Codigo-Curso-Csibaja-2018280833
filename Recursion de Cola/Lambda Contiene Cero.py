def contieneCero(lista):
    if isinstance (lista, list):
        contieneCero = lambda x: x == 0
        return aux(lista, contieneCero)
    else: return "Error"
           
def aux (lista, condicion):
    if lista == []:
        return False
    elif condicion (lista[0]):
        return True
    else: return aux (lista[1:], condicion)
    
