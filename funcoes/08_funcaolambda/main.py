# lambda 
pg = lambda X: X * 2
pa = lambda X: X + 2


#algoritmo principal
if __name__ == "__main__":
    
    #lista
   numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Progressão Aritmética: {list(map(pg, numeros))}")
print(f"Progressão Geométrica: {list(map(pa, numeros))}")

    #pa prodressao aritimetica
    