"""#TODO - atividade :
    faça um CRUD (Create, Read, Update, Delete) de um arquivo JSON.
    opções do menu  :
    
    - criar um novo arquivo JSON (usuario ira informar o diretorio )
    - abrir arquivo json existente(usuario ira informar o diretorio )
    - cadastrar nono usuario em um arquivo JSON
    - listar usuarios de um arquivo JSON
    - pesquisar usuario em um arquivo JSON
    - alterar dados de um usuario em um arquivo JSON
    - Deletar usuario de um arquivo JSON
    - sair do programa 
    
    
    dados do usuario 
    nome 
    data de nascimento 
    cpf
    emiail
    telefone
    filme favorito do usuario 
    
    """
    
import json
import os

usuarios= []
novo_arquivo = ""
while True:
    usuario = {}
    print ("Menu:")
    print("1 - criar um novo arquivo JSON")
    print("2 - abrir arquivo JSON existente")
    print("3 - cadastrar novo usuario em um arquivo JSON")
    print("4 - listar usuarios de um arquivo JSON")
    print("5 - pesquisar usuario em um arquivo JSON")
    print ("6 - alterar dados de um usuario em um arquivo JSON")
    print("7 - deletar usuario de um arquivo JSON")
    print("8 - sair do programa")
    opcao = input("Escolha uma opção: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    match opcao:
        case "1":
            usuario['nome'] = input("Digite o nome do arquivo JSON: ").strip().lower()
            usuario[data_de_nascimento] = input("Digite a data de nascimento: ").strip()
            usuario['cpf'] = input("Digite o CPF: ").strip()
            usuario['email'] = input("Digite o email: ").strip()
            usuario['telefone'] = input("Digite o telefone: ").strip()
            usuario['filme_favorito'] = input("Digite o filme favorito: ").strip()
            
            
           usuarios.append(usuario)
           os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f" Usuário cadastrado com sucesso!")
            continue
        case "2":

    
    
    
    
    
    
    