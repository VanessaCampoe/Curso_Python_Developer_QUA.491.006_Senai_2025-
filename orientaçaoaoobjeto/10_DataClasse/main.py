import Pessoa
def main():
    # instancia a classe Pessoa instancia  usuario e chama o construtor = Pessoa.pessoa
    # instancia e feita pelo construtor
    # contrutor
    usuario = Pessoa.Pessoa(nome="", email="",cpf="",idade=0, altura=0.0)
    # iniciaçlização e esse =0 setando o atributo 

# input 
    usuario.nome = input("Digite seu nome: ").strip().title()
    usuario.email = input("Digite seu email: ").strip().lower()
    usuario.cpf = input("Digite seu CPF: ").strip()
    usuario.idade = int(input("Digite sua idade: "))
    usuario.altura = float(input("Digite sua altura: ").replace(",", "."))
    

# output

    print(usuario)




if __name__ == "__main__":
    main()