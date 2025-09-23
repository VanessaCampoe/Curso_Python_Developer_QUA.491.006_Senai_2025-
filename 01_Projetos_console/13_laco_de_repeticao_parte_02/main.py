while True:

    #menu

    print(f"{'-'*20} MENU {'-'*20}")
    print("0 Encerrado")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")    
    print("4 - Dividir")
    operacao = input("Informe a operação desejada:").strip() # aqui devo usar o strip para remover os espaços em branco
    match operacao:
        case "0":
            print("Encerrando...")
            break
        case "1":
            try:
                x = float(input("Informe o primeiro número:").replace(",","."))
                y = float(input("Informe o primeiro número:").replace(",","."))
                print(f'{x} + {y} = {x+y}')
            except Exception as e:
                print(f"nao foi possivel somar {e}.")
            finally: # para voltar para o inicio do loop deve ser assim para nao dar continuidade com o codigo 
                continue

                # observar a identação do codigo try except finally eles ficam alinhados 

            
        case "2":
            try:
                x = float(input("Informe o primeiro número:").replace(",","."))
                y = float(input("Informe o primeiro número:").replace(",","."))
                print(f"{x} + {y} = {x+y}")
            except Exception as e:
                print(f"nao foi possivel somar {e}.")
            finally: # para voltar para o inicio do loop deve ser assim para nao dar continuidade com o codigo 
                continue
            
        case "3":
            try:
                x = float(input("Informe o primeiro número:").replace(",","."))
                y = float(input("Informe o primeiro número:").replace(",","."))
                print(f"{x} + {y} = {x+y}")
            except Exception as e:
                print(f"nao foi possivel somar {e}.")
            finally: # para voltar para o inicio do loop deve ser assim para nao dar continuidade com o codigo 
                continue
        case "4":
            try:
                x = float(input("Informe o primeiro número:").replace(",","."))
                y = float(input("Informe o primeiro número:").replace(",","."))
                print(f"{x} + {y} = {x+y}")
            except Exception as e:
                print(f"nao foi possivel somar {e}.")
            finally: # para voltar para o inicio do loop deve ser assim para nao dar continuidade com o codigo 
                continue
        case _:
                print("Operador inválido")# para voltar para o inicio do loop deve ser assim para nao dar continuidade com o codigo 
                continue