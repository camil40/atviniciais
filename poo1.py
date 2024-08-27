class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def falar(self):
        return("EU ESTOU FALANDO...")
    
aluno = Aluno("Maria","1234","Python")

print(aluno.falar())