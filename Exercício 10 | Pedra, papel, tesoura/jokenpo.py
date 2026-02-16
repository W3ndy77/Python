import random

while True:
    componentes_jogo = ["pedra", "papel", "tesoura"]
    numero_aleatorio = int(3*(random.random()))
    print(numero_aleatorio)

    resultado = componentes_jogo[numero_aleatorio]

    jogador = input("-- Escolha pedra, papel ou tesoura!!!: \n")
    if jogador == resultado:
        print("Empatou, continue o jogo!!!! A máquina também escolheu {}".format(resultado))
        continue
    elif jogador == "pedra" and resultado == "tesoura" or jogador == "tesoura" and resultado == "papel" or jogador == "papel" and resultado == "pedra":
        print("AEEE!!! Você ganhou! A máquina escolheu {}".format(resultado) + " e perdeu!")
        break
    else:
        print("Perdeu!! Mais sorte na próxima! A máquina escolheu {}". format(resultado) + " e venceu!")
        break
