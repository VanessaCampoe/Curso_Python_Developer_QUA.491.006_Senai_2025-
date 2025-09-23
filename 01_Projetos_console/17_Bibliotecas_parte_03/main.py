import math as m 
# exibir o numero do pi 
print(f"Numero do pi:{m.pi}.")
# raiz quadrada 
try:

    
    n = int(input("Informe um numero inteiro:"))
    print(f"A raiz quadrada de {n} é {m.sqrt(n)}")
except Exception as e:
    print(f"Não foi possivel calcular a raiz quadrada. {e}.")
