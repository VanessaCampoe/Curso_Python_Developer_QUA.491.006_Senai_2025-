class Pessoa:
    # construtor iniciar o contrutor 
    #  funcina com encapsuamento mas vamos fazer sem para nao perder tempo e deic=xar so os metodos especiais 
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def __str__(self):
        return f"Olá meu nome é : {self.nome}\nidade: {len(self)} anos."

    def __len__(self):
        return self.idade
    
    #  o len so retorna se for int e so posso usar em um atributo int 
    def __del__(self):
        print(f"Objeto {self.nome} foi destruído.")