# ☝️ PROJETÃO IDENTIFIND ❓

**A proposta deste projeto é simular um jogo de perguntas e respostas que ligam os resultados a um personagem. Baseado no jogo virtual "Akinator©️".**

## 📖 Sumário 📖

--> [Aquisição/Instalação](https://github.com/ebrunovs/IdentiFind/blob/main/README.md#-aquisiçãoinstalação-)

--> [Como Funciona](https://github.com/ebrunovs/IdentiFind/blob/main/README.md#-como-funciona-)

--> [Codificação](https://github.com/ebrunovs/IdentiFind/blob/main/README.md#-codificação-)

--> [Criadores](https://github.com/ebrunovs/IdentiFind/blob/main/README.md#-criadores-)


## 🌐 Aquisição/Instalação 📡

**Para iniciar a jogar este jogo, é necessário:**
1. Primeiro possuir uma aplicação que permita o uso de códigos, de preferência o Visual Studio Code.
2. Logo em seguida, é preciso um interpretador python instalado de versão 3.11.6 ou superior, facilmente achável no site
- [python](https://www.python.org/downloads/).
3. Então, baixe os arquivos deste repositório e abra-o na aplicação de código de sua escolha, link do repositório a seguir
- [Clique Aqui!](https://github.com/ebrunovs/IdentiFind).
4. Por fim, é necessário abrir um terminal, escrever <br/>
```"pip install numpy"``` <br/>e tudo estará pronto para começar a jogar. Caso esteja curioso sobre sua funcionalidade, numpy é uma biblioteca que suporta processamento de grandes arranjos e matrizes, possuindo também uma grande coleção de funções matemáticas para operar tais matrizes.
5. Para dar início ao jogo, é necessário abrir dois terminais separados, digitar ".\" + nome do arquivo, tudo junto sem espaçamento, de ambos "servidor.py" e "cliente.py".

## 🤔 Como Funciona 💭

**Feito os passos da instalação, agora é hora de iniciar o jogo! Para começar, é necessário ativar um terminal para o servidor e um terminal para o cliente. Feito isso, serão feitas perguntas sobre um personagem que o jogador deverá pensar a respeito e responder de acordo com o perguntado, por exemplo "Seu personagem é uma esponja?" e caso responda sim, "Seu personagem é Bob Esponja!". Após responder diversas perguntas, o jogo irá tentar identificar o personagem de sua escolha.**

**Arquivos Inclusos:**<br/>
```
||cliente.py > Referente à sessão do cliente, onde serão recebidas por ele as perguntas feitas, o local para responder e o envio da resposta para o servidor.
||hashtable.py > Utilizada para guardar as informações recebidas para cada pergunta, notavelmente os personagens.
||identifind.py > Main do código, onde são recebidas todas as outras informações e partes do código.
||lista.py > Lista encadeada responsável por armazenar as perguntas que serão lançadas ao jogador.
||pilha.py > Armazena as perguntas respondidas positivamente.
||protocols.md > Lista todos os protocolos utilizados no projeto.
||readme.md > Esta página que você está lendo. Serve para explicar o código, como adquirí-lo e como iniciá-lo; os autores e docentes responsáveis; e as matérias e materiais envolvidas.
||servidor.py > Entra em conexão com um ou mais clientes, recebe um protocolo e executa o que é pedido.
```

**Existem vários protocolos envolvidos no funcionamento do jogo, notavelmente para o funcionamento da conexão cliente/servidor e sua comunicação, para mais detalhes, ler "protocols.md".**

## 💻 Codificação 🧑‍💻

**Disciplinas Envolvidas:**
***<br/>--> Sistemas Operacionais (Gustavo Wagner)***
***<br/>--> Protocolos de Redes (Leônidas Francisco)***
***<br/>--> Estrutura de Dados (Alex Sandro da Cunha)***
<br/>
**Foram utilizadas as tecnologias:**
***<br/>--> Python***
***<br/>--> Threading***
***<br/>--> Sockets***

## ✍️ Criadores 🖋️

![Alessandro Rodrigues](https://avatars.githubusercontent.com/u/130919708?v=4)
### Email Institucional: alessandro.rodrigues@academico.ifpb.edu.br
<br/>
<br/>

![Alex Loureiro](https://avatars.githubusercontent.com/u/128738123?v=4)
### Email Institucional: alex.loureiro@academico.ifpb.edu.br
<br/>
<br/>

![Bruno Eneas](https://avatars.githubusercontent.com/u/81043770?s=48&v=4)
### Email Institucional: eneas.bruno@academico.ifpb.edu.br