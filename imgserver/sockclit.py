#!/usr/bin/env python

import socket
from os import walk
from filewatcher import FileWatcher

file_path = '/home/ray/file/images'
# host = 'www.ray-xyz.com'
host = 'localhost'
port = 8888

class ImgSocketClient:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('ready to connect to server...')
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send_data(self, msg):
        print('sending data...')
        try:
            totalsent = 0
            while totalsent < len(msg):
                sent = self.sock.send(msg[totalsent:])
                if sent == 0:
                    raise RuntimeError('socket connection broken')
                totalsent = totalsent + sent
            print('sending data complete.')
        finally:
            print('closing socket...')
            self.sock.close()

class ImgUploader:
    def __init__(self):
        print('Initializing image uploader...')

    # def check_imgs(self):
    #     files []
    #     for (dirpath, dirnames, filenames) in walk(file_path):
    #         files.extend(filenames)
    #         break
    #     print(files)

imgsockcli = ImgSocketClient()
imgsockcli.connect(host, port)
imgsockcli.send_data('Hi, I am from socket client!!!')
print('Starting watcher...')
watcher = FileWatcher()
watcher.watch(file_path)
print('The file watcher started.')