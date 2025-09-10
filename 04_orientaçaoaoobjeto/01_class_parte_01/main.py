#classe

class Pessoa:
    #atributos 
    nome = "Alex machado"
    idade = 40 
    telefone = "(61) 98765 4321"
    cpf = "123.456.789-12"
    email= "alex@gmail.com"
    
    
    
    # metodo
    def apresentar(self):
        print(f"ola, meu e {self.nome}, tenho {self.idade} anos, meu telefone e {self.telefone} , meu cpf e { self.cpf} e meu email e {self.email}. ")

# programa principal
if __name__ == "__main__":
    

    # instancia a classe
    usuario = Pessoa()
    # objeto se apresenta 
    usuario.apresentar()
    # o nome da pessoa e um atriburo 
    
# aqui um exepmlo de metodo construtor