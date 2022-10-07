import random
import time
from random import randint
from time import sleep

print("""
1 - 1 a 10
2 - 1 a 20
3 - 1 a 30
""")

n = int(input())

print(".")
sleep(1)
print("..")
sleep(1)
print("...")
sleep(1)

if n == 1:
	print(random.randint(1, 10))
elif n == 2:
	print(random.randint(1, 20))
elif n == 3:
	print(random.randint(1, 30))
