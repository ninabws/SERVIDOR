from tokenize import Double


class Conta_Bancaria():
    nome_do_correntista = ''
    saldo = 0
    conta_premium = False

    def depositar(self):
        self.saldo = 1000
    def retirar(self):
        self.saldo = 200
    def mostrar_dados(self):
        self.nome_do_correntista = 'Julia'
        self.saldo = 100000
        self.conta_premium = True

e = Conta_Bancaria()
e.depositar()
e.retirar()
e.mostrar_dados()
print(e.mostrar_dados)
print(type(e))
        