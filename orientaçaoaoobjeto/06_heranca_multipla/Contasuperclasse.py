# super classe 
import InterfaceContasuperclasse 
class Conta (i.InterfaceContasuperclasse): # implementei um interace  () esse i. chamasse alyya
    # construtor 
    def __init__(self, agencia, numero , saldo):
        # atibutos 
        
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        
        
        # set get@
        @ property
        def agencia(self):
            return self.__agencia

        @agencia.setter
        def agencia(self, agencia):
            self.__agencia = agencia

        @property
        def numero(self):
            return self.__numero

        @numero.setter
        def numero(self, numero):
            self.__numero = numero

        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, saldo):
            self.__saldo = saldo
            
            # metodos da interface 
            def exibir_dados(self):
                print(f"Agencia: {self.agencia}")
                print(f"Número da conta : {self.numero}")
                print(f"Saldo: {self.saldo:.2f}")

            def fazer_depositar(self, valor):
                self.saldo += valor
                return self.saldo

            def fazer_saque(self, valor):
                self.saldo -= valor
                return self.saldo
               
              
