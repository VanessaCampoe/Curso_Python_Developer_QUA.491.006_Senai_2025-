'''
Crie um programa que receba do usuario o valor de etanal e da gasolina, em reais e informe ao usuario  qual o melhor combustivelpara abastecer.
#NOTE - o usuario podera informar varias vezes os valores , e irá encerraro programa quando desejado .
#NOTE - calculo: compensa etanol caso ele tenha ate 70% do valor da gasolina.
#NOTE - oompensa etanol caso ele tenha mais de 70% do valor da gasolina.
#NOTE - Divirtam-se!!! =D
'''

gasolina = float(input('Informe o valor da gasolina: '))
etanol = float(input('Informe o valor do etanol: '))
while True:
    continuar = input('Deseja continuar? (s/n): ').strip().lower()
    
    abastecer = input('Escolha o combustivel: \n1 - Etanol\n2 - Gasolina\n')
    case "1" etanol <= gasolina * 0.7:
        
        print('Abasteça com etanol!')
    case "2":    
        print('Abasteça com gasolina!')