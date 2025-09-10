import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    cnpj: str
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        return f"Razão Social: {self.razao_social}, Nome Fantasia: {self.nome_fantasia}, CNPJ: {self.cnpj}, E-mail: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"
