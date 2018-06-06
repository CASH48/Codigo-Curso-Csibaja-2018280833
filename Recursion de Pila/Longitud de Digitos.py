# Dado un numero, determine su longitud (numero de digitos)
# Entrada: es un numero entero
# Restricciones: es un numero entero positivo mayor a cero
# Salida: longitud de un numero

def longitud_digitos (num):
    if isinstance (num, int) and (num > 0) :
        return longitud_digitos_aux (abs (num) )
    else:
        return "Error"

def longitud_digitos_aux (num) :
    if (num == 0) :
        return 0
    else:
         return 1 + longitud_digitos_aux (num // 10)
        
