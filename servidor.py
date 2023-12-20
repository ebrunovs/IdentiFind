import socket
import os
from teste2 import IdentFind
import threading


TAM_MSG = 1024
HOST = '0.0.0.0'
PORT = 40000
jogos = {}  # Dicionário para armazenar os jogos de cada cliente
lock = threading.Lock()

def processa_msg_cliente(msg, con, cliente):
    global jogos
    msg = msg.decode()
    print('Cliente', cliente, 'enviou', msg)

    if cliente in jogos and len(jogos[cliente].personagemUsuario()) == 4:
        con.send(str.encode('WIN\n' + jogos[cliente].personagem_encontrado()))

    if msg.upper() == 'START':
        try:
            jogo = IdentFind()
            jogo.iniciar()
            jogos[cliente] = jogo  # Associando o jogo ao cliente no dicionário
            pergunta = jogo.pergunta_atual()
            con.send(str.encode('STARTING\n' + pergunta))
        except Exception:
            con.send(str.encode('1234')) # envia codigo de erro

    elif msg.upper() == 'YES' or msg.upper() == 'NO':
        #with lock:
            if cliente in jogos and jogos[cliente] is not None:
                jogos[cliente].processar_resposta('sim' if msg.upper() == 'YES' else 'nao')
                pergunta = jogos[cliente].pergunta_atual()
                con.send(str.encode('RC\n' + pergunta))
    else:
        con.send(str.encode('-ERR Invalid command\n'))
    return True


def processa_cliente(con, cliente):
    # IMPLEMENTAR UM MULTITHREADING PARA VARIOS CLIENTES 
    print('Cliente conectado', cliente)
    while True:
        msg = con.recv(TAM_MSG)
        if not msg or not processa_msg_cliente(msg, con, cliente): 
            break
    con.close()
    print('Cliente desconectado', cliente)

def aceita_conexoes(sock):
    while True:
        con, cliente = sock.accept()
        threading.Thread(target=processa_cliente, args=(con, cliente)).start()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)

threading.Thread(target=aceita_conexoes, args=(sock,)).start()

# while True:
#     try:
#         con, cliente = sock.accept()
#     except: break
#     processa_cliente(con, cliente)

# Mantém o programa principal em execução
while True:
    try:
        # Qualquer outra lógica que você queira executar no programa principal
        pass
    except Exception as e:
        print("Erro:", e)
        break

#aceita_conexao(sock) # Inicia a thread de aceitar conexoes
sock.close()