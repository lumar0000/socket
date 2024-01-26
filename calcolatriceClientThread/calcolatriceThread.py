import socket, sys, random, os, time, threading, json, multiprocessing

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15

def genera_richiesta(addres,port):
    start_time_thread = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((addres, port))
        v = ["-", "+", "/", "*", "%"]
        primoNumero = random.randint(0, 10)
        operazione = random.randint(0, 4)
        secondoNumero = random.randint(0, 10)

        messaggio = {'primoNumero' : primoNumero,
                    'operazione' : v[operazione],
                    'secondoNumero' : secondoNumero}
        messaggio = json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))

        data = sock_service.recv(1024)
        print('risultato: ', data.decode())
        print(f"{threading.current_thread().name} execution time =",  time.time() - start_time_thread)

if __name__ == '__main__':
    start_time = time.time()
    threads = [threading.Thread(target=genera_richiesta, args=(SERVER_ADDRESS, SERVER_PORT,)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("total threads time=", end_time - start_time)