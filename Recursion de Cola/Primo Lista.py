#Sacar los numeros primos de una lista dada y colocarlos en una lista nueva.

def evaluar (lista):
    if isinstance (lista, list):
        return primolista(lista)
    else:
        return "Error, el valor introducido no es una lista"

def primolista(lista):
    if lista == []:
        return []
    elif primo(lista[0] , lista[0] - 1) == True:
        return [lista[0]] + primolista(lista[1:])
    else: return primolista(lista[1:])

def primo (numero , contador):
    if numero == 1 or numero == 2 or numero == 3:
        return True
    if contador == 1:
        return True
    elif numero % contador == 0:
        return False
    else: return primo(numero , contador - 1)

    
