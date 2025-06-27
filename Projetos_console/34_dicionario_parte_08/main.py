chaves = ("nome", "idade", "email", "telefone", "profissao")
usuarios = {
chaves[0]: "Alex Machado",
chaves[1]: 30,
chaves[2]: "alex@email.com",
chaves[3]: "1234-5678",
chaves[4]: "Desenvolvedor"

    
}

for chave in chaves :
    print(f"{chave}: {usuarios[chave]}")