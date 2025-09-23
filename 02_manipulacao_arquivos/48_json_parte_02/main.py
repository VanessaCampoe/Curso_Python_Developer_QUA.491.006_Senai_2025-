import json
import os
pessoa = {}
# primeiro passo e desserializar o json em um dicionario
try:
    arquivo = input("Informe o arquivo :").strip().lower()
    with open(f"{arquivo}.json", "r", encoding='utf-8') as f:
        pessoas = json.load(f)
    # aqui eu vou iterar sobre o dicionario e vou inserir os dados no dicionario pessoa
    # nao fazer o out put da lista do usuario pq esta tarde 
    # usuario informa os dados da pessoas 
    pessoa['nome'] = input("Informe o nome: ").strip().title()
    pessoa['idade'] = int(input("Informe a idade: "))
    pessoa['cpf'] = input("Informe o CPF: ").strip()
    pessoa['rg'] = input("Informe o RG: ").strip()
    pessoa['data_nasc'] = input("Informe a data de nascimento: ").strip().lower()
    pessoa['sexo'] = input("Informe o genero: ").strip().lower()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize
    pessoa['mae'] = input("Informe o signo: ").strip().title()
    pessoa['pai'] = input("Informe o signo: ").strip().title()
    pessoa['email'] = input("Informe o email: ").strip().lower()
    pessoa['senha'] = input("Informe a senha: ")
    pessoa['cep'] = input("Informe o cep: ").strip()
    pessoa['endereço'] = input("Informe o endereço: ").strip().title()
    pessoa['numero'] = input("Informe o numero: ")
    pessoa['bairro'] = input("Informe o bairro: ").strip().title()

    pessoa['cidade'] = input("Informe a cidade: ").    strip().title()
    pessoa['estado'] = input("Informe o estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("Informe o telefone fixo: ").strip()
    pessoa['celular'] = input("Informe o celular: ").strip()
    # aqui eu vou tratar a altura e o peso para que sejam float
    pessoa['altura'] = float(input("Informe a altura: ").strip().replace(',', '.'))
    pessoa['peso'] = float(input("Informe o peso: ").strip().replace(',', '.'))
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguíneo: ").strip().capitalize()
    pessoa['cor'] = input("Informe a cor: ").strip()
    
    # aqui eu vou adicionar a pessoa no dicionario pessoas
    pessoas.append(pessoa) # aqui eu inseri na lista e depois utf 8 vou colocar ele no arquivo json

    # aqui eu vou serializar o dicionario em json e gravar no arquivo
    with open(f"{arquivo}.json", "w", encoding='utf-8') as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)
    # aqui eu vou confirmar que o arquivo foi gravado com sucesso
        # aqui vamos ter q repetir a leitura dojson para verificar se a pessoa foi inserida corretamente, vai ficar no final da lista 
    with open(f"{arquivo}.json", "r", encoding='utf-8') as f:
        pessoa = json.load(f)
        
        print(f"{'-'*20} LISTA DE PESSOA {'-'*20}")
        for p in pessoa:
            for chave in pessoa:
                print(f"{chave.capitalize()}: {pessoa.get(chave)}")
                
            print(f"{'-'*40}\n")
    
except Exception as e:
    print(f"Não foi inserir nova pessoa .{e}.") 
  