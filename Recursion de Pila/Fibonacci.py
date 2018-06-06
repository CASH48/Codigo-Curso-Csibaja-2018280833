def fibonacci(num):
    if isinstance (num, int) and (num > 0):
        return fibonacci_aux(num)
    else:
        return "Error"
    
def fibonacci_aux(num):
    if (num == 1) or (num == 2):
        return 1
    else:
        return fibonacci_aux (num-1) + fibonacci_aux (num-2)

