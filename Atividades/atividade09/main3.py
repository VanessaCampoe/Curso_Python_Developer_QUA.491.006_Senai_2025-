import datetime
import os
import random

usuarios = []

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Alterar usuário")
    print("4. Sortear usuário")
    print("5. Excluir usuário")
    print("6. Sair")

    opcao = input("Escolha uma opção: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == "1":
        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento: ")
        email = input("E-mail: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        genero = input("Gênero: ")
        agora = datetime.datetime.now()
        data_cadastro = agora.strftime("%d/%m/%Y")
        hora_cadastro = agora.strftime("%H:%M:%S")
        usuario = [nome, nascimento, email, cpf, telefone, genero, data_cadastro, hora_cadastro]
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for i in range(len(usuarios)):
                print(f"\nUsuário {i+1}:")
                print("Nome:", usuarios[i][0])
                print("Nascimento:", usuarios[i][1])
                print("E-mail:", usuarios[i][2])
                print("CPF:", usuarios[i][3])
                print("Telefone:", usuarios[i][4])
                print("Gênero:", usuarios[i][5])
                print("Data de Cadastro:", usuarios[i][6])
                print("Hora de Cadastro:", usuarios[i][7])

    elif opcao == "3":
        if not usuarios:
            print("Nenhum usuário para alterar.")
        else:
            for i in range(len(usuarios)):
                print(f"{i+1}. {usuarios[i][0]}")
            escolha = int(input("Digite o número do usuário para alterar: ")) - 1
            if 0 <= escolha < len(usuarios):
                nome = input("Novo nome (Enter para manter): ")
                if nome:
                    usuarios[escolha][0] = nome
                nascimento = input("Nova data de nascimento: ")
                if nascimento:
                    usuarios[escolha][1] = nascimento
                email = input("Novo e-mail: ")
                if email:
                    usuarios[escolha][2] = email
                cpf = input("Novo CPF: ")
                if cpf:
                    usuarios[escolha][3] = cpf
                telefone = input("Novo telefone: ")
                if telefone:
                    usuarios[escolha][4] = telefone
                genero = input("Novo gênero: ")
                if genero:
                    usuarios[escolha][5] = genero
                print("Usuário alterado com sucesso.")
            else:
                print("Número inválido.")

    elif opcao == "4":
        if usuarios:
            sorteado = random.choice(usuarios)
            print("\nUsuário sorteado:")
            print("Nome:", sorteado[0])
            print("Nascimento:", sorteado[1])
            print("E-mail:", sorteado[2])
            print("CPF:", sorteado[3])
            print("Telefone:", sorteado[4])
            print("Gênero:", sorteado[5])
            print("Data de Cadastro:", sorteado[6])
            print("Hora de Cadastro:", sorteado[7])
        else:
            print("Nenhum usuário para sortear.")

    elif opcao == "5":
        if not usuarios:
            print("Nenhum usuário para excluir.")
        else:
            for i in range(len(usuarios)):
                print(f"{i+1}. {usuarios[i][0]}")
            escolha = int(input("Digite o número do usuário para excluir: ")) - 1
            if 0 <= escolha < len(usuarios):
                removido = usuarios.pop(escolha)
                print(f"Usuário {removido[0]} excluído com sucesso.")
            else:
                print("Número inválido.")

    elif opcao == "6":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

