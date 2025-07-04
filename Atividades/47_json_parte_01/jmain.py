# importaao 
import json 
try: 
    # input 
    arquivo = input("Digite o nome do arquivo JSON: ").strip().lower()
     
     # le o json e deserializa em um dicionario 
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    # imprime o dicionario aqui agora eu nao tenho mais um json e sim um  dicionario e deveo executar como um dicionario 
    
    # output
    print(f"{'--'*20} DADO{'--'*20}")
    for dado in dados:
        for chave in dado:
            print(f"{chave.capitalize()}:{dado[chave]}")
            print(f"{'--'*20} FIM{'--'*20}")
    
except Exception as e :
    print(f"Erro ao importar o módulo json: {e}")
    