def paresimpares(num):
    if isinstance(num, int):
        pares = lambda x : x % 2 == 0
        impares = lambda x : x % 2 == 1
        return aux(num, pares), aux (num, impares)
    else: return "Error"
 
def aux (num, condicion):
    if num == 0:
        return 0
    elif condicion (num % 10):
        return 1 + aux(num//10, condicion)
    else: return aux (num//10, condicion)
