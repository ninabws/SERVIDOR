from re import S, T


class carrinho():
    motor_esquerdo = False
    motor_direito = False

    def parar(self):
        self.motor_direito = False
        self.motor_esquerdo = False

    def frente(self):
        self.motor_direito = True
        self.motor_esquerdo = True

    def tras(self):
        self.motor_direito =True
        