
def calcul_multiplication(*args):
    result = 1
    for number in args:
        result *= number
        
    return result

calcul_multiplication(1, 2, 3, 4, 5)


def decorator():
    
    def my_function(*args):
        # Traitement avant execution de la fonction
        
        # fonction de multiplication
        
        # Traitement après execution de la fonction
        return sum(args)
    
    return my_function