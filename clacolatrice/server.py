import json
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# creazione del socket
cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cs.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi...")

while True:
    #ricezione dei dati del client
    data, addr=cs.recv(1024)

    if not data:
        break
    data=data.decode()
    data.json(data)
    n1=data['primoNumero']
    op=data['operazione']
    n2=data['secondoNumero']

    if op == '+':
        tot = n1 + n2
    if op == '-':
        tot = n1 - n2
    if op == '*':
        tot = n1 * n2
    if op == '/':
        tot = n1 / n2

    cs.sendto(tot.encode(), addr)
