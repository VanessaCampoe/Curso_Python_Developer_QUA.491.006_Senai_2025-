# super class 
# tipos de encapsulamento  public, protected ,private
class Pessoa:
    def __init__(self,telefone, endereco):
        self.__telefone = telefone # protected 
        self.__endereco = endereco # protected 
        
        
        # # exeplo de protect muda so o anderline 
        #  def __init__(self,telefone, endereco):
        # self.telefone = telefone # public 
        # self._endereco = endereco # protected  
        
        # # exeplo de private muda so o anderline duas vzes 
        #  def __init__(self,telefone, endereco):
        # self.__telefone = telefone # private
        # self._endereco = endereco # protected 
        
        #para mostra os resultados so faz atras dos metodos set e get
        
        # metodo de acesso 
        
        
        
        
        # metododo get telefone  aqui ele nao recebe uma parametro  eele retorna  
        @property
        def telefone(self):
            return self.__telefone
        
        # metodo de telefone 
           # metodo set aqui seria se eu quissesse atribuir um valor  ao atributo telefone

        @telefone.setter
        def telefone(self, telefone ):
            self.__telefone = telefone  #@ private
            
            
        #  em main ele chama o setter  e depois o get pq setei o valor 
        #  ja aqui ele vem primiero o get e depois o set para eledefeinir o valor 
        #
        @property
        def endereco(self):
            return self.__endereco

        @endereco.setter
        def endereco(self, endereco):
            self.__endereco = endereco  #@ private
            
            # sistema de herança 
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(telefone, endereco)
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(telefone, endereco)
        

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            self.__nome = nome

        @property
        def cpf(self):
            return self.__cpf

        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf
        
            #  aqui eu posso faxzer todos os set e todos geter de uma vez e juntos   
class PessoaJuridica(Pessoa):
    # contrutor da classe juridica
    def __init__(self, nome_fantasia, cnpj, telefone, endereco):
        
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        super().__init__(telefone, endereco)

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
