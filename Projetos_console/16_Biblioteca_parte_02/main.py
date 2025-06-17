# importar bibliotecas devo importar em cada progama nao basta esta na pasta tem q importar novamente 
import os 
import time  

try:
    
    n = int(input("Informe um numero inteiro :"))
    while n >= 0:
        os.system("cls")
        print(f"{n}...")
        time.sleep(1)
        n -= 1
        
    
    
    
    
except Exception as e:
    print(f"Não foi possivel executar a contagem . {e}.")

finally:
    os.system("cls")
    print("BOOOOOMMMMMMMMM!!!!!!!!!!!!")