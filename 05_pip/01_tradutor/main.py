# de qualquer para portugues 

from deep_translator import GoogleTranslator

#  criando uma instancia de uma classe 
def  main():
    
    tradutor = GoogleTranslator(source="auto", target="pt" )

#  auto vai tentar indentidifcar qual o indiomoa 
#  target o idioma para qual o texto vai ser traduzido 
    while True:
        try:
            print("1 - Traduzir texto")
            print("2 - Sair do programa ")
            opcao = input("Informe a opção desejada ")
            match opcao:
                case"1":
                    texto_original = input("Digite  o texto a ser traduzido ")
                    texto_traduzido = tradutor.translate(texto_original)
                    print(F"Texto traduzido :\n{texto_traduzido} ")
                    
                    
                    
                    
                    
                case"2":
                    print("Progrma encerrado .")
                    break
                
                
                
                case _:
                    print("opçao invalida")
                    continue

                
            
    
            
            
            
            
            
        
        except Exception as e:
            print(F"Não foi possivel traduzir. {e}.")
        

if __name__ == "__main__":
    main()
    
