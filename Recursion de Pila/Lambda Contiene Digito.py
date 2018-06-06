def contieneDigito(lista, digito):
    if isinstance (lista, list) and isinstance(digito, int):
        contieneDigito = lambda x: x == digito
        return aux(lista, contieneDigito)
    else: return "Error"
           
def aux (lista, condicion):
    if lista == []:
        return 0
    elif condicion (lista[0]):
        return 1 + aux (lista [1:], condicion)
    else: return aux (lista[1:], condicion)
    
