
# Forma 1
pessoas_legais = ["Joao", "Danielle", "Gabriel", "Leticia", "Castiel"]

salario = ["12.000","10.000","8.000","4.000","20.000"]
 
print("Pessoa chamada {} ".format(pessoas_legais[0]) + "ira receber {}".format(salario[0]))
print("Pessoa chamada {} ".format(pessoas_legais[1]) + "ira receber {}".format(salario[1]))        
print("Pessoa chamada {} ".format(pessoas_legais[2]) + "ira receber {}".format(salario[2]))
print("Pessoa chamada {} ".format(pessoas_legais[3]) + "ira receber {}".format(salario[3]))
print("Pessoa chamada {} ".format(pessoas_legais[4]) + "ira receber {} \n".format(salario[4]))


# Simplificado - Forma 2
for x in range(0, 5, 1):
    print("Legal!! Pessoa chamada {}" .format(pessoas_legais[x]) + " recebeu {}".format(salario[x]))