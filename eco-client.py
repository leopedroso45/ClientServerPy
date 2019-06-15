#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def connect(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    self.sock.connect((HOST, PORT))
    self.logger.debug('Seve port {}'.format(PORT))

    #login = create_aprs_login(self.aprs_user, -1, settings.APRS_APP_NAME, settings.APRS_APP_VER, self.aprs_filter)
    self.sock.send(login.encode())
    self.sock_file = self.sock.makefile('rw')

    self._kill = False 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    if s.connect((HOST, PORT)) != False:
        s.sendall(b'Tentando conectar...')
    
        while s._closed != True:
            if s.recv(1024):
                print('Received',s.recv(1024))#, repr(data))           
        #data = s.recv(1024)
        if s._closed == False:
            s.sendall(b'Fechando conexao!')
            data = s.recv(1024)
            print('Received', repr(data))
            s.close


#print('Received', repr(data))
