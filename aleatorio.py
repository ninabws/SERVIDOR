import math

class aleatorio():
    a= 0

    def random_function(self, a):
        return math.sin(2* 3.14*a + 1)
        
    def sorteia(self):
        n = self.random_function(self.a)
        self.a = n
        return n

e = aleatorio()
print(e.sorteia())
print(e.sorteia())
print(e.sorteia())