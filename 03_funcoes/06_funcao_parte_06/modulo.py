# fatoreaL CALCULE UM FATOREAL
def fatorial(n):
    #n!
    # ternario 
    return 1 if n == 0 or n == 1 else n * fatorial(n - 1)  

