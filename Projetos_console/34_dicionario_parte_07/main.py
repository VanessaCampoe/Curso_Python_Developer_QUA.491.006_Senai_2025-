usuario = {
    'nome': "Alex Machado",
    'idade': 30,
    'email': "alex.machado@example.com",
}

for chave  in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}") # exibe o dicionario 
print("-" * 20 )

chave = input("Informe a chave que deseja excluir:").lower().strip()
if chave in usuario:
    del usuario[chave]
else:
    print("Chave inexistente")
    print("-" * 20 )
for chave  in usuario :
    print(f"{chave.capitalize()}:{usuario.get(chave)}")