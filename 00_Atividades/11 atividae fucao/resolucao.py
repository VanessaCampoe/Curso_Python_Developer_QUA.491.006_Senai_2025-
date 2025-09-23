def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)
    
n = int(input("número de termos da sequência a ser calculada de Fibonacci): "))

print(calcular_fibonacci(n))
