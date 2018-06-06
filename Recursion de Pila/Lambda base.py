def revise_num(num):
    if isinstance(num, int):
        entre0y4 = lambda digito : digito <= 4
        entre5y9 = lambda digito : digito >= 5
        return aux(num, entre0y4), aux (num, entre5y9)
    else: return "Error"
def entreCeroyCuatro (digito):
    return digito <= 
def entreCincoyNueve (digito):
    if digito >= 5:
        return True
    else: return False
def aux (num, condicion):
    if num == 0:
        return 0
    elif condicion (num % 10):
        return 1 + revise_aux(num//10, condicion)
    else: return revise_aux (num//10, condicion)
