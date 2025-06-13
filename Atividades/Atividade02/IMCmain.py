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

peso = float(input('Informe seu peso em kg: ').replace(",","."))
altura = float(input('Informe sua altura em metros: ').replace(",","."))
imc = peso / (altura ** 2)
if imc < 18.5:
    status = "Abaixo do peso"
    print(f"Seu IMC é {imc:.2f}. Status: {status}")
elif 18.5 <= imc < 25:
    status = "Peso ideal"
    print(f"Seu IMC é {imc:.2f}. Status: {status}")
elif 25 <= imc < 30:
    status = "Acima do peso"
    print(f"Seu IMC é {imc:.2f}. Status: {status}")
elif 30 <= imc < 35:
    status = "Obeso"
    print(f"Seu IMC é {imc:.2f}. Status: {status}")     
elif 35 <= imc < 40:
    status = "Obesidade nível 2"
    print(f"Seu IMC é {imc:.2f}. Status: {status}")
elif imc >= 40:
    status = "Obesidade mórbida"
    print(f"Seu IMC é {imc:.2f}. Status: {status}")