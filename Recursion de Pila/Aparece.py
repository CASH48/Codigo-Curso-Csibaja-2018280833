# Dado un numero, encontrar cuantas veces aparece un digito en ese numero

def aparece (num, digito):
    if (isinstance (num, int) and isinstance (digito, int) and digito >= 0 and digito <=9 and (num > 0):
        return aparece_aux (num, digito)
    else:
        return "Error"

def aparece_aux (num, digito) :
    if (num == 0) :
        return 0
    else:
        if num % 10 == digito:
            return 1  + aparece_aux (num // 10)
        else:
            return aparece_aux (num // 10)
            
        
