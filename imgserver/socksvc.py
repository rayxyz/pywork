import socket

class ImgSocketServer:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind the socket to the port
            server_address = ('localhost', 8888)
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
                    data = conn.recv(32)
                    if data:
                        print('data recevied => {}'.format(data))
                    else:
                        print('receiving data finished.')
                        break
                    bytes_recd = bytes_recd + len(data)
                print('received all the data.')
            finally:
                print('finished a connection request.')
                # print('closing socket server connection')
                conn.close()
            print('The lenth of bytes received => {}'.format(bytes_recd))

print('running the image server....')
imgsock = ImgSocketServer()
print('create image server complte, ready to receive data')
imgsock.recv_data()