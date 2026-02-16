# Organizando lista, string, inteiro, float

lista_doida = ["jacare", 4675.3, "eisten", "kaue", 537, 87.22, "janaina", "saminta", 76, 9.1]

string = 0
inteiro = 0
floats = 0

for x in lista_doida:
    a = type(x)
    if a == str:
        string = string + 1
    elif a == int:
        inteiro = inteiro + 1
    else:
        floats = floats + 1

print("o número dos strings é igual a {}".format(string))
print("o número dos inteiros é igual a {}".format(inteiro))
print("o número dos floats é igual a {}".format(floats))
        

