class Aluno:
    nome = None
    cpf = None
    def __init(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Equipe:
    participantes = []
    projeto = None
    def __init__(self, participantes, projeto):
        self.participantes = []
        self.projeto = projeto

class GerenciadorEquipes:
    def __init__(self):
        EquipesLista = []

    def criarEquipe(self):
        
