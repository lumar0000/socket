import socket
import json

# Configurazione del server
IP = "127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

# Creazione della socket del server con Il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

  sock_server.bind((IP, PORTA))
  sock_server.listen()
  print(f"Server n ascolto su {IP}:{PORTA}...")

  while True:
    sock_service, address_clent = sock_server.accept()
    
    dati = sock_service.recv(DIM_BUFFER).decode()
    dati = json.loads(dati)
    n1=dati['primoNumero']
    op=dati['operazione']
    n2=dati['secondoNumero']
    with sock_service as sock_client:
        tot=0
        if not dati:
            break
        if op == '+':
            tot = n1 + n2
        if op == '-':
            tot = n1 - n2
        if op == '*':
            tot = n1 * n2
        elif op == "/":
            if n2 != 0:
                tot = n1 / n2
            else:
                tot = "Impossibile"
        elif op == "%":
            tot = n1 % n2

        # Stampa il messaggio ricevuto e invia una risposta al client
        print(f"Ricevuto messaggio dal client {sock_service}: {dati}")
        sock_service.sendall(str(tot).encode())