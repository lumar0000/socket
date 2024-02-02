import socket,json
from threading import Thread 

# Configurazione del server
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224
pagella = {}

def ricevi_comandi(sock_service, addr_client):
    while True:
        dati = sock_service.recv(1024).decode()
        if not dati:
            break
        dati = json.loads(dati)
        messaggio = ""
        valori = ""
        if(dati["comando"] == "#list "):
            valori = pagella
        elif(dati["comando"] == "#get "):
            if(dati["nomeStud"] in pagella):
                valori = pagella[dati["nomeStud"]]
            else:
                messaggio = "studente non trovato"
        elif(dati["comando"] == "#set "):
            if(dati["nomeStud"] in pagella):
                messaggio = "studente già esistente trovato"
            else:
                pagella[dati["nomeStud"]]=[]
                messaggio = "studente inserito"
        elif(dati["comando"] == "#put "):
            if(dati["nomeStud"] in pagella and dati["materia"] not in pagella[dati["nomeStud"]]):
                pagella[dati["nomeStud"]].append([dati["materia"], dati["voto"], dati["ora"]])
                messaggio = "materia inserita"
            else:
                messaggio = "materia gia inserita"
        elif(dati["comando"] == "#close "):
            messaggio = "connessione chiusa"
        else:
            messaggio = "comando sbagliato"
            
        invio = {
            "messaggio": messaggio,
            "valori": valori
        }
        invio = json.dumps(invio)
        sock_service.sendall(invio.encode())
        
        if(dati["comando"] == "#close "):
            break
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