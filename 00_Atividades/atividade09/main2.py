'''
# TODO - atividade: Crie um programa que faça as seguintes funções:
# 1 - Cadastre um novo usuário ok
# 2 - Liste todos os usuários cadastrados ok
# 3 - Altere os dados de um usuário ok
# 4 - Fazer do sorteio usuario ok
# 5 - Exclua um usuário
# 6 - Saia do programa
# NOTE - dados do usuário:
# - Nome completo
# - Data de Nascimento
# - E-mail
# - CPF
# - Telefone
# - Gênero
# - Data do cadastro(pegar do sistema )
# - Hora do cadastro (pegar do sistema )
'''
# importar bibliotecas
import datetime 
import os 
import random


usuario = []
while True:
    dicionario = {}
    print("Bem-vindo ao sistema de cadastro de usuários!")
    print("Selecione uma opção:")
    print("1. Cadastrar novo usuario na lista ")
    print("2. Listar usuarios cadastrados ")
    print("3. Alterar dados do usuario ")
    print("4. Fazer do sorteio usuario ")
    print("5. Excluir usuario na lista")
    print("6. Sair do programa ")
    
    
    
    
    opcao = input("Escolha uma opção desejejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela do terminal
    match opcao:
    # Aqui usamos match para verificar a opção escolhida
    # e executar a ação correspondente.
        case"1":
            try:
                novo_usuario = input("Informe o usuario: ").title().strip()
                lista.append(novo_usuario)
                print(f"{novo_usuario} cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possivel inserir um novo usuario: {e}")
            finally:
                continue

          
        case"2":
            try:
                
                for i in range(len(usuario)):
                    print(f"{i+1}. {usuario[i]}")
                print('-'*40)
            except Exception as e:
                print(f"Não foi possivel exibir a lista de usuarios: {e}")
            finally:
                continue
        case"3":
            try:
                i = int(input("Informe o usuario a ser alterado: "))
                if i < 0 and i < len(usuario):
                    usuario[i] = input(" Informe o novo usuario:").title().strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print(" Usuario alterado com sucesso")
                else:
                    print("Índice inválido. Tente novamente.")
                    
            
            