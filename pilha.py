class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None
    
    @property
    def carga(self):
        return self.__carga
    
    @property
    def prox(self):
        return self.__prox

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self):
        return f'{self.__carga}'




class Pilha:
    """A classe Pilha implementa a estrutura de dados "Pilha".
       Técnica: <Encadeamento/Sequencial>
       A classe foi desenvolvida de maneira a permitir que qualquer tipo de dado
       seja armazenado como carga de um nó.

     Atributos:
     ---------------------
        *definir a lista de atributos*
    """
    def __init__(self):
        """ Construtor padrão da classe Pilha sem argumentos. Ao instanciar
            um objeto do tipo Pilha, esta iniciará vazia. 
        """
        self.__topo = None
        self.__tamanho = 0
        
    def estaVazia(self)->bool:
        """ Método que verifica se a pilha está vazia .

        Returns:
            boolean: True se a pilha estiver vazia, False caso contrário.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente na pilha [10,20,30,40]<- topo
            if(p.estaVazia()): 
               # instrucoes quando a pilha estiver vazia
        """
        return self.__topo == None

    def __len__(self)->int:
        """ Método que retorna a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<- p
            print (p.tamanho()) # exibe 4
        """ 
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        """ Método que recupera a carga armazenada em um determinado elemento da pilha

        Args:
            posicao (int): um número correpondente à ordem do elemento existente.
                           Sentido: do topo em direção à base
        
        Returns:
            Any: a carga armazenada no elemento correspondente à posição indicada.

        Raises:
            PilhaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a uma posição  que excede a
                      quantidade de elementos da lista.                      
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            posicao = 5
            print (p.elemento(3)) # exibe 30
        """
        try:
            assert self.estaVazia() == False, 'Pilha está vazia'
            assert posicao > 0 and posicao <= len(self), f'Posição {posicao} é inválida para a pilha com {len(self)} elementos'

            contador = 1
            cursor = self.__topo
            while( cursor is not None ):
                if contador == posicao:
                    return cursor.carga
                cursor = cursor.prox
                contador += 1

            
        except AssertionError as ae:
            raise PilhaException(ae)
                
    def busca(self, key:any)->int:
        """ Método que retorna a posicao ordenada, dentro da pilha, em que se
            encontra uma chave passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada.
            O ordenamento que determina a posição é da base para o topo.

        Args:
            key (any): um item de dado que deseja procurar na pilha
        
        Returns:
            int: um número inteiro representando a posição, na pilha, em que foi
                 encontrada a chave.

        Raises:
            PilhaException: Exceção lançada quando o argumento "key"
                  não está presente na pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]<-topo
            print (p.elemento(40)) # exibe 4
        """
        if (self.estaVazia()):
            raise PilhaException('Pilha está vazia')
        contador = 1
        cursor = self.__topo
        while( cursor is not None ):
            if cursor.carga == key:
                return contador
            cursor = cursor.prox
            contador += 1
        raise PilhaException(f'A chave {key} não está presente na pilha')


    def topo(self)->any:
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo.
    
        Returns:
            any: o conteúdo armazenado no elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        return self.__topo.carga

    def empilha(self, carga:any):
        """ Método que adiciona um novo elemento ao topo da pilha

        Args:
            carga (any): a carga que será armazenada no novo elemento do topo da pilha.

        Examples:
            p = Pilha()
            ...   # considere a pilha  [10,20,30,40]<-topo
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        novo = No(carga)
        novo.prox = self.__topo
        self.__topo = novo
        self.__tamanho += 1


    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e retorna
            sua carga correspondente.
    
        Returns:
           any: a carga armazenada no elemento removido

        Raises:
            PilhaException: Exceção lançada quando se tenta remover algo de uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere a pilha [10,20,30,40]<-topo
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        carga = self.__topo.carga
        self.__topo = self.__topo.prox
        self.__tamanho -= 1
        return carga

        
    def __str__(self)->str:
        """ Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base

        Returns:
           str: a carga dos elementos da pilha, do topo até a base
        """  
        s = 'topo->[ '
        cursor = self.__topo
        while( cursor is not None ):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]'
        return s
