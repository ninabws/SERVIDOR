import random

class aleat():
    a= random.seed(0) #gerador de números pseudoaleatórios, fazendo o começar em um ponto arbitrário em sua sequência aleatória.
    b= random.randrange(1, 6) #gera aleatoriamente um número inteiro dentro de um intervalo dado pelo usuário.
    c= random.randint(1,2) #gera aleatoriamente um número inteiro dentro de um intervalo dado pelo usuário.
    d= random.choice(1,2,3,4,5) #retorna um elemento da sequência sorteada.
    e= random.shuffle(1,2,3,4,5) #usado para embaralhar uma sequência.
    f= random.sample(1,10) #retorna uma lista de comprimento particular de itens escolhidos da sequência.
    g= random() #módulo utilizado para gerar números pseudo-aleatórios.

    def __init__ (self, a, b, c, d, e, f, g):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g

e = aleat()
print(e.a, e.b, e.c)


