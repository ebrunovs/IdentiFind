class ArvoreException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__esq = None
        self.__dir = None
    
    @property
    def carga(self):
        return self.__carga
    
    @property
    def esq(self):
        return self.__esq

    @property
    def dir(self):
        return self.__dir

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @esq.setter
    def esq(self, novoEsq):
        self.__esq = novoEsq

    @dir.setter
    def dir(self, novoDir):
        self.__dir = novoDir

    def __str__(self):
        return f'{self.__carga}'
    
class ArvoreBinaria:
    def __init__(self, raiz:any):
        '''Inicializa a árvore com um nó raiz'''
        self.__raiz = No(raiz)
        self.__cursor = self.__raiz
        
    def estaVazia(self)->bool:
        pass

    def getRaiz(self)->any:
        '''Obtem a carga do nó "root"'''
        pass

    def getCursor(self)->any:
        '''Obtem a carga do nó apontado pelo "cursor"'''
        pass

    def resetCursor(self):
        '''Posiciona o cursor para o nó raiz'''
        pass

    def descer_para_esquerda(self):
        '''Desloca o cursor para o seu filho esquerdo, apenas 
           se tiver filho esquerdo'''
        pass

    def descer_para_direita(self):
        '''Desloca o cursor para o seu filho direito, apenas 
           se tiver filho direito'''
        pass

    def addFilhoEsquerdo(self, carga:any):
        '''Adiciona um novo nó à esquerda do "cursor"
           Se cursor já tiver filho esquerdo, não faz nada.'''
        pass

    def addFilhoDireito(self, carga:any):
        '''Adiciona um novo nó à direita do "cursor"
           Se cursor já tiver filho direita, não faz nada.'''
        pass

    def busca(self, chave:any )->bool:
        '''Percorre a árvore à procura de um nó cuja carga corresponde
           à chave passada como argumento.
           Returns
           ---------
           True: a chave está presente na árvore
           False: caso a chave não esteja na árvore
        '''
        pass

    def preordem(self):
        '''Exibe na tela os nós da árvore com percurso em pré-ordem'''
        pass

    def emordem(self):
        '''Exibe na tela os nós da árvore com percurso em-ordem'''
        pass

    def posordem(self):
        '''Exibe na tela os nós da árvore com percurso em pos-ordem'''
        pass

    def esvazia(self):
        '''Elimina todos os nós da árvore'''
        pass

    def remove(self, key:object):
        '''Remove o nó determinado pela chave de busca.
           IMPORTANTE:
           a) o cursor deve estar posicionado no nó pai referente ao nó chave.
           b) se não puder ser removido (árvore vazia, cursor no local errado,...)
              não é executada qualquer ação'''
        pass

    def __str__(self):
        '''Exibe os nós da árvore com percurso em pré-ordem'''
        return 'Em desenvolvimento'

