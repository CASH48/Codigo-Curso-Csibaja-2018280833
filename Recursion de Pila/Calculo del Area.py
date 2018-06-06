import math
def CalcularArea () :
    area = 0
    valor = input("ingrese el valor del radio: ")
    radio = int(valor)
    if radio > 0:
        area = (radio ** 2) * math.pi
        print ("El valor del area es: ", area)
    else:
        print ("el valor del radio no es mayor a cero.")
        
