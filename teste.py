import random as rd



def bem_vindo():
    print("""
    ====================BEM VINDO AO IDENTFIND====================
    O JOGO QUE IRÁ DESCOBRIR EM QUAL PERSONAGEM VOCE ESTA PENSANDO
    ==============================================================
                                                creat by: brunovs
    ==============================================================
    """ )

bem_vindo()

try:
    #while True:
        generator = rd.randint(1, 1)
        print(f'Gerador: {generator}')
        
        if generator == 1:
            masculino = input("Seu personagem é Homem?").lower()
            if masculino == "sim":
                real = input("Seu personagem é real?").lower()
                if real == "sim":
                    #[ Alex Sandro, Guga Wag, BatLeo, Elon Musk, Sergio Sacani ]
                    #Descobre o Elon Musk Elon Musk
                    multiM = input("Seu personagem é Multi Milionário?").lower()
                    if multiM == "sim":
                        tesla = input("Seu personagem é dono da Tesla?").lower()
                        if tesla == "sim":
                            spaceX = input("Seu personagem é dono da SpaceX?").lower()
                            if spaceX == "sim":
                                print("Seu personagem é Elon Musk")
                    else: 
                        #[ Alex Sandro, Guga Wag, BatLeo, Sergio Sacani ]
                        professor = input("Seu personagem é Professor?").lower()
                        if professor == "sim":
                            ifpb = input("Seu personagem é do IFPB?").lower()
                            if ifpb == 'sim':
                                #[ Alex Sandro, Guga Wag, BatLeo ]
                                ed = input("Seu personagem é do curso de Estrutura de Dados?").lower()
                                if ed == "sim":
                                    #Descobre o Alex Sandro
                                    print("Seu personagem é Alex Sandro")
                                elif ed == "nao":
                                    so = input("Seu personagem é do curso de Sistemas Operacionais?").lower()
                                    if so == "sim":
                                        #Descobre o Guga Wag
                                        print("Seu personagem é Guga Wag")
                                    elif so == "nao":
                                        #Descobre o BatLeo
                                        print("Seu personagem é BatLeo")
                            else:
                                #Descobre o Sergio Sacani
                                geofisico = input("Seu personagem é Geofísico?").lower()
                                if geofisico == "sim":
                                    youtuber = input("Seu personagem é Youtuber?").lower()
                                    if youtuber == "sim":
                                        print("Seu personagem é Sergio Sacani")
                else:
                    #[ Bob Esponja, patrick Estrela, Pikachu,  Homer, Picapau ]
                    amarelo = input("Seu personagem é Amarelo?").lower()
                    if amarelo == "sim":
                        #[ Bob Esponja, Pikachu ]
                        melhorAmigo = input("Seu personagem é melhor amigo de alguém?").lower()
                        if melhorAmigo == "sim":
                            #[ Bob Esponja, Pikachu ]
                            hamburguer = input("Seu personagem trabalha no Siri Cascudo?").lower()
                            if hamburguer == 'sim':
                                #[ Bob Esponja ]
                                calça = input("Seu personagem usa calça quadrada?").lower()
                                if calça == "sim":
                                    # Descobre o Bob Esponja
                                    print("Seu personagem é Bob Esponja")
                            else:
                                #[ Pikachu ]
                                raio = input("Seu personagem solta raio?").lower()
                                if raio == "sim":
                                    # Descobre o Pikachu
                                    print("Seu personagem é Pikachu")
                                if raio == 'nao':
                                    barriguinha = input("Seu personagem tem uma barriguinha?").lower()
                                    if barriguinha == 'sim':
                                        donut = input("Seu personagem gosta de Donuts?").lower()
                                        if donut == 'sim':
                                            # Descobre o Homer
                                            print("Seu personagem é Homer")
                    else:
                        #[ patrick Estrela, Picapau ]
                        estrela = input("Seu personagem é uma estrela?").lower()
                        if estrela == "sim":
                            #[ patrick Estrela ]
                            rosa = input("Seu personagem é rosa?").lower()
                            if rosa == "sim":
                                #[ patrick Estrela ]
                                amigo = input("Seu personagem é melhor amigo de alguém?").lower()
                                if amigo == "sim":
                                    #[ patrick Estrela ]
                                    bob = input("Seu personagem é melhor amigo do Bob Esponja?").lower()
                                    if bob == "sim":
                                        # Descobre o Patrick Estrela
                                        print("Seu personagem é Patrick Estrela")
                                    elif bob == "nao":
                                        # Descobre o Picapau
                                        print("Seu personagem é Picapau")
                        else:
                            #[ Picapau ]
                            madeira = input("Seu personagem é perfura madeira?").lower()
                            if madeira == "sim":
                                #[ Picapau ]
                                vermelho = input("Seu personagem é vermelho?").lower()
                                if vermelho == "sim":
                                    #[ Picapau ]
                                    frase = input("Seu personagem fala: 'O NENÉM NÃO É NENÉM'?").lower()
                                    if frase == "sim":
                                        # Descobre o Picapau
                                        print("Seu personagem é Picapau")
                                    elif frase == "nao":
                                        forte = input("Seu personagem é forte?").lower()
                                        if forte == "sim":
                                            chifre = input("Seu personagem tem chifres?").lower()
                                            if chifre == "sim":
                                                # Descobre o HellBoy
                                                print("Seu personagem é HellBoy")
        if generator == 2:
            feminino = input("Seu personagem é Mulher?").lower()
            if feminino == "sim":
                print("Seu personagem é Mulher")
except KeyboardInterrupt:
    print("\n\nFim do programa\n\n")
    
    
#criar obejtos para cada personagem


