# laço de repetição 
while True:
    #tratamento de exceÇõ 
    
    try:
        ...
        
        gasolina = float(input('Informe o valor da gasolina (R$): ').replace(",","."))
        etanol = float(input('Informe o valor do etanol (R$): ').replace(",","."))
        calculo = (etanol/gasolina )*100
        result = "gasolina" if calculo > 70 else "etanol" 
        
        print(f"Resultado = {calculo:.2f} Compensa abastecer com {result}. ")
        
        opcao = input('\nDeseja informar novos valores? (s/n): ').strip().lower()
       

        match opcao:
            case 's':
                continue
            case 'n':
                print("Programa encerrado. Obrigado por usar!")
                break
            case _:
                print("Opção inválida! ")

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar apenas números válidos.\n")
        
        
    
    #  ternario com result e  a outra normal com if 
# mais de 3 saidas possiveis usar o case 
