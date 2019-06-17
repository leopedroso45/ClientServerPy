#!/usr/bin/env python3

from threading import Timer
import threading
import time
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def timing():
    t = Timer(10)
    t.start()
    t.join()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    if s.connect((HOST, PORT)) != False:
        s.sendall(b'Conectado ao server...')
    
        while s._closed != True:
            s.sendall(b'Im here')
            #timing()
            time.sleep(10.0)
            if s.recv(1024):
                print('Received',s.recv(1024))#, repr(data))           
        #data = s.recv(1024)
        if s._closed == True:
            s.sendall(b'Fechando conexao!')
            data = s.recv(1024)
            print('Received', repr(data))
            s.close


#print('Received', repr(data))
