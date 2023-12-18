import socket
import os
from teste2 import IdentFind
import threading


TAM_MSG = 1024         # Tamanho do bloco de mensagem
HOST = '0.0.0.0'       # IP de alguma interface do Servidor
PORT = 40000           # Porta que o Servidor escuta
jogo = None

def processa_msg_cliente(msg, con, cliente):
    global jogo
    msg = msg.decode()
    print('Cliente', cliente, 'enviou', msg)

    if jogo is not None and len(jogo.personagemUsuario()) == 4:
        con.send(str.encode('WIN\n' + jogo.personagem_encontrado()))

    if msg.upper() == 'START':
        try:
            jogo = IdentFind()
            jogo.iniciar()
            pergunta = jogo.pergunta_atual()
            con.send(str.encode('STARTING\n' + pergunta))
        except Exception:
            con.send(str.encode('1234')) # envia codigo de erro

    elif msg.upper() == 'YES':
        if jogo is not None:
            jogo.processar_resposta('sim')
            pergunta = jogo.pergunta_atual()
            con.send(str.encode('RC\n' + pergunta))

    elif msg.upper() == 'NO':
        if jogo is not None:
            jogo.processar_resposta('nao')
            pergunta = jogo.pergunta_atual()
            con.send(str.encode('RC\n' + pergunta))
    else:
        con.send(str.encode('-ERR Invalid command\n'))
    return True


def processa_cliente(con, cliente):
    # IMPLEMENTAR UM MULTITHREADING PARA VARIOS CLIENTES 
    print('Cliente conectado', cliente)
    while True:
        msg = con.recv(TAM_MSG)
        if not msg or not processa_msg_cliente(msg, con, cliente): break
    con.close()
    print('Cliente desconectado', cliente)

def aceita_conexao(sock):
    while True:
        con, cliente = sock.accept()
        thread = threading.Thread(target=processa_cliente, args=(con, cliente))
        thread.start()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)

while True:
    try:
        con, cliente = sock.accept()
    except: break
    processa_cliente(con, cliente)
    
aceita_conexao(sock) # Inicia a thread de aceitar conexoes
sock.close()
