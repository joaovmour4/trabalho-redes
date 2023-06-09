from socket import *
import os

def send(clientSocket, command):
    clientSocket.send(command.encode())
    recv = clientSocket.recv(1024).decode()
    return recv

msg = 'algum texto'
endmsg = '\r\n.\r\n'

mailserver = ('mail.rockdian.com', 25)

sender = 'alguem@algum.com'
rcpt = 'fibemi6062@rockdian.com'
subject = 'Cabeçalho teste'
subject = 'Assunto teste'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
recv = recv.decode()

command = f'EHLO {sender[-9:]}\r\n'
send(clientSocket, command)

command = f'MAIL FROM:{sender}\r\n'
send(clientSocket, command)

command = f'RCPT TO: {rcpt}\r\n'
send(clientSocket, command)
recv_rcpt = send(clientSocket, command)
if recv_rcpt[:3] != '250':
    subject = subject + ' ; e-mail destinatário não encontrado!'

command = 'DATA\r\n'
clientSocket.send(command.encode())

command = f'Subject: {subject}\r\n'
clientSocket.send(command.encode())

clientSocket.send(msg.encode())
send(clientSocket, endmsg)
recv_mailSend = clientSocket.recv(1024).decode()

if recv_mailSend[:3] == '250':
    if not os.path.exists('Caixa de Saída'):
        os.mkdir('Caixa de Saída')
    with open(f'Caixa de Saída/{subject}.txt', 'w') as email:
        email.writelines(msg)
else:
    if not os.path.exists('Caixa de Entrada'):
        os.mkdir('Caixa de Entrada')
    with open(f'Caixa de Entrada/{subject}.txt', 'w') as email:
        email.writelines(msg)

if recv_mailSend[:3] != '250':
    print('Falha no envio do e-mail, verifique as informações e tente novamente!')
else:
    print('E-mail enviado com sucesso!')


send(clientSocket, 'QUIT\r\n')