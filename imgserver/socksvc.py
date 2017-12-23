#!/usr/bin/env python

import socket

HOST = 'localhost'
PORT = 8888
DATA_BLOCK_SIZE = 1 << 10

class ImgSocketServer:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind the socket to the port
            server_address = (HOST, PORT)
            print('starting up on {}'.format(server_address))
            self.sock.bind(server_address)
            self.sock.listen(1)
        else:
            self.sock = sock

    def recv_data(self):
        while True:
            # Wait for a connection
            print('waiting for a connection')
            bytes_recd = 0
            conn, client_address = self.sock.accept()
            try:
                print('reading data...')
                while True:
                    data = conn.recv(DATA_BLOCK_SIZE)
                    if data:
                        print('data recevied => {}'.format(data))
                    else:
                        break
                    bytes_recd = bytes_recd + len(data)
                print('receiving data finished.')
            finally:
                # conn.close()
            print('The lenth of bytes received => {}'.format(bytes_recd))



print('running the image server....')
imgsock = ImgSocketServer()
print('create image server complte, ready to receive data')
imgsock.recv_data()