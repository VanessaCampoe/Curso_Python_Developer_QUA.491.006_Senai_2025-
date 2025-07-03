import json

try:
    arquivo = input("Digite o nome do arquivo JSON: ").strip().lower()
    with open(f"{arquivo}.json", "r", encoding='utf-8') as f:   
          # aqui eu vou formatar o json para ficar mais legivel
        # aqui eu devo faze o r primeiro pq devo pegar o dados dele preimeiro 
        lista = json.load(f) # ao fazer ate aaqui eu ja tenho uma lista de dicicionario 
    for dado in lista:  # aqui eu vou iterar sobre a lista de dicionario
        dado['altura'] = dado ['altura' ].replace (',', '.')
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])
        
        # serializa o dicionario em json e grava arquivo 
        
    with open(f"{arquivo}.json", "w", encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)   # aqui foi feito a mudando o cod para conv=certar o codigo # aqui eu vou serializar o dicionario em json e gravar no arquivo
        #observacao: o ensure_ascii=False serve para que os caracteres especiais sejam gravados corretamente no arquivo json, e o indent=4 serve para formatar o json de forma mais legivel
        # aqui eu vou serializar o dicionario em json e gravar no arquivo


# confirma que o arquivo foi gravado com sucesso
    print("Conversão gravada com sucesso!")
except Exception as e:
    print(f"Não foi possivel converter  json: {e}")