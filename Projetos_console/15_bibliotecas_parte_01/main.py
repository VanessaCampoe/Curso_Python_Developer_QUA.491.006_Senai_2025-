# importação de biblioteca
import os 
while True:
    nome = input(" Informe seu nome:")
    os.system("cls")
    print(f"Seja bem vindo(a), {nome}!")
    
    proesseguir = input ("Deseja inserir outro nome? (s/n)").lower().strip()
    
    match proesseguir:
        case "s": 
            os.system("cls")
            continue
        case "n":
            break
        case _:
            print("Opção invalida")
            break
        