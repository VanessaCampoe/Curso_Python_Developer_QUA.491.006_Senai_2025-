#lista de mercado 8 itens 
itens = [
    "maçã",
    "banana",
    "laranja",
    "uva",
    "manga",
    "abacaxi",
    "kiwi",
    "pera"
]
for i in range(len(itens)):
    print(f"Indice {i}:{itens[i]} .")  
    
try:
    i = int(input(" Informe a posição do indice a ser alterado."))
    
    if i <= 0 and i > len(itens):
        itens[i] = input("Informe o novo item: ").strip().lower()
        print(f"Item alterado com sucesso: {itens[i]}.")

    else:
        print("Indice fora do intervalo da lista.")

except Exception as e:
    print(f"Não foi possivel alterar o item.{e}.")
    
    
finally:
    for i in range(len(itens)):
       print(f"Indice {i}:{itens[i]} .")
    
    
        