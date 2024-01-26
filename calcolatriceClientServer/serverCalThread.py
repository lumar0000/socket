import socket,json
from threading import Thread 

# Configurazione del server
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224

def ricevi_comandi(sock_service, addr_client):
    while True:
        dati = sock_service.recv(1024).decode()
        if not dati:
            break
        dati = json.loads(dati)
        n1=dati['primoNumero']
        op=dati['operazione']
        n2=dati['secondoNumero']
        tot=0
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
        elif op == 0:
            break
        # Stampa il messaggio ricevuto e invia una risposta al client
        print(f"Ricevuto messaggio dal client {sock_service}: {dati}")
        sock_service.sendall(str(tot).encode())
    sock_service.close()

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nconnessione ricevuta da %s" % str(addr_client))
        print("creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_listen:
            sock_listen.bind((indirizzo, porta))
            sock_listen.listen()
            ricevi_connessioni(sock_listen)

    except:
        print("socket non creato")

if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("termina")