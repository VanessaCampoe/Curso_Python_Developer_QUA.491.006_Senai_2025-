'''
Atividade 02 - IMC
Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
o programa de ve mostrar o valor do imc arredondado para duas casas decimais.
Caso o imc seja menor que < 18.5: Abaixo do peso

Caso o imc seja menor que 18.5 <= IMC < 25: Peso ideal
Caso o imc seja menor que 25 <= IMC < 30: acima do peso 
Caso o imc seja menor que IMC >= 35: Obeso
Caso o imc seja menor que IMC >= 40: Obesidade nivel 2
# Caso o imc seja menor que IMC >= 40: Obesidade mórbida
# NOTE  o usuario devera informar o encerramenro do programa ou , para pode repedir o calculo quantas vezes quiser 




'''
while True:
    
    try:
            nome = input("Informe seu nome:").title().strip()
            peso = float(input('Informe seu peso em kg: ').replace(",","."))
            altura = float(input('Informe sua altura em metros: ').replace(",","."))
            
            imc = peso / (altura ** 2)
            
            print(f"O valordo IMC de{nome} é {imc:.2f}")
            if imc < 18.5:
                status = "Abaixo do peso"
                print(f"{nome} esta abaixo do peso.")
            elif 18.5 <= imc < 25:
                status = "Peso ideal"
                print(f"{nome} esta no peso.")
            elif 25 <= imc < 30:
                status = "Acima do peso"
                print(f"{nome} esta acima do peso.")
            elif 30 <= imc < 35:
                status = "Obeso"
                print(f"{nome} esta obeso.")     
            elif 35 <= imc < 40:
                status = "Obesidade nível 2"
                print(f"{nome} esta Obesidade nível 2.")
            elif imc >= 40:
                status = "Obesidade mórbida"
                print(f"{nome} esta Obesidade mórbida.")
                
                
                
            while True:
                prosseguir = input("Deseja refazer? (s/n)").lower().strip()
                if prosseguir == "s" or prosseguir == "n":
                    break
                else:
                    print ("opção invalida") 
                    continue  
            match prosseguir:
                case"s":
                    continue
                case "n":
                    break
                
            
    except Exception as e:
        print(f"Não foi possivel calcular o IMC. {e}.")
        continue
        
        # o que faltou try de tratamento de excesao , e depois um em caso de erro
        # exxe em caso de erro e o except
        # faltou o arredondamento print(f"O valordo IMC de{nome} é {imc:.2f}")
        