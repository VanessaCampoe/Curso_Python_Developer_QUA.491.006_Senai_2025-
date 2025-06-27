#dicionario
usuario = dict(nome = "Alex machado", idade = 40, email = "alex.machado@example.com")

for chave in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}")