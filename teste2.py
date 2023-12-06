import random as rd

#HASHTABLE AQUI? OU DENTRO DO OBJETO "IDENTFIND"

class IdentFind:
    def __init__(self) -> None:
        self.__rodadas = 0
        self.__personagemUser = []
        self.__pergunta_vez = None

    def iniciar(self):
        self.__lista_perguntas = self.__perguntas()
        self.__lista_personagens = self.__personagens()
        jogadas = 0
        while len(self.__personagemUser) != 5 :  # Limitando a 5 rodadas para exemplo
            # try: 
                # if jogadas == 6:
                #     break
                self.__rodadas += 1
                #jogadas += 1
                print("\nRodada -> ", self.__rodadas)
                gera_pergunta = self.__random_quest(self.__lista_perguntas)
                pergunta_atual = self.__lista_perguntas[gera_pergunta]
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
        #REMOVER ESSE PRINT           
        print("Seu personagem é:", self.__encontraPersonagem(self.__personagemUser),"\nRodadas -> ", self.__rodadas)
                # else:
                #     print("Resposta inválida")
                #     continue
                    
            # except IndexError:
            #     print("Acabaram as perguntas")
            #     break
        #print("Seu personagem é:", self.__lista_personagens[0])
        
    def __verificaPersonagem(self):
        pass

    def __perguntas(self):
        # return [
        # "Seu personagem é um ser humano?",
        # "Seu personagem existe na vida real?",
        # "Seu personagem é um animal?",
        # "Seu personagem é famoso?",
        # "Seu personagem viveu antes do século 20?",
        # "Seu personagem é conhecido por habilidades específicas?",
        # "Seu personagem é um personagem de desenho animado?",
        # "Seu personagem é parte de um livro?",
        # "Seu personagem é parte de um jogo de vídeo game?",
        # "Seu personagem é um cientista?",
        # "Seu personagem é um personagem de ficção científica?",
        # "Seu personagem é um atleta?",
        # "Seu personagem é conhecido por sua música?",
        # "Seu personagem é parte de um filme de terror?",
        # "Seu personagem é uma figura política?",
        # "Seu personagem é uma celebridade?",
        # "Seu personagem é um personagem histórico?",
        # "Seu personagem é uma figura religiosa?",
        # "Seu personagem é conhecido por suas invenções?",
        # "Seu personagem é um artista?",
        # "Seu personagem é um super-herói?",
        # "Seu personagem é um vilão?",
        # "Seu personagem é um líder?",
        # "Seu personagem é um músico?",
        # "Seu personagem é um filósofo?",
        # "Seu personagem é uma figura literária?",
        # "Seu personagem é um personagem de conto de fadas?",
        # "Seu personagem é uma figura mitológica?",
        # "Seu personagem é conhecido por suas viagens?",
        # "Seu personagem é um personagem de anime?",
        # "Seu personagem é um personagem de quadrinhos?",
        # "Seu personagem é uma pessoa real?",
        # "Seu personagem é uma figura de Hollywood?",
        # "Seu personagem é conhecido por seu trabalho humanitário?",
        # "Seu personagem é uma figura de televisão?",
        # "Seu personagem é um inventor?",
        # "Seu personagem é um personagem histórico recente?",
        # "Seu personagem é um personagem de fantasia?",
        # "Seu personagem é uma pessoa viva?",
        # "Seu personagem é uma figura da música pop?",
        # "Seu personagem é um personagem de literatura infantil?",
        # "Seu personagem é uma figura do mundo dos negócios?",
        # "Seu personagem é conhecido por seu talento artístico?",
        # "Seu personagem é uma figura da realeza?",
        # "Seu personagem é uma figura esportiva?",
        # "Seu personagem é uma figura do cinema?",
        # "Seu personagem é conhecido por sua inteligência?",
        # "Seu personagem é uma figura do mundo da moda?",
        # "Seu personagem é um personagem de série de TV?",
        # "Seu personagem é uma figura do mundo da ciência?",
        # "Seu personagem é uma figura do mundo da tecnologia?",
        # "Seu personagem é uma figura do mundo da medicina?",
        # ]
        
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
    
    def __empilharPerguntas(self):
        pass
    
    def __encontraPersonagem(self, pUser):
        
        for i in range (len(pUser)):
            meus_personagens = self.__personagens()
            for chave, val in meus_personagens.items():
                if set(val).issubset(set(pUser)):
                    personagem = chave
                    break
                else:
                    personagem = "Não encontrado"
            break
        return personagem
    
    
    #def __reencontrarPersonagem?
        

def bem_vindo():
    print("""
    ==========================IdentiFind==========================
    ==============================================================
                                                creat by: brunovs
    ==============================================================
    """ )

bem_vindo()
teste = IdentFind()
teste.iniciar()
