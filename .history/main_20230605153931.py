from socket import *
import os

def send(clientSocket, command):
    clientSocket.send(command.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)

msg = 'algum texto'
endmsg = '\r\n.\r\n'

mailserver = ('mail.rockdian.com', 25)

sender = 'alguem@algum.com'
rcpt = 'fibemi6062@rockdian.com'
subject = 'Cabeçalho teste'

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
print(clientSocket.recv(1024).decode())

if recv[:3] == '250':
    os.md

send(clientSocket, 'QUIT\r\n')