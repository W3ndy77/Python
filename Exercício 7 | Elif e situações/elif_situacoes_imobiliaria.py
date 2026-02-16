# IMOBILIÁRIA DO DIEGO

print("Seja bem-vindo a imobiliaria Diego's Houses!")
print("Aqui você encontrará muitas casas de bom preço e qualidade, confira agora!\n")

quantos_quartos = input("--Para casas com menos de 2 quartos (Tecle 1):\n--Para casas com mais de 2 quartos (Tecle 2):")
valor_da_entrada = input("\n--Para menos de 35.000R$ (Tecle 1):\n--Para mais de 35.000R$ (Tecle 2): ")
lugar = input ("\n--Casas na Área A (Tecle 1):\n--Casas na Área B (Tecle 2): ")


if quantos_quartos == "2" and valor_da_entrada == "2" and lugar == "1" or quantos_quartos == "2" and valor_da_entrada == "1" and lugar == "1" or quantos_quartos == "1" and valor_da_entrada == "1" and lugar == "1":
    print("Parabéns!!! você ganhou um desconto de 5%!")
elif quantos_quartos == "1" and valor_da_entrada == "2" and lugar == "2" or quantos_quartos == "1" and valor_da_entrada == "1" and lugar == "2":
    print("Parabéns!!! você ganhou um desconto de 6%!")
elif quantos_quartos == "2" and valor_da_entrada == "2" and lugar == "2":
    print("Parabéns!!! você ganhou um desconto de 3%!")
elif quantos_quartos == "2" and valor_da_entrada == "1" and lugar == "2":
    print("Parabéns!!! você ganhou um desconto de 15%!")
elif quantos_quartos == "1" and valor_da_entrada == "2" and lugar == "1":
    print("Parabéns!!! você ganhou um desconto de 7%!")