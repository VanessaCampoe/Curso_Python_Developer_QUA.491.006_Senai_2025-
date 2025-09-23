usuario = {
    'nome': "Alex Machado",
    'idade': 30,
    'email': "alex.machado@example.com",
   
}
 
for chave  in usuario:
     print(f"{chave.capitalize()}:{usuario.get(chave)}") # exibe o dicionario 
     print("-" * 20 )
     usuario['profissao'] = input("Digite a profissão").strip()
     
     print("-" * 20 )