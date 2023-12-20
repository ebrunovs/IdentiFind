#!/usr/bin/env python3
import socket
import sys

TAM_MSG = 1024         # Tamanho do bloco de mensagem
HOST = '127.0.0.1'     # IP do Servidor
PORT = 40000           # Porta que o Servidor escuta

# IMPELEMENTAR APENAS OS PRINTS, PARA QUE TUDO FIQUE OK

# Codifica o comando do usuário para o protocolo
def decode_cmd_usr(cmd_usr):
    cmd_map = {
    'iniciar' : '2408', #start
    'sim' : '2705', #yes
    'nao' : '2705', #no
    'sair': '0000', #quit #Fazer ainda
    }
    tokens = cmd_usr
    if tokens.lower() in cmd_map:
        tokens = cmd_map[tokens.lower()]
        return tokens
    else:
        return False

# Decodifica o protocolo para a mensagem do usuário
def decode_cmd_svr(protocol_svr):
    cmd_map = {
    '2409' : 'STARTING', #start
    '2905' : 'RECEIVED', #yes
    '1111' : 'WIN', #no
    '1234' : '1234', #quit #Fazer ainda
    }
    tokens = protocol_svr
    if tokens.lower() in cmd_map:
        tokens = cmd_map[tokens.lower()]
        return tokens
    else:
        return False

if len(sys.argv) > 1:
    HOST = sys.argv[1]
print('Servidor:', HOST+':'+str(PORT))
serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
print('Para encerrar use SAIR, CTRL+D ou CTRL+C\n')

while True:
    try:
        cmd_usr = input('IdentF> ')
    except:
        cmd_usr = 'SAIR'
    cmd = decode_cmd_usr(cmd_usr)
    if not cmd:
        print('Comando indefinido:', cmd_usr)
    else:
        sock.send(cmd.encode())
        dados = sock.recv(TAM_MSG)
        if not dados: break
        protocol_svr = dados.decode().split('\n')[0]
        msg_status = decode_cmd_svr(protocol_svr)
        dados = dados.decode()[len(protocol_svr)+1:]
        
        if msg_status == 'QUIT':
            break
        elif msg_status == 'STARTING':
            #bem_vindo()
            print('Dados: ',dados)
            # IdentFind #
            
        elif msg_status == 'RECEIVED':
            
            print('Dados: ',dados)
            
        elif msg_status == 'WIN':
            print('Dados: ',dados)
        elif msg_status == '1234':
            print('Erro ao iniciar o jogo')
        elif msg_status == '-ERR Invalid command':
            print('Comando inválido:', cmd_usr)
            
sock.close()