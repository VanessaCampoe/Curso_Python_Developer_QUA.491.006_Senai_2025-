"""
    # todo - atividade crie um programa q receba do usuario um  numero  (aqui eu ja comço commeu imput  . isso se ue for direto )
    # ineiro e o pprogra, calcula o valor da sequencia de fibonacci 
"""
# Programa que calcula a sequência de Fibonacci

# Recebe um número inteiro do usuário
n = int(input("Digite um número inteiro (número de termos da sequência de Fibonacci): "))

# Verifica se o número é válido
if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print("Sequência de Fibonacci:")
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

