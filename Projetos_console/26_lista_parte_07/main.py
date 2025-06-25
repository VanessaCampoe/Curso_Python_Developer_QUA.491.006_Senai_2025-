import os
import random
#lista 
nomes = []

while True:
    print("1- Inserir nome na  lista ")
    print("3 - Sortear nome")
    print("2 - Exibir lista de nomes")
   
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case"1":
            try:
                novo_nome = input("Informe o nome: ").title().strip()
                os.system("cls" if os.name == "nt" else "clear")
                nomes.append(novo_nome)
                print(" Nome inserido com sucesso !")
            except Exception as e: 
                print(f"Erro ao inserir nome: {e}.")
            finally:
                continue

        case"2":
            try:
                #ordenar a lista
                nomes.sort()
                for nome in nomes:
                    print(nome)
            except Exception as e:
                
                    print(f"Não foi possivel exibir lista,{e}.")
            finally:
                    continue


                 
    



        case"3":
              i = random.randint(0, len(nomes))
              print(f"Nome sorteado:{nomes[i]}")
              continue
            



            
        case"4":
            print("Programa encerrado")
            break  
            nome = input("Informe o nome a ser inserido: ").strip().title()


        case _:
            print("Opção inválida")
            continue