# declaração de variaveis 
x = float (input("Informe o valorde x:").replace(",","."))
y = float (input("Informe o valorde y:").replace(",","."))


#menu 
print(f"{"-"*20}Escolha a operação {"-"*20} \n")
print("1 - Soma")
print("2 - Subtração ")
print("3 - Multiplicação")
print("4 - Divisão ")


# usuario escolhe a operação desejada
operador = input("Informe a operação desejada:").strip()

#machat case 
match operador :
    case "1":
        print(f"A soma dos valores é {x+y}.")
    case "2":    
        print(f"A soma dos valores é {x-y}.")
    case "3":
        print(f"A soma dos valores é {x*y}.")
    case "4":
        print(f"A soma dos valores é {x/y}.")
    case _: # default  aqui nao existe aspas 
        print("Operação invalida")
        
        # aqui colocar para poder voltar ao menu e fazer novo  calculo sem precisar acrecenstra novos numeros
