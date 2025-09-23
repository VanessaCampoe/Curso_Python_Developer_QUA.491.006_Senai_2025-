nome = input ("Informe seu nome :")
idade = int(input("Informe seu idade :"))
altura = float (input("Informe sua altura:")).replace("," , ".")

print(f" Seja bem vindo ao curso de pynthon,{nome}!")
print(f"Idade do usuario {idade}.")
print(f"Altura do usuario:{altura}")



print(f"{nome}: {type(nome)}.")
print(f"{idade}: {type(idade)}.")
print(f"{altura}: {type(altura)}.")

