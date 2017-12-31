#!/usr/bin/env python

import socket
import os
import time
import base64
import progressbar
import logging

FILE_PATH = '/home/ray/file/images'
HOST = 'www.ray-xyz.com'
# HOST = 'localhost'
PORT = 8888
DATA_SECTION_SEPARATOR = '<-=+=->'
DATA_BLOCK_SIZE = 1 << 10

class ImgSocketClient:
    def __init__(self, sock=None):
        print('Initializing...')
        progressbar.streams.wrap_stderr()
        logging.basicConfig()

    def connect(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send_data(self, data):
        print('sending data...')
        self.connect(HOST, PORT)
        try:
            total_sent = 0
            bar = progressbar.ProgressBar()
            num_blocks_of_data = len(data) / DATA_BLOCK_SIZE
            for i in bar(range(num_blocks_of_data)):
                # logging.error('Sending %d', i)
                sent = self.sock.send(data[total_sent:((i + 1) * DATA_BLOCK_SIZE)])
                if sent == 0:
                    raise RuntimeError('socket connection broken')
                total_sent = total_sent + sent

            # while totalsent < len(data):
            #     sent = self.sock.send(data[totalsent:])
            #     if sent == 0:
            #         raise RuntimeError('socket connection broken')
            #     totalsent = totalsent + sent
            print('sending data complete.')
        finally:
            print('closing socket...')
            self.sock.close()

class Uploader:
    def __init__(self):
        print('Initializing uploader...')
        new_files = []
        self.imgsockcli = ImgSocketClient()

    def files_to_timestamp(self, path):
        files = [os.path.join(path, f) for f in os.listdir(path)]
        return dict([(f, os.path.getmtime(f)) for f in files])

    def prepare_data(self, data_name, effective_data):
        return base64.encodestring(data_name + DATA_SECTION_SEPARATOR + effective_data)

    def watch(self, path_to_watch, interval=5):
        # path_to_watch = sys.argv[1]
        print("Watching {}".format(path_to_watch))
        before = self.files_to_timestamp(path_to_watch)
        while True:
            time.sleep(interval)
            after = self.files_to_timestamp(path_to_watch)
            new_files = [f for f in after.keys() if not f in before.keys()]
            # print('ther are {} file to be sended.'.format(len(new_files)))
            if new_files:
                for f in new_files:
                    file = open(f, 'r')
                    print('file base name => {}'.format(os.path.basename(f)))
                    data = self.prepare_data(os.path.basename(f), file.read())
                    print('sending file {} to remote server'.format(f))
                    self.imgsockcli.send_data(data)
                    print('sending file {} done.'.format(f))
                    file.close()
            before = after

uploader = Uploader()
uploader.watch(FILE_PATH, 3)