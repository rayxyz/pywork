#!/usr/bin/env python

import socket
import base64

HOST = 'localhost'
PORT = 8888
FILE_PATH = '/home/ray/file/images/recved'
DATA_BLOCK_SIZE = 1 << 10
DATA_SECTION_SEPARATOR = '<$$$$$>'

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
            data_recved = ''
            conn, client_address = self.sock.accept()
            try:
                print('reading data...')
                while True:
                    data = conn.recv(DATA_BLOCK_SIZE)
                    if data:
                        data_recved += data
                        print('data recevied => {}'.format(data))
                    else:
                        break
                    bytes_recd = bytes_recd + len(data)
                print('The lenth of bytes received => {}'.format(bytes_recd))
                print('data before decoded => {}'.format(data_recved))
                decoded_data = base64.decodestring(data_recved)
                print('decoded_data => {}'.format(decoded_data))
                data_sections = decoded_data.split(DATA_SECTION_SEPARATOR)
                print('length of data_sectons array => {}'.format(len(data_sections)))
                file_receved = FILE_PATH + '/' + data_sections[0]
                print('file_receved => {}'.format(file_receved))
                print('length of image => {}'.format(len(data_sections[1])))
                file_to_write = open(file_receved, 'w')
                lengthOfWritten = file_to_write.write(data_sections[1])
                print('length of content wrote => {}'.format(lengthOfWritten))
            finally:
                # conn.close()
                print('in finally block')



print('running the image server....')
imgsock = ImgSocketServer()
print('create image server complte, ready to receive data')
imgsock.recv_data()