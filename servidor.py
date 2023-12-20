import socket
from identifind import IdentFind
import threading


#SERVIDOR ESTA OK ATÉ ENTAO

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
        con.send(str.encode('1111\n' + jogos[cliente].personagem_encontrado()))

    if msg == '2408':
        if cliente in jogos:
            del jogos[cliente]
        if cliente not in jogos:
            try:
                jogo = IdentFind()
                jogo.iniciar()
                jogos[cliente] = jogo
                print(jogos)# Associando o jogo ao cliente no dicionário
                pergunta = jogo.pergunta_atual()
                con.send(str.encode('2409\n' + pergunta))
            except Exception:
                con.send(str.encode('1234')) # envia codigo de erro

    elif msg == '2705' or msg == '2805':
        with lock:
            if cliente in jogos and jogos[cliente] is not None:
                jogos[cliente].processar_resposta('sim' if msg == 'YES' else 'nao')
                pergunta = jogos[cliente].pergunta_atual()
                con.send(str.encode('2905\n' + pergunta))
    else:
        con.send(str.encode('-ERR Invalid command\n'))
    return True


def processa_cliente(con, cliente):
    print('Cliente conectado', cliente)
    print(jogos)
    while True:
        try:
            msg = con.recv(TAM_MSG)
            if not msg or not processa_msg_cliente(msg, con, cliente): 
                break
        except ConnectionResetError:
            print('Cliente desconectado', cliente)
            break
    con.close()

def aceita_conexoes(sock):
    while True:
        try:
            con, cliente = sock.accept()
            threading.Thread(target=processa_cliente, args=(con, cliente)).start()
        except Exception:
            print('Erro ao aceitar conexão')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)

threading.Thread(target=aceita_conexoes, args=(sock,)).start()


aceita_conexoes(sock) # Inicia a thread de aceitar conexoes


sock.close()