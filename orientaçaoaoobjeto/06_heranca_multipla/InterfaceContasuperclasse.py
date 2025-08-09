from abc import ABC
from abc import abstractmethod
# interface 
class InterfaceContasuperclasse(ABC):
    @abstractmethod
    def exibir_dados(self):
        pass
#set get

    @abstractmethod
    def fazer_depositar(self, valor):
        pass

    @abstractmethod
    def fazer_saque(self, valor):
        pass