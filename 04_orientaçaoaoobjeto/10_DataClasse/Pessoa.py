# importa o detaclass 
from dataclasses import dataclass

#  classe Pessoa 
@dataclass
#  aqui eu ia criar meu contrutor , mas agora nao mais 
class Pessoa:
    #  atributos 
    nome: str
    email: str
    cpf: str
    idade: int
    altura: float
    
    # metodo srting
    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nCPF: {self.cpf}\nIdade: {self.idade}\nAltura: {self.altura}"

    def __len__(self):
        return len(self.idade) # metodo para retornar metodo inteiro 
