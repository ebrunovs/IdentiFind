import random as rd
import os
from pilha import Pilha
from lista import Lista
from hashtable import HashTable
#HASHTABLE AQUI? OU DENTRO DO OBJETO "IDENTFIND"

class IdentFind:
    #inicia o Objeto
    
    def __init__(self) -> None:
        self.__rodadas = -1 #quantidade de rodadas
        self.__personagemUser = [] #lista de caracteristicas do personagem do usuario
        self.__pergunta_vez = None #pergunta atual
        self.__jogo_em_andamento = False
        self.__lista = Lista()
        self.__verifica_lista_perguntas = False
        self.__caracteristicas_personagem = HashTable()
        self.perguntas_respondidas = Pilha()


    def iniciar(self):
        self.__verificar_jogo_em_andamento()
        self.__iniciar_jogo()
        #self.__jogar()

    def __verificar_jogo_em_andamento(self):
        if self.__jogo_em_andamento: 
            raise Exception("Jogo já iniciado")

    def __iniciar_jogo(self):
        self.__jogo_em_andamento = True

    def __jogar(self):
        while len(self.__personagemUser) != 4 :  # Limitando a 4 rodadas 
            try: 
                input(self.pergunta_atual())
            except IndexError:
                print("Acabaram as perguntas")
                continue
            except KeyboardInterrupt:
                print("Programa encerrado")
                break
        return self.personagem_encontrado(self.__personagemUser)
            
    def personagem_encontrado(self):
        return self.__encontraPersonagem(self.__personagemUser)
    
    def pergunta_atual(self):
        return self.__geraPergunta()
    
    def __rodada(self):
        ...
        #Comunicação Cliente Servidor
        #print("\nRodada -> ", self.__numeroRodadas())
        #pergunta_atual = self.__geraPergunta()
        #print(pergunta_atual)
        #resposta = input("Responda 'sim' ou 'nao': ").lower()
        #self.__processar_resposta(resposta, pergunta_atual)

    def processar_resposta(self, resposta):
        self.__processar_resposta(resposta, self.__pergunta_vez)

    def __processar_resposta(self, resposta, pergunta_atual):
        if resposta == 'sim':
            self.__resposta_sim(pergunta_atual)
        elif resposta == 'nao':
            self.__resposta_nao(pergunta_atual)
        else:
            print("Resposta inválida")

    def personagemUsuario(self):
        return self.__personagemUser

    def __resposta_sim(self, pergunta_atual):
        quebra_perg = pergunta_atual.split()
        quebra_perg = quebra_perg[len(quebra_perg) - 1]
        self.__personagemUser.append(quebra_perg[:-1]) if quebra_perg[:-1] not in self.__personagemUser else None
        self.__empilhaPergunta(pergunta_atual)
        self.__lista.remover_por_valor(pergunta_atual)
        #print(self.__personagemUser)
        #self.__limpaTerminal()

    def __resposta_nao(self, pergunta_atual):
        quebra_perg = pergunta_atual.split()
        quebra_perg = quebra_perg[len(quebra_perg) - 1]
        #self.__personagemUser.remove(quebra_perg[:-1]) if quebra_perg[:-1] in self.__personagemUser else None
        self.__lista.remover_por_valor(pergunta_atual)
        print(self.__personagemUser)
        #self.__limpaTerminal()
        
            
    def __perguntas(self):
        self.__verifica_lista_perguntas = True
        self.__lista.inserir(1, "Seu personagem é Homem?")
        self.__lista.inserir(2, "Seu personagem é Real?")
        self.__lista.inserir(3, "Seu personagem é Professor?")
        self.__lista.inserir(4, "Seu personagem é Professor do IFPB?")
        self.__lista.inserir(5, "Seu personagem é Professor de Estrutura de Dados?")
        self.__lista.inserir(6, "Seu personagem é Professor de Sistemas de Operacionais?")
        self.__lista.inserir(7, "Seu personagem é Professor de Protocolos?")
        self.__lista.inserir(8, "Seu personagem é melhor amigo do Patrick Estrela?")
        self.__lista.inserir(9, "Seu personagem é melhor amigo do Bob Esponja?")
        self.__lista.inserir(10, "Seu personagem faz parte de algum Desenho?")
        self.__lista.inserir(11, "Seu personagem é Amarelo?")
        self.__lista.inserir(12, "Seu personagem trabalha no Siri Cascudo?")
        self.__lista.inserir(13, "Seu personagem é uma Estrela do Mar?")
        self.__lista.inserir(14, "Seu personagem é melhor amigo do Ash?")
        self.__lista.inserir(15, "Seu personagem é Rosa?")
        self.__lista.inserir(16, "Seu personagem é um Pokemon?")
        
    def __geraPergunta(self):
        if not self.__verifica_lista_perguntas:
            self.__perguntas()
        self.__pergunta_vez = self.__lista.busca_por_posicao(self.__lista.posicaoAleatoria())
        return self.__pergunta_vez
        
    def __personagens(self):
        self.__caracteristicas_personagem.put("Alex Sandro", ["Homem", "Real", "Professor", "IFPB", "Dados"])
        self.__caracteristicas_personagem.put("Guga Wag", ["Homem", "Real", "Professor", "IFPB", "Operacionais"])
        self.__caracteristicas_personagem.put("BatLeo", ["Homem", "Real", "Professor", "IFPB", "Protocolos"])
        self.__caracteristicas_personagem.put("Bob Esponja", ["Homem", "Desenho", "Amarelo", "Estrela", "Cascudo"])
        self.__caracteristicas_personagem.put("Patrick Estrela", ["Homem", "Desenho", "Rosa", "Esponja", "Mar"])
        self.__caracteristicas_personagem.put("Pikachu", ["Homem", "Desenho", "Amarelo", "Ash", "Pokemon"])
        self.__caracteristicas_personagem.put("Homer", ["Homem", "Desenho", "Amarelo", "Pai de Bart", "Pai de Lisa", "Pai de Maggie", "Marido de Marge"])
        self.__caracteristicas_personagem.put("Picapau", ["Homem", "Desenho", "Amarelo", "Pássaro", "Floresta"])
        self.__caracteristicas_personagem.put("Bella", ["Mulher", "Real", "Professora", "IFPB", "Dados"])
        return self.__caracteristicas_personagem
    
    def __empilhaPergunta(self, pergunta):
        self.perguntas_respondidas.empilha(pergunta)
    
    def rodada(self):
        return self.__numeroRodadas()
    
    def __numeroRodadas(self):
        self.__rodadas += 1
        return self.__rodadas 
    
    def __encontraPersonagem(self, pUser):
        for _ in range(len(pUser)):
            meus_personagens = self.__personagens()
            for chave, val in meus_personagens.items():
                if set(pUser).issubset(set(val)):
                    personagem = chave
                    break
                else:
                    personagem = "Não encontrado"
            break
        return personagem

    # def personagem(self):
    #     return self.__personagemUser
        #print("Seu personagem é:", self.__encontraPersonagem(self.__personagemUser),"\nRodadas -> ", self.__numeroRodadas())

            
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

# while len(teste.personagemUsuario()) != 4:
#     try:
#         print(teste.rodada())
#         print(teste.pergunta_atual())
#         resposta = input("Responda 'sim' ou 'nao': ").lower()
#         teste.processar_resposta(resposta)
#         print(teste.personagemUsuario())
#     except KeyboardInterrupt:
#         print("Programa encerrado")
#         break
#     except IndexError:
#         print("Acabaram as perguntas")
#         break
#     except Exception as e:
#         print(e)
#         break
# if len(teste.__personagemUser) == 4:    
#     print('Seu personagem é:',teste.personagem_encontrado())


