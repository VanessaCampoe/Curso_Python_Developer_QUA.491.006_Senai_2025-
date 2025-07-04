import json
import os

usuarios = []
caminho_arquivo = ""

def salvar_json():
    if caminho_arquivo:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)

def carregar_json():
    global usuarios
    if caminho_arquivo and os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            usuarios.clear()
            usuarios.extend(json.load(f))

while True:
    print("Menu:")
    print("1 - Criar um novo arquivo JSON")
    print("2 - Abrir arquivo JSON existente")
    print("3 - Cadastrar novo usuário")
    print("4 - Listar usuários")
    print("5 - Pesquisar usuário por CPF")
    print("6 - Alterar dados de um usuário")
    print("7 - Deletar usuário por CPF")
    print("8 - Sair do programa")
    opcao = input("Escolha uma opção: ").strip()

    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case "1":
            caminho_arquivo = input("Digite o caminho do novo arquivo JSON (ex: usuarios.json): ").strip()
            usuarios.clear()
            salvar_json()
            print("Novo arquivo JSON criado com sucesso.")

        case "2":
            caminho_arquivo = input("Digite o caminho do arquivo JSON existente: ").strip()
            if os.path.exists(caminho_arquivo):
                carregar_json()
                print("Arquivo carregado com sucesso.")
            else:
                print("Arquivo não encontrado.")

        case "3":
            if not caminho_arquivo:
                print("Abra ou crie um arquivo JSON primeiro.")
                continue
            usuario = {}
            usuario['nome'] = input("Nome: ").strip()
            usuario['data_de_nascimento'] = input("Data de nascimento: ").strip()
            usuario['cpf'] = input("CPF: ").strip()
            usuario['email'] = input("Email: ").strip()
            usuario['telefone'] = input("Telefone: ").strip()
            usuario['filme_favorito'] = input("Filme favorito: ").strip()
            usuarios.append(usuario)
            salvar_json()
            print("Usuário cadastrado com sucesso.")

        case "4":
            if not caminho_arquivo:
                print("Abra ou crie um arquivo JSON primeiro.")
                continue
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for i, user in enumerate(usuarios, start=1):
                    print(f"\nUsuário {i}:")
                    for chave, valor in user.items():
                        print(f"{chave}: {valor}")

        case "5":
            if not caminho_arquivo:
                print("Abra ou crie um arquivo JSON primeiro.")
                continue
            cpf_busca = input("Digite o CPF do usuário que deseja buscar: ").strip()
            encontrado = False
            for user in usuarios:
                if user['cpf'] == cpf_busca:
                    print("Usuário encontrado:")
                    for chave, valor in user.items():
                        print(f"{chave}: {valor}")
                    encontrado = True
                    break
            if not encontrado:
                print("Usuário não encontrado.")

        case "6":
            if not caminho_arquivo:
                print("Abra ou crie um arquivo JSON primeiro.")
                continue
            cpf_alterar = input("Digite o CPF do usuário que deseja alterar: ").strip()
            for user in usuarios:
                if user['cpf'] == cpf_alterar:
                    print("Deixe em branco se não quiser alterar o campo.")
                    novo_nome = input(f"Novo nome ({user['nome']}): ").strip()
                    novo_email = input(f"Novo email ({user['email']}): ").strip()
                    novo_telefone = input(f"Novo telefone ({user['telefone']}): ").strip()
                    novo_filme = input(f"Novo filme favorito ({user['filme_favorito']}): ").strip()
                    novo_nascimento = input(f"Nova data de nascimento ({user['data_de_nascimento']}): ").strip()

                    if novo_nome: user['nome'] = novo_nome
                    if novo_email: user['email'] = novo_email
                    if novo_telefone: user['telefone'] = novo_telefone
                    if novo_filme: user['filme_favorito'] = novo_filme
                    if novo_nascimento: user['data_de_nascimento'] = novo_nascimento

                    salvar_json()
                    print("Dados do usuário atualizados.")
                    break
            else:
                print("Usuário não encontrado.")

        case "7":
            if not caminho_arquivo:
                print("Abra ou crie um arquivo JSON primeiro.")
                continue
            cpf_deletar = input("Digite o CPF do usuário que deseja deletar: ").strip()
            for i, user in enumerate(usuarios):
                if user['cpf'] == cpf_deletar:
                    confirmacao = input(f"Tem certeza que deseja deletar o usuário {user['nome']}? (s/n): ").strip().lower()
                    if confirmacao == 's':
                        usuarios.pop(i)
                        salvar_json()
                        print("Usuário deletado com sucesso.")
                    break
            else:
                print("Usuário não encontrado.")

        case "8":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
