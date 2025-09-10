import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaFisica(Pessoa.Pessoa):
    nome: str
    cpf: str
    idade: int
    
    def __str__(self):
        return f"Nome: {self.nome},  Idade: {len(self)}, CPF: {self.cpf}"
    
    def __len__(self):
        return self.idade