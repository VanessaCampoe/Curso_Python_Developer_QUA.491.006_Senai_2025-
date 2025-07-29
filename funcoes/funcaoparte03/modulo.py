
# import modulo  buscar por alyas 

import modulo as m 
#  aqui foi feito o import os depois tirado quando lancei na funçai 


# algoritomos  principal 


if __name__ == "__main__":
    #  bloquear e manter a integridade do  arquivo ele bloquea o import do modulo e nao o main
    
    while True:
        
        print("1 - Calculadora quadrada .")
        print("2 - Calculadora retangulo ")
        print("3 - Calculadora triangulo.")
        print("4 - sair do programa ")
        opcao = input ("iforme a opcao desejada :").strip()
        m.limpar_tela() 
        match opcao:
            
            
            case"1":
                
                try:
                    1 = int(input("Informe o lado do quadrodo:"))
                    a = m.area_quadrado(1)
                    
                    print(f"Area do quadrado:{e}.")
                except Exception as e:
                    print(f"Erro.{e}.")
                finally:
                    continue
                
                
            case"2":
                try:
                    b = int(input("Informe a base do retangulo:"))
                    h = int(input("Informe a altura do retangulo:"))
                    a = m.area_retangulo(b, h)
                    print(f"Area do retangulo .{a}.")
                    
                except Exception as e:
                    print(f"Erro.{e}.")
                finally:
                    continue
                
            case"3":
                try:
                    b = int(input("Informe a base do retangulo:"))
                    h = int(input("Informe a altura do retangulo:"))
                    a = m.area_retangulo(b, h)
                    print(f"Area do retangulo .{a}.") 
                    
                
                except Exception as e:
                    print(f"Erro.{e}.")
                finally:
                    continue
            case"4":
                print("Prongrama encerrado.")
                
                
            case"_":
                print("Opção invalida.")
                continue 
     