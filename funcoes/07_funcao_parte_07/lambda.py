# funcao normal 
# def somar(x, y):
#     return x + y
# return = result 

import os
# funcao importada
# funcao lambda
somar = lambda x, y: x + y
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    try:
            x = int(float(input("Informe o valor de x: ")))
            y = int(float(input("Informe o valor de y: ")))
            result = somar(x, y)
            limpar()
           

            print(f"O resultado da soma é {result}.")
    except Exception as e:
        print (f" nao e possivel somar. {e}")
