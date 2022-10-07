import random
from random import randint
from time import sleep

y = 1

print("\n" + '\033[1m' + "	   Bem vindo ao rolador de dados automático!\n" + '\033[0m' + "Escolha a quantidade de números em seu dado para que possa começar.\n\nUse " + '\033[1m' + "s" + '\033[0m' + " para sair.\n\n"'\033[1m' + "1" + '\033[0m' + " - 10\n" + '\033[1m' + "2" + '\033[0m' + " - 20\n" + '\033[1m' + "3" + '\033[0m' + " - 30\n")
while y == 1:
	def cmc():
		n = input("Qual o número do dado que você deseja escolher? ").lower()
		ny = [1, 2, 3]
		
		if n == "1":
			a = random.randint(1, 10)
			sleep(1)
			print(	'\033[1m' + str(a) + '\033[0m')
			quit()
		elif n == "2":
			a = random.randint(1, 20)
			sleep(1)
			print(	'\033[1m' + str(a) + '\033[0m')
			quit()
		elif n == "3":
			a = random.randint(1, 30)
			sleep(1)
			print(	'\033[1m' + str(a) + '\033[0m')
			quit()
		elif n == "s":
			quit()
		elif n != ny:
			print("Coloque um número certo!")
		return ""
		
	print(cmc())
