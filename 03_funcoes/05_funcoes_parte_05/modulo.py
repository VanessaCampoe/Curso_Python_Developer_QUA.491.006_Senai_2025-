import math
import os



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def primeiro_grau(a,b):
    # a*x + b = 0
    
    x = -b / a
    return x

def segundo_grau(a, b, c):
    # a*x² + b*x + c = 0
    
    if a != 0:
        delta = (b**2)- (4*a*c)
        if delta> 0:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            yield f"x' = {x1}" 
            yield f"x'' = {x2}"
        elif delta == 0:
            yield " nao ha raizes reais para x  "
        else:
            x = -b/ (2*a)
            yield f"x = {x}"

    else: 
            yield primeiro_grau(b, c)
            
            
            #  yield retorno de uma funçao e, lista e ele para a funçai 
      