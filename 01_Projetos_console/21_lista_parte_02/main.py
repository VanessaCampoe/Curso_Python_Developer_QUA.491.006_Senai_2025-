#lista 
nomes = [
    "Alex",
    "Joana",
    "Joao",
    "Marina",
    "Mario",
    "Fernanda"
    ]
for nome in nomes :
    print(nome)
     
novo_nome = input(" Informe o novo nome: ").title().strip()
     #novo nome e inserido na lista 
nomes.append(novo_nome)
     # re-exibo a lista 
for nome in nomes:
    print(nome)