
# Kaio e situações

print("Poderia me informar sobre a situação que Kaio está? Ajude-me respondendo algumas perguntas utilizando (sim/não):\n")
como_esta_dindin = input("Kaio tem dinheiro? (sim/não): ")
como_esta_saude = input("\nKaio está doente? (sim/não): ")

if como_esta_dindin == "sim" and como_esta_saude == "sim":
    print("\n-- Kaio então decide ir ao hospital particular, para cuidar de sua sáude\n")

elif como_esta_dindin == "não" and como_esta_saude == "sim":
    print("\n-- Kaio então decide ir a upa, para cuidar de sua saúde\n")

elif como_esta_dindin == "sim" and como_esta_saude == "não":
    print("\n-- Kaio decide tomar sorvete e aproveitar seu belo dia\n")

elif como_esta_dindin == "não" and como_esta_saude == "não":
    print("\n-- Kaio decide ficar em casa\n")