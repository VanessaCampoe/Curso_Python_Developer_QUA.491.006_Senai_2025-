usuarios = [
    {
    'nome': "Alex Machado",
    'idade': 30,
    'email': "alex.machado@example.com",
},
{ 
 "nome": "Alex Machado", "idade": 30, "email": "fulano@gmail.com"
 
 
 },
{ "nome": "Alex Machado", "idade": 30, "email": "ciclano"
 
 
 }
 
]
#exibir dados 
for usuario in usuarios:
    
    print("-" * 20 )
    for chave in usuario:
        print(f"{chave.capitalize()}:{usuario.get(chave)}")