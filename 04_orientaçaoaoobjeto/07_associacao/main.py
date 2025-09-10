import CursoClass
import alunoclass




def main():
    #    instanciar as duas classes 
    if __name__ == "__main__":
        # aqueivo curso depois classe curso 
        curso1 = CursoClass.Curso(nome_curso="Python")
        curso2 = CursoClass.Curso(nome_curso="Java")
        
        aluno1 = alunoclass.Aluno(nome_aluno="Alice", matricula="001")
        aluno2 = alunoclass.Aluno(nome_aluno="Bob", matricula="002")
        aluno3 = alunoclass.Aluno(nome_aluno="Charlie", matricula="003")
        aluno4 = alunoclass.Aluno(nome_aluno="David", matricula="004")
        aluno5 = alunoclass.Aluno(nome_aluno="Eva", matricula="005")
        aluno6 = alunoclass.Aluno(nome_aluno="Frank", matricula="006")
        
        
        #  aluno 12345 sao meus objetos e cruso e o meu 
        
        aluno1.inscrever_curso(curso1)
        aluno2.inscrever_curso(curso1)
        aluno3.inscrever_curso(curso1)
        aluno4.inscrever_curso(curso1)

        # inscrever alunos no curso 2
        
        aluno5.inscrever_curso(curso2)
        aluno6.inscrever_curso(curso2)
        
        #  curso e objeoto . mas nome do curso e metodo  ou listar curso ou listar alunos 
        
        # listar cursos do curso 1
        print(f" Cursos do {curso1.nome}:")
        print("Listar  de alunos:")
        for aluno in curso1.listar_alunos():
            print(aluno)
        
        print(f"{'-'*40}")
        
        # listar cursos do curso 2
        print(f" Cursos do {curso2.nome}:")
        print("Listar  de alunos:")
        for aluno in curso2.listar_alunos():
            print(aluno)

if __name__ == "__main__":
    main()
        
        
        

      