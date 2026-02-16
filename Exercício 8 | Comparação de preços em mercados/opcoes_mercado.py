# QUAL MERCADO SAI MAIS BARATO?

#arroz - 0
#carne - 1 
#feijao - 2 
#verduras - 3


dia_a_dia = [18.50, 35.60, 5.99, 45.66]
tatico = [19.69, 34.20, 6.88, 50.89]
primor = [25.44, 31.30, 4.50, 52.10]
soberano = [17.20, 36.50, 9.30, 53.10]
mercadinho_do_vovo = [23.30, 30.40, 6.88, 49.80]

arroz = [8.50,19.69,25.44,17.20,23.30]
carne = [35.60, 34.20, 31.30, 36.50, 30.40]
feijao = [5.99, 6.88, 4.50, 9.30, 6.88 ]
verduras = [45.66, 50.89, 52.10, 53.10, 49.80]


print("Hoje é dia de compras!!! Vamos calcular os preços do mercado mais caro e mais barato!\n")

print(" Mercado Dia-a-dia:\n ARROZ/KG - 18.50R$\n CARNE/KG - 35.60R$\n FEIJÃO/KG 5.99R$\n VERDURAS/KG - 45.66 R$\n\n Mercado Tatico:\n ARROZ/KG - 19.69R$\n CARNE/KG - 34.20R$\n FEIJÃO/KG 6.88R$\n VERDURAS/KG - 50.89R$\n\n Mercado Primor:\n ARROZ/KG - 25.44R$\n CARNE/KG - 31.30R$\n FEIJÃO/KG 4.50R$\n VERDURAS/KG - 52.10R$\n\n Mercado Soberano:\n ARROZ/KG - 17.20R$\n CARNE/KG - 36.50R$\n FEIJÃO/KG 9.30R$\n VERDURAS/KG - 53.10R$\n\n Mercadinho do vovô:\n ARROZ/KG - 23.30R$\n CARNE/KG - 30.40R$\n FEIJÃO/KG - 6.88R$\n VERDURAS/KG - 49.80R$ ")

lista_de_comparacao = []
kg_arroz = round(float(input("\n--Quantos KG de 'arroz' será comprado? ")),2)
kg_carne = round(float(input("\n--Quantos KG de 'carne' será comprado? ")),2)
kg_feijao = round(float(input("\n--Quantos KG de 'feijão' será comprado? ")),2)
kg_verduras = round(float(input("\n--Quantos KG de 'verduras' será comprado? ")),2)

lista_do_mercado = ["Dia-a-Dia", "Tatico", "Primor", "Soberano", "Mercadinho do vovô"]

def comparacao(arroz, carne, feijao, verduras):
    # Dia-a-Dia #################
    resultado_dia_dia = 18.5*(arroz) + 35.6*(carne) + 5.99*(feijao) + 45.66*(verduras)
    lista_de_comparacao.append(resultado_dia_dia)

    resultado_tatico = 19.69*(arroz) + 34.20*(carne) + 6.88*(feijao) + 50.89*(verduras)
    lista_de_comparacao.append(resultado_tatico)

    resultado_primor = 25.44*(arroz) + 31.30*(carne) + 4.50*(feijao) + 52.10*(verduras)
    lista_de_comparacao.append(resultado_primor)

    resultado_soberano = 17.20*(arroz) + 36.50*(carne) + 9.30*(feijao) + 53.10*(verduras)
    lista_de_comparacao.append(resultado_soberano)

    resultado_vovo = 23.30*(arroz) + 30.40*(carne) + 6.88*(feijao) + 49.80*(verduras)
    lista_de_comparacao.append(resultado_vovo)
    return

comparacao(kg_arroz, kg_carne, kg_feijao, kg_verduras)

print(lista_de_comparacao)

mais_barato = min(lista_de_comparacao)
mais_caro = max(lista_de_comparacao)

for x in range (0, 4, 1):
    if mais_barato == lista_de_comparacao[x]:
        mercado = lista_de_comparacao[x]
        print("-- O mercado mais barato é {}".format(lista_do_mercado[x]))
    if mais_caro == lista_de_comparacao[x]:
        mercado_caro = lista_de_comparacao[x]
        print("-- O mercado mais caro é {}".format(lista_do_mercado[x]))