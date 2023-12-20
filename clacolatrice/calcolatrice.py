import json
import socket

# d = {'alpha': 1, 'beta': 2}
# s = json.dumps(d)
# open("out.json","w").write(s)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

n1 = float(input("inserisci il primo numero "))
op = input("inserisci l'operazione ")
n2 = float(input("inserisci il secondo numero "))

messaggio = {'primoNumero': n1, 'operazione': op, 'secondoNumero': n2}
messaggio = json.dumps(messaggio) # oggetto in stringa

s.sendall(messaggio.encode("UTF-8"))
data=s.recv(1024)
print("risulatto: ",data.decode())
