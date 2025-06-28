# Importo datetime porque vou precisar da data e hora atuais para registrar quando o usuário for cadastrado.
import datetime

# Importo os para poder limpar a tela do terminal e deixar a interface mais limpa a cada ação.
import os

# Importo random para poder sortear um usuário aleatoriamente quando essa opção for escolhida.
import random

# Defino uma variável para o nome do arquivo que vai guardar os usuários. Escolhi .txt para ser simples e legível.
arquivo = "usuarios.txt"

# Aqui verifico se o arquivo já existe. Se não existir, crio um arquivo vazio.
# Faço isso para evitar erro na hora de ler o arquivo depois, garantindo que ele sempre exista.
if not os.path.exists(arquivo):
    open(arquivo, "w").close()

# Inicio o loop principal do programa, que fica rodando até o usuário decidir sair.
# Cada vez que o loop roda, o menu é mostrado para o usuário escolher uma opção.
while True:
    # Apresento as opções do sistema para o usuário.
    print("\n--- MENU ---")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Alterar usuário")
    print("4. Sortear usuário")
    print("5. Excluir usuário")
    print("6. Sair")

    # Peço para o usuário digitar a opção que quer executar.
    # Uso strip() para tirar espaços antes/depois e evitar erros bobos.
    opcao = input("Escolha uma opção: ").strip()

    # Limpo a tela para o terminal ficar mais organizado.
    # Uso 'cls' no Windows e 'clear' no Linux/Mac para funcionar em qualquer sistema.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Se o usuário escolheu a opção 1, vamos cadastrar um novo usuário.
    if opcao == "1":
        # Peço os dados um a um para preencher o cadastro.
        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento: ")
        email = input("E-mail: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        genero = input("Gênero: ")

        # Aqui eu pego a data e hora atuais para registrar quando o cadastro foi feito.
        agora = datetime.datetime.now()
        # Formato a data e a hora em strings legíveis para salvar no arquivo.
        data_cadastro = agora.strftime("%d/%m/%Y")
        hora_cadastro = agora.strftime("%H:%M:%S")

        # Junto tudo em uma linha só, separando os campos por ponto e vírgula.
        # Isso me ajuda a salvar e depois ler os dados facilmente.
        usuario = f"{nome};{nascimento};{email};{cpf};{telefone};{genero};{data_cadastro};{hora_cadastro}\n"

        # Abro o arquivo no modo 'append' para adicionar essa linha no final sem apagar os anteriores.
        with open(arquivo, "a") as f:
            f.write(usuario)

        # Aviso que o cadastro deu certo.
        print("Usuário cadastrado com sucesso!")

    # Se a opção for 2, vou listar todos os usuários cadastrados.
    elif opcao == "2":
        # Abro o arquivo para leitura e pego todas as linhas (cada linha é um usuário).
        with open(arquivo, "r") as f:
            linhas = f.readlines()

        # Se o arquivo estiver vazio, aviso que não tem nenhum usuário cadastrado.
        if not linhas:
            print("Nenhum usuário cadastrado.")
        else:
            # Para cada linha, faço o seguinte:
            for i in range(len(linhas)):
                # Quebro a linha nos campos usando o separador ';'
                dados = linhas[i].strip().split(";")
                # Exibo os dados com rótulos para o usuário entender.
                print(f"\nUsuário {i + 1}")
                print("Nome:", dados[0])
                print("Nascimento:", dados[1])
                print("E-mail:", dados[2])
                print("CPF:", dados[3])
                print("Telefone:", dados[4])
                print("Gênero:", dados[5])
                print("Data de Cadastro:", dados[6])
                print("Hora de Cadastro:", dados[7])

    # Se o usuário escolheu a opção 3, vamos alterar dados de um usuário cadastrado.
    elif opcao == "3":
        # Abro o arquivo e leio as linhas para carregar os usuários.
        with open(arquivo, "r") as f:
            linhas = f.readlines()

        # Se não tem usuários, não tem o que alterar.
        if not linhas:
            print("Nenhum usuário para alterar.")
        else:
            # Mostro os nomes com números para o usuário escolher qual deseja alterar.
            for i in range(len(linhas)):
                print(f"{i + 1}. {linhas[i].split(';')[0]}")

            # Peço que digite o número do usuário que quer alterar.
            end = int(input("Digite o número do usuário a alterar: ")) - 1

            # Verifico se o número é válido, para evitar erros.
            if 0 <= end < len(linhas):
                # Divido a linha do usuário escolhido em campos para facilitar a alteração.
                dados = linhas[end].strip().split(";")

                # Para cada campo, peço para digitar o novo valor.
                # Se o usuário apertar Enter sem digitar nada, mantenho o valor antigo.
                nome = input(f"Nome ({dados[0]}): ") or dados[0]
                nascimento = input(f"Nascimento ({dados[1]}): ") or dados[1]
                email = input(f"E-mail ({dados[2]}): ") or dados[2]
                cpf = input(f"CPF ({dados[3]}): ") or dados[3]
                telefone = input(f"Telefone ({dados[4]}): ") or dados[4]
                genero = input(f"Gênero ({dados[5]}): ") or dados[5]

                # Recrio a linha do usuário com os dados atualizados,
                # mantendo a data e hora do cadastro original para não perder essa informação.
                nova_linha = f"{nome};{nascimento};{email};{cpf};{telefone};{genero};{dados[6]};{dados[7]}\n"

                # Substituo a linha antiga pela nova na lista de linhas.
                linhas[end] = nova_linha

                # Abro o arquivo em modo escrita para salvar as alterações.
                # Isso vai apagar o conteúdo antigo e salvar tudo novo.
                with open(arquivo, "w") as f:
                    f.writelines(linhas)

                # Confirmo que a alteração deu certo.
                print("Usuário alterado com sucesso.")
            else:
                # Caso o número seja inválido, aviso o usuário.
                print("Número inválido.")

    # Se a opção for 4, vamos sortear um usuário aleatório.
    elif opcao == "4":
        # Leio as linhas do arquivo para pegar os usuários.
        with open(arquivo, "r") as f:
            linhas = f.readlines()

        # Se não tem usuário, aviso.
        if not linhas:
            print("Nenhum usuário para sortear.")
        else:
            # Uso random.choice para pegar uma linha qualquer da lista.
            sorteado = random.choice(linhas).strip().split(";")

            # Exibo os dados do usuário sorteado.
            print("\nUsuário sorteado:")
            print("Nome:", sorteado[0])
            print("Nascimento:", sorteado[1])
            print("E-mail:", sorteado[2])
            print("CPF:", sorteado[3])
            print("Telefone:", sorteado[4])
            print("Gênero:", sorteado[5])
            print("Data de Cadastro:", sorteado[6])
            print("Hora de Cadastro:", sorteado[7])

    # Se a opção for 5, vamos excluir um usuário.
    elif opcao == "5":
        # Leio as linhas do arquivo.
        with open(arquivo, "r") as f:
            linhas = f.readlines()

        # Se não tem usuário, aviso.
        if not linhas:
            print("Nenhum usuário para excluir.")
        else:
            # Mostro a lista para o usuário escolher quem excluir.
            for i in range(len(linhas)):
                print(f"{i + 1}. {linhas[i].split(';')[0]}")

            # Peço o número do usuário a excluir.
            end = int(input("Digite o número do usuário a excluir: ")) - 1

            # Verifico se o número é válido.
            if 0 <= end < len(linhas):
                # Removo o usuário escolhido da lista.
                removido = linhas.pop(end)

                # Regravo o arquivo com os usuários restantes.
                with open(arquivo, "w") as f:
                    f.writelines(linhas)

                # Informo quem foi removido.
                print(f"Usuário removido: {removido.split(';')[0]}")
            else:
                print("Número inválido.")

    # Se a opção for 6, o usuário quer sair do programa.
    elif opcao == "6":
        print("Saindo do programa. Até logo!")
        break  # Quebro o loop para finalizar o programa

    # Se o usuário digitar qualquer coisa que não seja uma opção válida:
    else:
        print("Opção inválida. Tente novamente.")
