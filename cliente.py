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
    'nao' : '2805', #no
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
    '2409' : 'STARTING', #starting
    '2905' : 'RECEIVED', # recebeu a resposta
    '1001' : 'QUIT', # encerra conexão
    '1111' : 'CHARACTER', # personagem encontrado
    '4004' : 'ERROR INIT', # erro ao iniciar o jogo
    '4005' : 'ERROR ANSWER', # erro ao responder a pergunta
    '0001' : 'COMMAND ERROR', # erro no comando
    }
    tokens = protocol_svr
    if tokens.lower() in cmd_map:
        tokens = cmd_map[tokens.lower()]
        return tokens
    else:
        return False

def bem_vindo():
    print()
    print('\033[34m=\033[0m'*50)
    print('\033[34m=============\033[0m Bem vindo ao IdentFind!\033[34m============= \033[0m')
    print('\033[34m=\033[0m'*50)
    print('         \033[3m\033[92mcreated by: \033[0mbrunovs, alexls, alessandrorg\033[0m')
    print()
    print('> Para iniciar o jogo digite \033[96mINICIAR \033[0m')
    print('> Para sair digite \033[31mSAIR\033[0m ou \033[31mCTRL+C\033[0m')
    print('> Para responder as perguntas digite \033[92mSIM\033[0m ou \033[31mNAO\033[0m\n')
    

try:
    if len(sys.argv) > 1:
        HOST = sys.argv[1]
    print('Servidor:', HOST+':'+str(PORT))
    serv = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(serv)
    bem_vindo()
except ConnectionRefusedError:
    print('\nConexão recusada pelo servidor.\n')
    sys.exit()

while True:
    try:
        cmd_usr = input('\033[34mIdentF> \033[0m').upper().strip()
    except:
        cmd_usr = 'SAIR'
    cmd = decode_cmd_usr(cmd_usr)
    if not cmd:
        print('\033[31mComando indefinido:\033[0m', cmd_usr)
    else:
        sock.send(cmd.encode())
        dados = sock.recv(TAM_MSG)
        if not dados: break
        protocol_svr = dados.decode().split('\n')[0]
        msg_status = decode_cmd_svr(protocol_svr)
        dados = dados.decode()[len(protocol_svr)+1:]
        
        if msg_status == 'QUIT':
            print('\033[31m\nDesconectado do servidor.\033[0m')
            break
        
        elif msg_status == 'STARTING':
            print(f'\n \033[1mPergunta> \033[0m {dados}\n\033[3m\033[30m(responda sim ou nao)\033[0m\n')
            
        elif msg_status == 'RECEIVED':
            print(f'\n \033[1mPergunta> \033[0m {dados}\n\033[3m\033[30m(responda sim ou nao)\033[0m\n')
            #print(f'Pergunta> {dados}\n\033[3m\033[30m(responda sim ou nao)\033[0m\n')
            
        elif msg_status == 'CHARACTER':
            print(f'Seu personagem é \033[92m{dados}!\033[0m\n')
            
        elif msg_status == 'ERROR INIT':
            print('\n\033[31mErro ao iniciar o jogo.\033[0m\n')
        
        elif msg_status == 'ERROR ANSWER':
            print('\n\033[31mErro ao responder a pergunta, o jogo ainda nao foi iniciado.\033[0m\n')
            
        elif msg_status == 'COMMAND ERROR':
            print(f'\n\033[31mComando inválido:\033[0m {cmd_usr}\n')
            
sock.close()