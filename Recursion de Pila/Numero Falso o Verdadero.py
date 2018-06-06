def numero_verdadero_falso (num) :
    if (num == 0) :  # Condicion de parada
        return True
    else:
        if ((num % 10) >= 0) and ((num % 10 ) <= 4):
            return numero_verdadero_falso (num // 10)
        else: 
                return False
            
