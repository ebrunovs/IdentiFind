from pilha import Pilha
from lista import Lista
from hashtable import HashTable


class IdentFind:
    
    #inicia o Objeto
    def __init__(self) -> None:
        self.__rodadas = 0 #quantidade de rodadas
        self.__personagemUser = [] #lista de caracteristicas do personagem do usuario
        self.__pergunta_vez = None #pergunta atual
        self.__jogo_em_andamento = False # Verifica se há jogo em andamento
        self.__lista = Lista() # Lista de perguntas
        self.__verifica_lista_perguntas = False # Verifica se a lista de perguntas foi criada
        self.__caracteristicas_personagem = HashTable() # Tabela de personagens
        self.__perguntas_respondidas = Pilha() # Pilha de perguntas respondidas com 'sim'

    # Inicia o jogo
    def iniciar(self):
        self.__verificar_jogo_em_andamento()
        self.__iniciar_jogo()
    
    # Verifica se o jogo já foi iniciado
    def __verificar_jogo_em_andamento(self):
        if self.__jogo_em_andamento: 
            raise Exception("Jogo já iniciado")

    # Atualiza o estado do jogo
    def __iniciar_jogo(self):
        self.__jogo_em_andamento = True

    # def __jogar(self):
    #     while len(self.__personagemUser) != 4 :  # Limitando a 4 rodadas 
    #         try: 
    #             input(self.pergunta_atual())
    #         except IndexError:
    #             print("Acabaram as perguntas")
    #             continue
    #         except KeyboardInterrupt:
    #             print("Programa encerrado")
    #             break
    #     return self.personagem_encontrado(self.__personagemUser)
    
    # Retorna o personagem encontrado
    def personagem_encontrado(self):
        return self.__encontraPersonagem(self.__personagemUser)
    
    # Retorna a lista de caracteristicas do personagem do usuario
    def personagemUsuario(self):
        return self.__personagemUser
    
    
    # Armazena a pergunta gerada para lançar para o servidor
    def pergunta_atual(self):
        return self.__geraPergunta()

    # Armazena a resposta do servidor
    def processar_resposta(self, resposta):
        self.__processar_resposta(resposta, self.__pergunta_vez)


    # Processa a resposta do servidor
    def __processar_resposta(self, resposta, pergunta_atual):
        if resposta == 'sim':
            self.__resposta_sim(pergunta_atual)
        elif resposta == 'nao':
            self.__resposta_nao(pergunta_atual)
        else:
            print("Resposta inválida")

    # Trata caso a resposta seja 'sim'
    def __resposta_sim(self, pergunta_atual):
        quebra_perg = pergunta_atual.split()
        quebra_perg = quebra_perg[len(quebra_perg) - 1]
        self.__personagemUser.append(quebra_perg[:-1]) if quebra_perg[:-1] not in self.__personagemUser else None # Adiciona a caracteristica do personagem na lista se não estiver
        self.__empilhaPergunta(pergunta_atual)
        self.__lista.remover_por_valor(pergunta_atual) # Remove a pergunta da lista de perguntas
        
    # Trata caso a resposta seja 'nao'
    def __resposta_nao(self, pergunta_atual):
        quebra_perg = pergunta_atual.split()
        quebra_perg = quebra_perg[len(quebra_perg) - 1]
        self.__lista.remover_por_valor(pergunta_atual) # Remove a pergunta da lista de perguntas
        
            
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
        self.__lista.inserir(17, "Seu personagem é Mulher?")
        self.__lista.inserir(18, "Seu personagem é Azul?")
        self.__lista.inserir(19, "Seu personagem é um Pássaro?")
        
    # Gera uma pergunta aleatória da lista de perguntas
    def __geraPergunta(self):
        if not self.__verifica_lista_perguntas:
            self.__perguntas()
        self.__pergunta_vez = self.__lista.busca_por_posicao(self.__lista.posicaoAleatoria())
        return self.__pergunta_vez
    
    # Armazena a pergunta na pilha de perguntas respondidas (Atualização futura: poder retornar a pergunta para alterar a resposta)
    def __empilhaPergunta(self, pergunta):
        self.__perguntas_respondidas.empilha(pergunta)
        
    # Dicionario de personagens e suas caracteristicas  
    def __personagens(self):
        self.__caracteristicas_personagem.put("Alex Sandro", ["Homem", "Real", "Professor", "IFPB", "Dados"])
        self.__caracteristicas_personagem.put("Guga Wag", ["Homem", "Real", "Professor", "IFPB", "Operacionais"])
        self.__caracteristicas_personagem.put("BatLeo", ["Homem", "Real", "Professor", "IFPB", "Protocolos"])
        self.__caracteristicas_personagem.put("Bob Esponja", ["Homem", "Desenho", "Amarelo", "Estrela", "Cascudo"])
        self.__caracteristicas_personagem.put("Patrick Estrela", ["Homem", "Desenho", "Rosa", "Esponja", "Mar"])
        self.__caracteristicas_personagem.put("Pikachu", ["Homem", "Desenho", "Amarelo", "Ash", "Pokemon"])
        self.__caracteristicas_personagem.put("Pica-Pau", ["Homem", "Desenho", "Azul", "Pássaro",])
        self.__caracteristicas_personagem.put("Bella", ["Mulher", "Real", "Professora", "IFPB", "Dados"])
        return self.__caracteristicas_personagem
    
    # Busca o personagem do usuario no dicionario de personagens
    def __encontraPersonagem(self, pUser):
        for _ in range(len(pUser)):
            meus_personagens = self.__personagens() #armazena o dicionario de personagens
            for chave, val in meus_personagens.items(): #percorre o dicionario
                if set(pUser).issubset(set(val)): #verifica se a lista de caracteristicas do usuario é um subconjunto da lista de caracteristicas do personagem
                    personagem = chave
                    break
                else:
                    personagem = "Não encontrado"
            break
        return personagem
    
    
    # Retorna a quantidade de rodadas
    def rodada(self):
        return self.__numeroRodadas()
    
    # Incrementa a quantidade de rodadas
    def __numeroRodadas(self):
        self.__rodadas += 1
        return self.__rodadas 
    