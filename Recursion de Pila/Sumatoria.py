def sumatoria(num):
    if isinstance (num, int) and (num > 0):
        return sumatoria_aux(num)
    else:
        return "Error"

def sumatoria_aux(num):
    if (num == 0):
        return 0
    else:
        return num + sumatoria_aux(num - 1)
    
