#!/usr/bin/env python3
import socket
import sys

TAM_MSG = 1024         # Tamanho do bloco de mensagem
HOST = '127.0.0.1'     # IP do Servidor
PORT = 40000           # Porta que o Servidor escuta

# def decode_cmd_usr(cmd_usr):
#     cmd_map = {
#     'iniciar' : 'start',
#     'sim' : 'yes',
#     'não' : 'no',
#     'sair':'quit',
#     }
#     tokens = cmd_usr.split()
#     if tokens[0].lower() in cmd_map:
#         tokens[0] = cmd_map[tokens[0].lower()]
#         return " ".join(tokens)
#     else:
#         return False

def decode_cmd_usr(cmd_usr):
    cmd_map = {
    'iniciar' : 'start',
    'sim' : 'yes',
    'nao' : 'no',
    'sair':'quit',
    }
    tokens = cmd_usr
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
        msg_status = dados.decode().split('\n')[0]
        dados = dados.decode()[len(msg_status)+1:]
        #print('Dados: ',dados)
        #print('STATUS: ',msg_status)
        #cmd = cmd.split()
        #cmd = cmd.upper()
        if msg_status == 'QUIT':
            break
        elif msg_status == 'STARTING':
            #bem_vindo()
            print('Dados: ',dados)
            # IdentFind #
            
        elif msg_status == 'RC':
            # CHARQUEST #
            ...
            print('Dados: ',dados)
            
        elif msg_status == 'WIN':
            print('Dados: ',dados)
            ...
            # CHARQUEST #
sock.close()