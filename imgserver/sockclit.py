import socket

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

imgsockcli = ImgSocketClient()
imgsockcli.connect('localhost', 8888)
imgsockcli.send_data('Hi, I am from socket client!!!')