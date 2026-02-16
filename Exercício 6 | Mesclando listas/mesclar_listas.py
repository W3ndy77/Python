

grupo_1 = ["julia","lucas","pedro","william"]
print("\nPessoas do grupo 1:")
print(grupo_1)
grupo_2 = ["fernando","heitor","lucas","thalita"]
print("\nPessoas do grupo 2:")
print(grupo_2)
novo_grupo =[]
novo_grupo = set(grupo_1 + grupo_2) # set além de mesclar listas impede que itens repetidos que estão em ambas listas, como a palavra lucas, não se repitam na nova lista

print("\nUma nova união foi feita! Grupo 1 e Grupo 2:")
print(novo_grupo)