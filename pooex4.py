class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def Estudar(self, horasDeEstudo):
        return horasDeEstudo + self.tempoSemDormir
    
    def Dormir(self, horasDeSono):
        return horasDeSono - self.tempoSemDormir
    
aluno = Aluno("Maria", "Python", 12)
print(aluno.Estudar(4), aluno.Dormir(8))