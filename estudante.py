class Estudante: 
    nome = ''
    nota = 0
    curso = ''
    bolsista = False 

    def __init__(self, nome, nota, curso):
        self.nome = nome
        self.nota = nota
        self.curso = curso



    def dar_bolsa(self):
        self.bolsista = True

e = Estudante(input("Nome: "), input("Nota: "), input("Curso: "))
e.dar_bolsa()
print(e.nome, e.nota, e.curso) 
print(type(e))
