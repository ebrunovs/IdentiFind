# Protocolos do Cliente:

## 2408 (iniciar)
***Pede ao servidor para começar o jogo. Sempre que inicia, sobrepõe o anterior.***


## 2705 (sim)
***A resposta enviada para o servidor é positiva.***


## 2805 (não)
***A resposta enviada para o servidor é negativa.***


## 0000 (sair)
***O cliente requisita a saída ao servidor.***


# Protocolos do Servidor:

## 2409 (starting)
***Recebe o pedido de início do cliente e envia este protocolo como resposta.***


## 2905 (received)
***Envia ao cliente comprovação que recebeu a resposta (sim/não).***


## 1001 (quit)
***Ao receber um pedido de saída do cliente, envia uma confirmação ao pedido.***


## 1111 (personagem encontrado)
***Ao possuir todas as respostas ligadas ao personagem, envia a resposta ao cliente.***


## 4004 (error iniciar)
***Enviado quando houve alguma falha na inicialização do jogo.***


## 4005 (erro na resposta), # erro ao responder a pergunta
***Enviado quando o jogador tenta responder sem iniciar o jogo.***


## 0001 (command error, não entendeu o comando)
***Enviado quando não é reconhecido o pedido/comando do cliente.***
