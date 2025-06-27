#dicionario 
usuario = {
    'nome': "Alex Machado",
    'idade': 30,
    'email': "alex.machado@example.com",
    'profissão' : "DBA"
}

for chave  in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}") # exibe o dicionario 
    print("-" * 20 )
    
chave = input("Informe a chave que deseja alterar:").lower().strip()
if chave in usuario:
    usuario[chave] = input(f"Informe o valor da chave {chave}:").strip()  
else:
    print("Chave inexistente")
    print("-" * 20 )
for chave in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}")
    
    
    
    
    