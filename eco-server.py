#!/usr/bin/env python3
from threading import Timer
import threading
import time
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def timeout():
    print('Game Over')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    if conn & addr != False:
        print("BOA MALUCO")
    with conn:
        print('Connected by', addr)
        conn.sendall(b'Conexao estabelecida.')
        while True:
            data = conn.recv(1024)
            if not data:
                while not data:
                    conn._accept
                    t = Timer(10, timeout)
                    t.start()
                    t.join()
                    #print('Disconnected by', addr)
                    # break
            conn.sendall(data)
