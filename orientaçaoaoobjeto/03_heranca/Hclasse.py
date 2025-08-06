# superclasse  ou classe_pai
#tem atributos e metodos que seram chamados 
class Pessoa:     # toda class e maiouscula 
    
    # construtor
    #  aqui e como se ele colocasee o herença por ser os memos atributos income=um com a pessoa juridica e fisica 
    # fconstrutor onde fica os dados em comum 
    def __init__(self, telefone,endereco ):
        self.telefone = telefone
        self.endreco = endereco 
       
       
       # metodo poliformismo  
    def exibir_dados(self):
        print(f"Telefone:{self.telefone}")
        print(f"Endereço:{self.endereco }")
        
        
        # subclasse ou classe_filha
class PessoaFisica(Pessoa):
    # construtor da class fisica 
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(telefone, endereco)
        
        
        
    # aqui e uma açao um print na tela 
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()
        
    #  se eu colocar um atributo depois de endereço ele vai ficar depoisod pusper 
            
            
            
            
class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, telefone, endereco):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(telefone, endereco)

    def exibir_dados(self):
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()
            
            
#  estudar data class  opção que nao precisa fazer a herança ou
