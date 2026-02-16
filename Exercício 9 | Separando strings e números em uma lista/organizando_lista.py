# SEPARANDO NÚMEROS E STRINGS EM UMA LISTA

listinha = ["casa", "mercado", 3, "carro", 9, 7] # antes da organização

lista_dos_strings = []
lista_de_numero = []

for x in listinha:
    elemento = type(x)
    if elemento == str:
        lista_dos_strings.append(x)
    else:
        lista_de_numero.append(x)

print(lista_dos_strings) # lista de strings que estavam na lista
print(lista_de_numero) # lista de números que estavam na lista