def sumatoria_potencia(num):
    if isinstance (num, int) and (num > 0):
        return sumatoria_potencia_aux(num)
    else:
        return "Error"

def sumatoria_potencia_aux(num):
    if (num == 0):
        return 0
    else:
        return (num * num ** 3) + sumatoria_potencia_aux (num-1)
