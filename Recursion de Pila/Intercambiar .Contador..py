def intercambiar (num):
    if isinstance (num,int):
        return intercambiar_aux (num)
    else:
        return "Error"

def intercambiar_aux (num, pot):
    if num == 0:
        return 0
    else:
        return ((( num // 10) % 10) * (10 ** pot)) + ((num % 10)) * (10 ** (pot + 1)) + intercambio_aux ( num // 100, pot +2)
