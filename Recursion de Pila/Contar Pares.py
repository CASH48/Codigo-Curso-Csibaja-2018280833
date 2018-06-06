def par_impar (num):
    if isinstance (num, int) and (num > 0):
        return par_aux (num), impar_aux (num)
    else:
        return "Error"

def impar_aux (num) :
    if (num == 0) :  # Condicion de parada
        return 0
    else:
        if ((num % 10) % 2 == 1):
            return 1 + impar_aux (num // 10)
        else:
            return impar_aux (num // 10)
    
def par_aux (num) :
    if (num == 0) :  # Condicion de parada
        return 0
    else:
        if ((num % 10) % 2 == 0):
            return 1 + par_aux (num // 10)
        else:
            return par_aux (num // 10)  
