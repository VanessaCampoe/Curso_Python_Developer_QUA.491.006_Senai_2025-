nome = input("Informe  seu nome ")
idade = int(input("informe sua idade"))
altura = float(input("informe sua altura em metros: ").replace(",","."))

# estrutura de decição 
# vamos usar o boleano 
if  idade >=12 and altura >= 1.15 :
    print(f"{nome}esta autorizado a entrar ")
else:
    print(f"{nome} não esta autorizado a entrar ")