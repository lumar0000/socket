import socket
import json

HOST = "127.0.0.1"  # Indirizzo del server
PORT = 22224        # Porta usata dal server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
  sock_service.connect((HOST, PORT))
  while True:
    comando = input("comando: ").split("/")

    messaggio = {
        "comando": comando[0]
    }
    if(comando[0] == "#get " or comando[0] =="#set " or comando[0]=="#put "):
        messaggio["nomeStud"] = comando[1]
    if(comando[0]=="#put "):
       messaggio["materia"] = comando[2]
       messaggio["voto"] = comando[3]
       messaggio["ora"] = comando[4]

    print(messaggio)

    messaggio = json.dumps(messaggio)
    sock_service.sendall(messaggio.encode("UTF-8"))

    data = sock_service.recv(1024)
    data = json.loads(data)

    print(data["messaggio"], data["valori"])





#    messaggio = json.dumps(messaggio)
