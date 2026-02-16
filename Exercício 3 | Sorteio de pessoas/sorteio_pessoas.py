import random

pessoas_sorteio = ["Bruno","Lucio","André","Ayla","Cristiane"]

numero = int(4*random.random())
if numero <4:
    parabenizado = pessoas_sorteio[numero]
    print("Parabéns!! {}". format(parabenizado) + " foi contemplado(a) com 5 centavos!!!\n")
print("Número sorteado:")
print(numero)