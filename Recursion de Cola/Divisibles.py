def divisible (num):
    if isinstance (num,int):
        return divisible_aux(num,0)
    else:
        return "ERROR"

def divisible_aux(num, resultado, pot):
    if (num == 0):
        return resultado
    elif (num % 10) % 3 == 0: 
        return divisible_aux (num // 10, resultado,pot)
    else:
        return divisible_aux (num // 10, resultado + num % 10 * (10 ** pot)pot + 1)
    
