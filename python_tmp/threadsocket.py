import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient, args = (client, address))

    def listenToClient(self, client, address):
        while True:
            try:
                data = client.recv(size)
                if data:
                    response = data
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()        
                return False

if __name__ == "__main__":
    while True:
        port_num = input("Port Number? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('192.168.0.6',port_num).listen()
