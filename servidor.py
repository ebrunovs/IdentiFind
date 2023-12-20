import socket
from identifind import IdentFind
import threading


TAM_MSG = 1024
HOST = '0.0.0.0'
PORT = 40000
clientes = []  # Lista de clientes conectados
jogos = {}  # Dicionário para armazenar os jogos de cada cliente
lock = threading.Lock()

# Processa a mensagem recebida do cliente e retorna a resposta
def processa_msg_cliente(msg, con, cliente):
    global jogos
    msg = msg.decode()
    print('Cliente', cliente, 'enviou', msg)

    if msg == '0000':  # Se o cliente enviar 'sair', desconecte-o
        print('Cliente', cliente, 'desconectado.')
        con.send(str.encode('1001\n'))
        return False  # Encerra o processamento do cliente

    if msg == '2408':
        if cliente in jogos:
            del jogos[cliente]
        if cliente not in jogos:
            try:
                jogo = IdentFind()
                jogo.iniciar()
                jogos[cliente] = jogo
                #print(jogos)# Associando o jogo ao cliente no dicionário
                pergunta = jogo.pergunta_atual()
                con.send(str.encode('2409\n' + pergunta))
            except Exception:
                con.send(str.encode('1234')) # envia codigo de erro

    elif msg == '2705' or msg == '2805':
        # Garante exclusão mútua no acesso ao dicionário de jogos
        with lock:
            if cliente in jogos and jogos[cliente] is not None:
                jogos[cliente].processar_resposta('sim' if msg == '2705' else 'nao')
                if len(jogos[cliente].personagemUsuario()) != 4:
                    pergunta = jogos[cliente].pergunta_atual()
                    con.send(str.encode('2905\n' + pergunta))
                else:
                    con.send(str.encode('1111\n' + jogos[cliente].personagem_encontrado()))
            else:
                con.send(str.encode('4005')) # envia codigo de erro
            
    
    else:
        con.send(str.encode('0001\n'))
    return True


# Processa o cliente conectando-o ao servidor e desconectando-o
def processa_cliente(con, cliente):
    print('Cliente conectado', cliente)
    while True:
        try:
            msg = con.recv(TAM_MSG)
            if not msg or not processa_msg_cliente(msg, con, cliente): 
                break
        except ConnectionResetError:
            print('Cliente desconectado', cliente)
            break
    con.close()

# Aceita conexões de varios clientes via thread
def aceita_conexoes(sock):
    while True:
        try:
            con, cliente = sock.accept()
            threading.Thread(target=processa_cliente, args=(con, cliente)).start()
        except Exception:
            print('Erro ao aceitar conexão')

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv = (HOST, PORT)
    sock.bind(serv)
    sock.listen(50)
    threading.Thread(target=aceita_conexoes, args=(sock,)).start()
    print('Servidor', HOST+':'+str(PORT), 'conectado...')
    aceita_conexoes(sock)
except ConnectionError:
    print('Erro ao iniciar Conexão')
    sock.close()
except OSError:
    print('\nNão pode haver mais de um servidor em uma unica porta.\n')
    

#threading.Thread(target=aceita_conexoes, args=(sock,)).start()

# try:
#     print('Servidor', HOST+':'+str(PORT), 'conectado...')
#     aceita_conexoes(sock) # Inicia a thread de aceitar conexoes
# except ConnectionError:
#     print('Erro ao iniciar Conexão')
#     sock.close()

sock.close()