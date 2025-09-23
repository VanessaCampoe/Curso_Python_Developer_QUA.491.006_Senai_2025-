#lista
cidade = [
    "Brasilia",
    "São Paulo",
    "Rio De Janeiro",
    "Teresina",
    "Belo Horizonte",
    "Palmas",
    "Fortaleza",
    "Salvador",
    "Recife", 
    "São Paulo",
    "Rio De Janeiro",  
    "Curitiba",
    "Porto Alegre",
    "Manaus",
    "Brasilia",
    "Rio De Janeiro",
    "Brasilia"
]
# Usuario informa o nome da cidade a ser psquisada
cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").title().strip()  # mudar tudo e colocar o lower para testar se funciona

# programa infroma  o nome da cidade ser pesquisada 
qtde = cidade.count(cidade_pesquisada)
# prama indica quantas vezes o titem foi encontrado 

print(f"A cidade {cidade_pesquisada } foi encontrada {qtde} vezes na lista.")
