# classe  Pessoa:
class Pessoa:
     # construtor 
    def __init__(self, nome, idade, telefone, cpf, email):
         #atributos 
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
    # metodo de ação 
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu email é {self.email}."
    #  so os defs que ficam indentados dentro da class depois if nome e fora da class
    
    
    # algoritimo principal
if __name__ == "__main__":
    # instanciandoa a classe 
    usuario  =  Pessoa(
        nome="",
        idade=0,
        telefone="",
        cpf="",
        email=""
    )
    try: 
        #input
        
        usuario.nome = input("Digite seu nome: ").strip().title()
        usuario.idade = int(input("Digite sua idade: "))
        usuario.telefone = input("Digite seu telefone: ").strip()
        usuario.cpf = input("Digite seu CPF: ").strip()
        usuario.email = input("Digite seu email: ").strip().lower()

    # apresentando os dados do usuário
        print(usuario.apresentar())
    except Exception as e:
        print(f"Ocorreu um erro: {e}")