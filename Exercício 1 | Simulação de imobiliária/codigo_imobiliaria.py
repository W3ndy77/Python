#codigo_imobiliaria ######

print("Seja bem-vindo a imobiliaria Lar Doce Lar!\n")
print("Aqui você encontrara as melhores casas e apartamentos a venda! E tudo isso com preços que cabem no seu bolso!\n")
print("Venha ja conferir! Somos os mais vendidos de todo estado!")

tipo_de_imobiliaria = input("\n Se deseja conferir casas (Tecle 1): \n Se deseja conferir apartamentos (Tecle 2): \n Se deseja consultar com um dos nossos atendentes (Tecle 3): ")

if tipo_de_imobiliaria == "1" or tipo_de_imobiliaria == "2" or tipo_de_imobiliaria == "3":
    print("Opção selecionada! Carregando...")

   #quando for tipo CASAS ###########
    if tipo_de_imobiliaria == "1":
        tipo_de_casa = input ("\n Se deseja conferir casas com 1 quarto (Tecle 1): \n Se deseja conferir casas com 2 quartos (Tecle 2): \n Se deseja conferir casas com 3 quartos ou mais (Tecle 3): ")
 
      #CASAS BLOCO 1 ######
        if tipo_de_casa == "1":
            print("Casas com 1 quarto! Pesquisando localidades...")
            print("Selecione locais que deseja visualizar:")
            #LOCAL DA CASA
            if tipo_de_casa == "1" or tipo_de_casa == "2" or tipo_de_casa == "3":
                local_c = input("\n Santo Antônio do Descoberto (Tecle 1): \n Águas Lindas (Tecle 2): \n Taguatinga (Tecle 3): \n Samambaia (Tecle 4): \n Alexania (Tecle 5): ")
                print("Confira as casas a venda neste local!" )
      # CASAS BLOCO 2 ###
        if tipo_de_casa == "2":
            print("Casas com 2 quartos! Pesquisando localidades...")
            print("Selecione locais que deseja visualizar:")
            #LOCAL DA CASA
            if tipo_de_casa == "1" or tipo_de_casa == "2" or tipo_de_casa == "3":
                local_c = input("\n Santo Antônio do Descoberto (Tecle 1): \n Águas Lindas (Tecle 2): \n Taguatinga (Tecle 3): \n Samambaia (Tecle 4): \n Alexania (Tecle 5): ")
                print("Confira as casas a venda neste local!" )
          # CASAS BLOCO 3 ###
        if tipo_de_casa == "3":
            print("Casas com 3 quartos ou mais! Pesquisando localidades...")
            print("Selecione locais que deseja visualizar:")
            #LOCAL DA CASA
            if tipo_de_casa == "1" or tipo_de_casa == "2" or tipo_de_casa == "3":
                local_c = input("\n Santo Antônio do Descoberto (Tecle 1): \n Águas Lindas (Tecle 2): \n Taguatinga (Tecle 3): \n Samambaia (Tecle 4): \n Alexania (Tecle 5): ")
                print("Confira as casas a venda neste local!" )

#### fim das opções de casas #####


#### quando for tipo APARTAMENTOS ######
    if tipo_de_imobiliaria == "2":
        tipo_de_apartamento = input ("\n Se deseja conferir apartamentos com 1 quarto (Tecle 1): \n Se deseja apartamentos casas com 2 quartos (Tecle 2): \n Se deseja conferir apartamentos com 3 quartos ou mais (Tecle 3): ")
   
#APARTAMENTOS BLOCO 1 #######
        if tipo_de_apartamento == "1":
            print("Apartamentos com 1 quarto! Pesquisando localidades...")
            print("Selecione locais que deseja visualizar:")
            #LOCAL DO APARTAMENTO
            if tipo_de_apartamento == "1" or tipo_de_apartamento == "2" or tipo_de_apartamento == "3":
                local_ap = input("\n Santo Antônio do Descoberto (Tecle 1): \n Águas Lindas (Tecle 2): \n Taguatinga (Tecle 3): \n Samambaia (Tecle 4): \n Alexania (Tecle 5): ")
                print("Confira as casas a venda neste local!" )
   
#APARTAMENTOS BLOCO 2 ######
        if tipo_de_apartamento == "2":
            print("Apartamentos com 2 quartos! Pesquisando localidades...")
            print("Selecione locais que deseja visualizar:")
            #LOCAL DO APARTAMENTO
            if tipo_de_apartamento == "1" or tipo_de_apartamento == "2" or tipo_de_apartamento == "3":
                local_ap = input("\n Santo Antônio do Descoberto (Tecle 1): \n Águas Lindas (Tecle 2): \n Taguatinga (Tecle 3): \n Samambaia (Tecle 4): \n Alexania (Tecle 5): ")
                print("Confira as casas a venda neste local!" )
  
#APARTAMENTOS BLOCO 3 ######
        if tipo_de_apartamento == "3":
            print("Apartamentos com 3 quartos ou mais! Pesquisando localidades...")
            print("Selecione locais que deseja visualizar:")
            #LOCAL DO APARTAMENTO
            if tipo_de_apartamento == "1" or tipo_de_apartamento == "2" or tipo_de_apartamento == "3":
                local_ap = input("\n Santo Antônio do Descoberto (Tecle 1): \n Águas Lindas (Tecle 2): \n Taguatinga (Tecle 3): \n Samambaia (Tecle 4): \n Alexania (Tecle 5): ")
                print("Confira as casas a venda neste local!" )

#fim das opções de apartamentos ######


#quando tipo ATENDENTES #####
    if tipo_de_imobiliaria == "3":
        print ("Aguarde até um dos nossos atendentes estarem disponíveis...")