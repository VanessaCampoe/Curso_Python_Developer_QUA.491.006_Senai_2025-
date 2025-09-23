'''# atividade :crie um programa com o seguinta menu:
calcular  area de um circulo 
- calcular o tamnaho de um circunferencencia 
- sair do programa
'''
import os
import math as m 


while True:
    os.system('cls')
    print("Menu:")
    print("1 - Calcular a área de um círculo")
    print("2 - Calcular o tamanho de uma circunferência")
    print("3 - Sair do programa")

    opcao = input("Informe a opção desejada:").strip()

   
    
    try:
        if opcao =="1" or opcao == "2":
            raio = float(input("informe o valor do raio").replace(',', '.'))
            
        else:
            ...
        os.system('cls' if os.name == 'nt' else 'clear')
        match opcao:
            case "1":
                raio = float(input("Digite o raio do círculo: "))
                area = m.pi * raio ** 2
                print(f"A área do círculo é: {area}.")
                continue
            case "2":
                raio = float(input("Digite o raio da circunferência: "))
                circunferencia = 2 * m.pi * raio
               
                print(f"O tamanho da circunferência é: {circunferencia}.")
            case "3":
                print("Programa encerrado  ")
                break
            case _:
                
                print("Opção inválida. ")

    except ValueError:
        print("Não foi possivel calcular .")
        continue 
    