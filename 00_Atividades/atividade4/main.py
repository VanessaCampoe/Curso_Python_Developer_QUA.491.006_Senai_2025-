'''
#TODO - atividade : crie um programa  que mostre a hora atual sempre sendo atualizada a cada segundo .
#NOTE: para intrromper o programa pressione ctrl + c
# '''
import os
import time

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hora atual:", time.strftime("%H:%M:%S"))
    time.sleep(1)
    
    # interromper o programa com ctrl + c
    try:
        pass
    # Pressione CTRL + C para interromper o programa.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário." )
        break