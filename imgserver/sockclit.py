#!/usr/bin/env python

import socket
import os
import time
import base64

file_path = '/home/ray/file/images'
# host = 'www.ray-xyz.com'
host = 'localhost'
port = 8888
DATA_SECTION_SEPARATOR = '<$$$$$>'

class ImgSocketClient:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('ready to connect to server...')
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send_data(self, data):
        print('sending data...')
        try:
            totalsent = 0
            while totalsent < len(data):
                sent = self.sock.send(data[totalsent:])
                if sent == 0:
                    raise RuntimeError('socket connection broken')
                totalsent = totalsent + sent
            print('sending data complete.')
        finally:
            print('closing socket...')
            self.sock.close()

class Uploader:
    def __init__(self):
        print('Initializing uploader...')
        new_files = []
        self.imgsockcli = ImgSocketClient()
        self.imgsockcli.connect(host, port)

    def files_to_timestamp(self, path):
        files = [os.path.join(path, f) for f in os.listdir(path)]
        return dict ([(f, os.path.getmtime(f)) for f in files])

    def encode_data(self, data):
        return base64.encodestring(data)

    def prepare_data(self, data_name, effective_data):
        return self.encode_data(data_name + DATA_SECTION_SEPARATOR + effective_data)

    def watch(self, path_to_watch, interval=5):
        # path_to_watch = sys.argv[1]
        print("Watching {}".format(path_to_watch))
        before = self.files_to_timestamp(path_to_watch)
        while True:
            time.sleep (interval)
            after = self.files_to_timestamp(path_to_watch)
            new_files = [f for f in after.keys() if not f in before.keys()]
            if new_files: print "new_files: ", ", ".join(new_files)
            # print('ther are {} file to be sended.'.format(len(new_files)))
            for f in new_files:
                file = open(f, 'r')
                print('file base name => {}'.format(os.path.basename(f)))
                data = self.prepare_data(os.path.basename(f), file.read())
                print('sending file {} to remote server'.format(f))
                self.imgsockcli.send_data(data)
                print('sending file {} done.'.format(f))
            before = after


# imgsockcli.send_data('Hi, I am from socket client!!!')

uploader = Uploader()
uploader.watch(file_path, 3)