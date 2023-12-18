# import random as rd



# def bem_vindo():
#     print("""
#     ====================BEM VINDO AO IDENTFIND====================
#     O JOGO QUE IRÁ DESCOBRIR EM QUAL PERSONAGEM VOCE ESTA PENSANDO
#     ==============================================================
#                                                 creat by: brunovs
#     ==============================================================
#     """ )

# bem_vindo()

# try:
#     #while True:
#         generator = rd.randint(1, 1)
#         print(f'Gerador: {generator}')
        
#         if generator == 1:
#             masculino = input("Seu personagem é Homem?").lower()
#             if masculino == "sim":
#                 real = input("Seu personagem é real?").lower()
#                 if real == "sim":
#                     #[ Alex Sandro, Guga Wag, BatLeo, Elon Musk, Sergio Sacani ]
#                     #Descobre o Elon Musk Elon Musk
#                     multiM = input("Seu personagem é Multi Milionário?").lower()
#                     if multiM == "sim":
#                         tesla = input("Seu personagem é dono da Tesla?").lower()
#                         if tesla == "sim":
#                             spaceX = input("Seu personagem é dono da SpaceX?").lower()
#                             if spaceX == "sim":
#                                 print("Seu personagem é Elon Musk")
#                     else: 
#                         #[ Alex Sandro, Guga Wag, BatLeo, Sergio Sacani ]
#                         professor = input("Seu personagem é Professor?").lower()
#                         if professor == "sim":
#                             ifpb = input("Seu personagem é do IFPB?").lower()
#                             if ifpb == 'sim':
#                                 #[ Alex Sandro, Guga Wag, BatLeo ]
#                                 ed = input("Seu personagem é do curso de Estrutura de Dados?").lower()
#                                 if ed == "sim":
#                                     #Descobre o Alex Sandro
#                                     print("Seu personagem é Alex Sandro")
#                                 elif ed == "nao":
#                                     so = input("Seu personagem é do curso de Sistemas Operacionais?").lower()
#                                     if so == "sim":
#                                         #Descobre o Guga Wag
#                                         print("Seu personagem é Guga Wag")
#                                     elif so == "nao":
#                                         #Descobre o BatLeo
#                                         print("Seu personagem é BatLeo")
#                             else:
#                                 #Descobre o Sergio Sacani
#                                 geofisico = input("Seu personagem é Geofísico?").lower()
#                                 if geofisico == "sim":
#                                     youtuber = input("Seu personagem é Youtuber?").lower()
#                                     if youtuber == "sim":
#                                         print("Seu personagem é Sergio Sacani")
#                 else:
#                     #[ Bob Esponja, patrick Estrela, Pikachu,  Homer, Picapau ]
#                     amarelo = input("Seu personagem é Amarelo?").lower()
#                     if amarelo == "sim":
#                         #[ Bob Esponja, Pikachu ]
#                         melhorAmigo = input("Seu personagem é melhor amigo de alguém?").lower()
#                         if melhorAmigo == "sim":
#                             #[ Bob Esponja, Pikachu ]
#                             hamburguer = input("Seu personagem trabalha no Siri Cascudo?").lower()
#                             if hamburguer == 'sim':
#                                 #[ Bob Esponja ]
#                                 calça = input("Seu personagem usa calça quadrada?").lower()
#                                 if calça == "sim":
#                                     # Descobre o Bob Esponja
#                                     print("Seu personagem é Bob Esponja")
#                             else:
#                                 #[ Pikachu ]
#                                 raio = input("Seu personagem solta raio?").lower()
#                                 if raio == "sim":
#                                     # Descobre o Pikachu
#                                     print("Seu personagem é Pikachu")
#                                 if raio == 'nao':
#                                     barriguinha = input("Seu personagem tem uma barriguinha?").lower()
#                                     if barriguinha == 'sim':
#                                         donut = input("Seu personagem gosta de Donuts?").lower()
#                                         if donut == 'sim':
#                                             # Descobre o Homer
#                                             print("Seu personagem é Homer")
#                     else:
#                         #[ patrick Estrela, Picapau ]
#                         estrela = input("Seu personagem é uma estrela?").lower()
#                         if estrela == "sim":
#                             #[ patrick Estrela ]
#                             rosa = input("Seu personagem é rosa?").lower()
#                             if rosa == "sim":
#                                 #[ patrick Estrela ]
#                                 amigo = input("Seu personagem é melhor amigo de alguém?").lower()
#                                 if amigo == "sim":
#                                     #[ patrick Estrela ]
#                                     bob = input("Seu personagem é melhor amigo do Bob Esponja?").lower()
#                                     if bob == "sim":
#                                         # Descobre o Patrick Estrela
#                                         print("Seu personagem é Patrick Estrela")
#                                     elif bob == "nao":
#                                         # Descobre o Picapau
#                                         print("Seu personagem é Picapau")
#                         else:
#                             #[ Picapau ]
#                             madeira = input("Seu personagem é perfura madeira?").lower()
#                             if madeira == "sim":
#                                 #[ Picapau ]
#                                 vermelho = input("Seu personagem é vermelho?").lower()
#                                 if vermelho == "sim":
#                                     #[ Picapau ]
#                                     frase = input("Seu personagem fala: 'O NENÉM NÃO É NENÉM'?").lower()
#                                     if frase == "sim":
#                                         # Descobre o Picapau
#                                         print("Seu personagem é Picapau")
#                                     elif frase == "nao":
#                                         forte = input("Seu personagem é forte?").lower()
#                                         if forte == "sim":
#                                             chifre = input("Seu personagem tem chifres?").lower()
#                                             if chifre == "sim":
#                                                 # Descobre o HellBoy
#                                                 print("Seu personagem é HellBoy")
#         if generator == 2:
#             feminino = input("Seu personagem é Mulher?").lower()
#             if feminino == "sim":
#                 print("Seu personagem é Mulher")
# except KeyboardInterrupt:
#     print("\n\nFim do programa\n\n")
    
    
# #criar obejtos para cada personagem


# t = "Eu sou Bruno1"
# a = t.split()
# print(a)
# x = a[len(a) - 1]
# print(x[:-1])

# meudict = {"Alex Sandro": ["Homem", "Real", "Professor", "IFPB", "Estutura de Dados"],
#         "Guga Wag": ["Homem", "Real", "Professor", "IFPB", "Sistemas Operacionais",],
#         "BatLeo": ["Homem", "Real", "Professor", "IFPB", "Protocolos"]}

# Dicionário de exemplo


# Array de valores
# valores = ["Real", "IFPB", "Homem", "Professor", "Estutura de Dados"]

# for i in range (len(valores)):
#     for chave, val in meudict.items():
#         if sorted(val) == sorted(valores):
#             print(f'O valor {valores} está associado à chave {chave}')
#             break
#     else:
#         print(f'O valor {valores} não está presente como valor no dicionário')

# valores = ["Real", "IFPB", "Homem", "Professor", "Estrutura de Dados"]

# meudict = {
#     "chave1": ["Real", "IFPB", "Homem", "Professor", "Estrutura de Dados"],
#     "chave2": ["Professor", "Estrutura de Dados"],
#     "chave3": ["Outros", "Valores", "Aqui"]
# }

# # Convertendo os valores para um conjunto para verificação mais eficiente
# valores_set = set(valores)

# for chave, val in meudict.items():
#     if set(val) == valores_set:
#         print(f'O conjunto de valores {valores} está associado à chave {chave}')
#         break
# else:
#     print(f'O conjunto de valores {valores} não está presente como valores em nenhuma chave do dicionário')

    

# valores = ["Real", "IFPB", "Homem", "Professor", "Estrutura de Dados"]

# meudict = {
#     "chave1": ["Real", "IFPB", "Homem"],
#     "chave2": ["Professor", "Estrutura de Dados"],
#     "chave3": ["Outros", "Valores", "Aqui"]
# }

# for valor in valores:
#     encontrado = False
#     for chave, val in meudict.items():
#         if valor in val:
#             print(f'O valor {valor} está associado à chave {chave}')
#             encontrado = True
#             break
#     if not encontrado:
#         print(f'O valor {valor} não está presente como valor em nenhuma chave do dicionário')

## TESTE TRUE ##

# valores = ["Real", "IFPB", "Homem", "Professor", "Estrutura de Dados", "teste1", "teste2"]

# meudict = {
#     "chave1": ["Real", "IFPB", "Homem"],
#     "chave2": ["Aluno", "Estrutura de Dados"],
#     "chave3": ["Outros", "Valores", "Aqui"]
# }

# valores_set = set(valores)

# encontrado = False
# for chave, val in meudict.items():
#     if valores_set.issubset(set(val)):
#         print(f'O conjunto de issubset {valores} está associado à chave {chave}')
#         encontrado = True
#         break

# if not encontrado:
#     print(f'O conjunto de valores {valores} não está presente como valores em nenhuma chave do dicionário')




# meudict = {"Alex Sandro": ["Homem", "Real", "Professor", "IFPB", "Estutura de Dados"],
#         "Guga Wag": ["Homem", "Real", "Professor", "IFPB", "Sistemas Operacionais",],
#         "BatLeo": ["Homem", "Real", "Professor", "IFPB", "Protocolos"]}

# # Array de valores
# valores = ["Real", "IFPB", "Homem", "Professor", "Estutura de Dados", "teste1", "teste2"]

# for i in range (len(valores)):
#     # meus_personagens = self.__personagens()
#     for chave, val in meudict.items():
#         if set(val).issubset(set(valores)):
#             print(f'O valor {valores} está associado à chave {chave}')
#             break
#         else:
#             print(f'O valor {valores} não está presente como valor no dicionário')
#     break

lista = [1,2,3]
texto = 
print(lista, '\nalgo\n')