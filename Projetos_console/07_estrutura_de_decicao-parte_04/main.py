nome = input("Informe seu nome:")
idade = int(input("Informe seu idade:"))
#ternario 
result = "È maior de idade ." if idade >= 18 else " é  menor de idade."
# saida
print(f"{nome}{result}")