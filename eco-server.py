#!/usr/bin/env python3
from threading import Timer
from _thread import *
import threading
import time
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

print_lock = threading.Lock()

def timeout():
    print('Sem mensagens')

def timing():
    t = Timer(20, timeout)
    t.start()
    t.join()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    threading.th conn, addr = s.accept()
    if conn != False:
        print("Alguem esta se conectando...")
    with conn:
        print('Conectado com ', addr)
        while conn._closed != True:
            data = conn.recv(1024)
            timing()
            if not data:
                timing()
                s.close()

    conn.sendall(data)
