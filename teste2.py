import random as rd
import os
from pilha import Pilha
#HASHTABLE AQUI? OU DENTRO DO OBJETO "IDENTFIND"

class IdentFind:
    #inicia o Objeto
    def __init__(self) -> None:
        #quantidade de rodadas
        self.__rodadas = 0
        #lista de caracteristicas do personagem do usuario
        self.__personagemUser = []
        #pergunta atual
        self.__pergunta_vez = None
        self.__jogo_em_andamento = False

    def iniciar(self):
        if self.__jogo_em_andamento: 
            raise Exception("Jogo já iniciado")
        self.__jogo_em_andamento = True
            
        self.__lista_perguntas = self.__perguntas()
        while len(self.__personagemUser) != 4 :  # Limitando a 4 rodadas 
            try: 
                print("\nRodada -> ", self.__numeroRodadas())
                gera_pergunta = self.__random_quest(self.__lista_perguntas)
                pergunta_atual = self.__lista_perguntas[gera_pergunta]
                self.__empilhaPergunta(pergunta_atual)
                print(pergunta_atual)
                resposta = input("Responda 'sim' ou 'nao': ").lower()

                if resposta == 'sim':
                    # Acessa personagens relacionados à pergunta atual
                    # personagens_restantes = [p for p in self.__lista_personagens if p != '']
                    # self.__lista_personagens = personagens_restantes
                    quebra_perg = pergunta_atual.split()
                    quebra_perg = quebra_perg[len(quebra_perg) - 1]
                    self.__personagemUser.append(quebra_perg[:-1]) if quebra_perg[:-1] not in self.__personagemUser else None
                    # REMOVER PERGUNTA QUE JA FOI RESPONDIDA SIM #
                    
                    print(self.__personagemUser)
                    self.__limpaTerminal()
                    #return self.__personagemUser
                    ...
                elif resposta == 'nao':
                    # Remove personagens relacionados à pergunta atual
                    # self.__lista_personagens[pergunta_atual] = ''
                    # personagens_restantes = [p for p in self.__lista_personagens if p != '']
                    
                    #se disser que nao para uma pergunta antes sim, remove do array
                    quebra_perg = pergunta_atual.split()
                    quebra_perg = quebra_perg[len(quebra_perg) - 1]
                    self.__personagemUser.remove(quebra_perg[:-1]) if quebra_perg[:-1] in self.__personagemUser else None
                    #FAZER COM QUE A PERGUNTA NAO SEJA FEITA NOVAMENTE
                    print(self.__personagemUser)
                    self.__limpaTerminal()
        #REMOVER ESSE PRINT           
                else:
                    print("Resposta inválida")
                    continue
                #print("Seu personagem é:", self.__encontraPersonagem(self.__personagemUser),"\nRodadas -> ", self.__numeroRodadas())
                    
            except IndexError:
                print("Acabaram as perguntas")
                continue
            except KeyboardInterrupt:
                print("Programa encerrado")
                break
        
    def __perguntas(self):
        return [
            "Seu personagem é Homem?",
            "Seu personagem é Real?",
            "Seu personagem é Professor?",
            "Seu personagem é Professor do IFPB?",
            "Seu personagem é Professor de Estrutura de Dados?",
            "Seu personagem é Professor de Estrutura de Operacionais?",
            "Seu personagem é Professor de Protocolos?",
            "Seu personagem é melhor amigo do Patrick Estrela?",
            "Seu personagem é melhor amigo do Bob Esponja?",
            "Seu personagem faz parte de algum Desenho?",
            "Seu personagem é Amarelo?",
            "Seu personagem trabalha no Siri Cascudo?",
            "Seu personagem é uma Estrela do Mar?",
            "Seu personagem é melhor amigo do Ash?",
            "Seu personagem é Rosa?",
            "Seu personagem é um Pokemon?",
        ]

    def __personagens(self):
        map = {
            "Alex Sandro": ["Homem", "Real", "Professor", "IFPB", "Dados"],
            "Guga Wag": ["Homem", "Real", "Professor", "IFPB", "Operacionais"],
            "BatLeo": ["Homem", "Real", "Professor", "IFPB", "Protocolos"],
            "Bob Esponja": ["Homem", "Desenho", "Amarelo", "Estrela", "Cascudo"],
            "Patrick Estrela": ["Homem", "Desenho", "Rosa", "Esponja", "Mar"],
            "Pikachu": ["Homem", "Desenho", "Amarelo", "Ash", "Pokemon"],
            #"Homer": ["Homem", "Desenho", "Amarelo", "Pai de Bart", "Pai de Lisa", "Pai de Maggie", "Marido de Marge"],
        }
        return map

    # def __personagens(self):
    #     return [
    #         "Alex Sandro", 
    #         "Guga Wag", 
    #         "BatLeo", 
    #         "Elon Musk", 
    #         "Sergio Sacani",
    #         "Bob Esponja", 
    #         "Patrick Estrela", 
    #         "Pikachu",  
    #         "Homer", 
    #         "Picapau"
    #         "Bella",
    #         "Moana" , 
    #         "Hermione Granger", 
    #         "Fiona",
    #         "Ellie", 
    #         "Coraline Jones",
    #         "Ada Lovelace",
    #         "Marie Curie", 
    #         "Amelia Earhart", 
    #         "Anne Frank"
    #     ]

    def __random_quest(self, array):
        self.__pergunta_vez = rd.randint(0, len(array) - 1)
        return self.__pergunta_vez
    
    def __empilhaPergunta(self, pergunta):
        pilha = Pilha()
        pilha.empilha(pergunta)
        
    def __numeroRodadas(self):
        #rodadas = self.__rodadas + 1
        self.__rodadas += 1
        return self.__rodadas 
    
    
    
    def __encontraPersonagem(self, pUser):
        
        for i in range (len(pUser)):
            meus_personagens = self.__personagens()
            for chave, val in meus_personagens.items():
                if set(pUser).issubset(set(val)):
                    personagem = chave
                    break
                else:
                    personagem = "Não encontrado"
            break
        return personagem

    def personagem(self):
        return self.__personagemUser
        #print("Seu personagem é:", self.__encontraPersonagem(self.__personagemUser),"\nRodadas -> ", self.__numeroRodadas())

    def __limpaTerminal(self):
        sistema = os.name
        if sistema == "nt": #Limpa terminal no windows
            os.system("cls")
        else: #$Limpa terminal no linux e outros
            os.system("clear")
            
# def bem_vindo():
#     print("""
#     ==========================IdentiFind==========================
#     ==============================================================
#                                                 creat by: brunovs
#     ==============================================================
#     """ )

# bem_vindo()
# teste = IdentFind()
# teste.iniciar()
