
from dataclasses import dataclass

#  aqi por ser um super data classe nem toda pessoa tem nome 
#  bloquear a classe pessoa e nao instaciar a classe pessoa 

@dataclass
class Pessoa:
    email: str
    telefone: str 
    endereco: str
    
    #  pyt abstrada e interface no pythom e a mesma coisa
    @abstractmetho
    def __str__(self):
        pass