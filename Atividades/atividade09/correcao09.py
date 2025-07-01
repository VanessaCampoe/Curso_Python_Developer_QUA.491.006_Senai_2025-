'''
# TODO - atividade: Crie um programa que faça as seguintes funções:
# 1 - Cadastre um novo usuário
# 2 - Liste todos os usuários cadastrados
# 3 - Altere os dados de um usuário
#   - Fazer do sorteio usuario 
# 4 - Exclua um usuário
# 5 - Saia do programa
# NOTE - dados do usuário:
# - Nome completo
# - Data de Nascimento
# - E-mail
# - CPF
# - Telefone
# - Gênero
# - Data do cadastro(pegar do sistema )
# - Hora do cadastro (pegar do sistema )
# ---
'''




import os 
import random
import datetime
from datetime import date

# lista de usuarios vazias 

usuarios = []



# loop 

while True:
    
    #dicionario
    
    usuario = {}
    # menu 
    
    print("\n--- MENU ---")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Alterar usuário")
    print("4. Sortear usuário")
    print("5. Excluir usuário")
    print("6. Sair")

    opcao = input("Escolha uma opção: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case "1":
            try:
                usuario['nome'] = input("Informe o nome completo: ").strip().title()
                usuario['data_nascimento'] = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
                usuario['email'] = input("Informe o e-mail: ").strip().lower()
                usuario['cpf'] = input("Informe o CPF: ").strip()
                usuario['telefone'] = input("Informe o telefone: ").strip()
                usuario['genero'] = input("Informe o gênero: ").strip().title()
                usuario['data_cadastro'] = date.today().strftime("%d/%m/%Y")
                usuario['hora_cadastro'] = datetime.datetime.now().strftime("%H:%M:%S")
                
                usuarios.append(usuario)
                os.system('cls' if os.name == 'nt' else 'clear')

                print(f"Usuário {usuario.get('nome')}cadastrado com sucesso!")
            except Exception as e:
                print(f"Erro ao cadastrar usuário: {e}")
            finally:
                continue
        case "2":
            try:
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                for i in range (len(usuarios)):
                    print(f"\nUsuário {i}:")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}:{usuarios[i].get(chave)}")
            except Exception as e:
                print(f"Erro ao listar usuários: {e}")
            finally:
                continue
        case "3":
            try:
                i = int(input("Informe o índice do usuário a ser alterado: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                if i >= 0 and i < len(usuarios):
                    print("Dados atuais do usuário:")
                    for chave, in usuarios[i].items(): # usuarios do indice i (assim q se le )
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}") 
                    print("\n")
                    
                    while True: # mudaça feita aqui 
                    
                    
                    
                    
                        chave_escolhida = input ("Informe a cgave a ser alterada :").strip().lower()
                        if chave_escolhida in usuarios[i]:
                            usuarios[i][chave_escolhida] = input(f"Novo valor para {chave_escolhida} :")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Chave alterada com sucesso !")
                            
                            
                            
                        else:
                            print("Chave inexistente. ") 
                        while True:
                            #mudança 
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir == "s" or prosseguir == "n":
                                break
                            else:
                                continue
                        match prosseguir:
                                case "s":
                                    continue
                                case "n":
                                    break 
                                
                                
                
                            
                else:
                    print("Índice inválido. Tente novamente.") 
            except Exception as e :
                
                    print(f"Erro alterar o  usuários: {e}")
            finally:
                continue
                    
        case "4":
                    
            try:
                i = random.randint(0, len(usuarios) - 1)
                print("\nUsuário sorteado:")
                for chave, in usuarios[i].items():  
                    print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    continue
            except Exception as e:
                print(f"nao foi possivel sortear um usuario: {e}")
            finally:
                continue
                
        case "5":
            try:
                i = int(input("Informe o índice do usuário a ser excluído: "))
                if i < 0 and i >= len(usuarios):
                    print("Índice inválido.")
                else:
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")

                while True:
                    excluir = input("Deseja excluir este usuário? (s/n): ").strip().lower()
                    if excluir == "s" or excluir == "n":
                        break
                    else:
                        print("Opção inválida. ")
                        continue
                    match excluir:
                        case "s":
                            del usuarios[i]
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"Usuário {i} excluído com sucesso!")
                            break
                        case "n":
                            print("usuario nao excluido .")
                else:
                    print("Opção inválida. Tente novamente.")   
            
            except Exception as e:
                print(f"Nao foi possivel excluir usuario: {e}")
            finally:
                continue
        case "6":
            print("Saindo do programa. Até logo!")
            break  # Quebra o loop para finalizar o programa
        case _:
            print("Opção inválida. Tente novamente.")
            continue  # Volta para o início do loop
            