"""
    # TODO -  Atividade :crie um  programa que calcule a area e a circunferencia de um circulo
    #NOTE -  - Use lambda 

"""
import os
import math
# funcao lambda para calcular a area do circulo
#limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#area_circulo = lambda r: 3.14 * r ** 2
area_circulo = lambda r: math.pi * r ** 2
# funcao lambda para calcular a circunferencia do circulo
circunferencia_circulo = lambda r: 2 * math.pi * r
if __name__ == "__main__":
    try:
            r = int(float(input("Informe o valor do raio: ")))
            area = area_circulo(r)
            circunferencia = circunferencia_circulo(r)
            #limpar()

            print(f"A área do círculo é: {area}")
            print(f"A circunferência do círculo é: {circunferencia}")
    except Exception as e:
        print (f" nao e possivel somar. {e}")
