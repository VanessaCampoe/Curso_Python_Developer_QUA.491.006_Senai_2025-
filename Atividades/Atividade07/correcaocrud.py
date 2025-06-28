import os
nomes = []
while True :
    print("1. Cadastrar novo nome na lista ")
    print("2. Listar nomes na lista")
    print("3. Pesquisar nome na lista")
    print("4. Alterar nome na lista")
    print("5. Excluir nome na lista")
    print("6. Sair do programa ")
    opcao = input("Escolha uma opção desejejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela do terminal
    match opcao:
    # Aqui usamos match para verificar a opção escolhida
    # e executar a ação correspondente.
    
        case"1":
            try:
                novo_nome = input("Informe o nome: ").title().strip()
                nomes.append(novo_nome)
                print(f"{novo_nome} cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possivel inserir um novo nome: {e}")
            finally:
                continue

          
        case"2":
            try:
                
                for i in range(len(nomes)):
                    print(f"{i+1}. {nomes[i]}")
                print('-'*40)
            except Exception as e:
                print(f"Não foi possivel exibir a lista de nomes: {e}")
            finally:
                continue
            
            
        
        case"3":
            nome_pesquisado = input("Informe o nome a ser pesquisado: ").title().strip()
            os.system("cls" if os.name == "nt" else "clear") # quando devo incluir essa limpeza  de tela?
            qtde = nomes.count(nome_pesquisado)
            print(f"O nome {nome_pesquisado} foi encontrado {qtde} vezes na lista.")
            continue
            
            
            
        case"4":
            try:
                i = int(input("Informe o nome a ser alterado: "))
                if i < 0 and i < len(nomes):
                    nomes[i] = input(" Informe o novo nome:").title().strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print(" Nome alterado com sucesso")
                else:
                    print("Índice inválido. Tente novamente.")
            except Exception as e :
                print(f"Não foi possivel alterar o nome: {e}")
            finally:
                continue
        case"5":
            try:
                i = int(input("Informe o nome a ser excluido: "))
                if i <= 0 and i < len(nomes):
                    del(nomes[i])
                    os.system("cls" if os.name == "nt" else "clear")
                    print(" Nome excluido com sucesso ")
                    
                    
                else:
                    print("Indice invalido.")
            except Exception as e:
                print(f"Não foi possivel excluir o nome: {e}")
            finally:
                continue
        case"6":
            print("Programa encerrado ")
            break
        case"_":
            print("Opção inavalida")
            continue
    
    
    
    
    
    
    
    
    
    
   