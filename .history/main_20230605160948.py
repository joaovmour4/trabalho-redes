from socket import *
import os

def send(clientSocket, command):
    clientSocket.send(command.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)

msg = 'VAI TOMAR NO CU SILMAR E BRUNO E DAYANA, DEPOIS DA VIAGEM PARA SALINAS'
endmsg = '\r\n.\r\n'

mailserver = ('mail.rockdian.com', 25)

sender = 'alguem@algum.com'
rcpt = 'fibemi6062@rockdian.com'
subject = 'Contrato de trabalho pra eu sair daquele caralho daquela empresa chamada MG CONTABILIDADE'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
recv = recv.decode()
print(f'Message after connection request: {recv}')

command = f'EHLO {sender[-9:]}\r\n'
send(clientSocket, command)

command = f'MAIL FROM:{sender}\r\n'
send(clientSocket, command)

command = f'RCPT TO: {rcpt}\r\n'
send(clientSocket, command)

command = 'DATA\r\n'
clientSocket.send(command.encode())

command = f'Subject: {subject}\r\n'
clientSocket.send(command.encode())

clientSocket.send(msg.encode())

send(clientSocket, endmsg)
if clientSocket.recv(1024).decode()[:3] == '250':
    if not os.path.exists('Caixa de Saída'):
        os.mkdir('Caixa de Saída')
    with open(f'Caixa de Saída/{subject}.txt', 'w') as email:
        email.writelines(msg)
else:
    if not os.path.exists('Caixa de Entrada'):
        os.mkdir('Caixa de Entrada')
    with open(f'Caixa de Entrada/{subject}.txt', 'w') as email:
        email.writelines(msg)


send(clientSocket, 'QUIT\r\n')