class Curso:
    def __init__(self, nome_curso):
        self.nome = nome_curso
        self.alunos_inscritos = []

    @property
    def nome_curso(self):
        return self.__nome_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)

    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)
        return lista

"""class Curso:
    # definindo meu construtor 
    def __init__(self, nome_curso):
        self.nome = nome_curso
        self.alunos_inscritos = []  # pq um obejto nao tem so um valor tem varios uma lista da classe aluno
#  a lista estra como atributo
# definir o seter e gert 

    @property
    def nome_curso(self):
        return self.__nome_curso # aqui tem erturn pq estou pegando o valor ja o set nao 

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso
       
        

        #  definir metodos 
        # metodos de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)   # aqui 
            #aluno.inscrever_curso(self) # associa o curso ao aluno 
            
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome_aluno)
        return lista"""
                
         
