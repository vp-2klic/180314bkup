#! /usr/bin/python3
import socket
import threading
import queue
import time
import logging

logging.basicConfig(level=logging.DEBUG, \
                    format='(%(threadName)-10s) %(message)s',)
def get_ip():
    tmp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tmp.connect(("8.8.8.8", 80))
    tmp_ip = tmp.getsockname()[0]
    tmp.close()
    return tmp_ip

class UDPThread(threading.Thread):
    udp_host = None
    stopper = None
    def __init__(self, rdaddr_queue, dladdr_queue, stopper):
        super().__init__()
        self.stopper = stopper
        self.rdaddr_queue = rdaddr_queue
        self.dladdr_queue = dladdr_queue
    def run(self):
        while not self.stopper.is_set():
            data_udp, addr_udp = udpsocket.recvfrom(1024)
            if ('RD01' in data_udp.decode()):
                self.rdaddr_queue.put(addr_udp[0])
                udpsocket.sendto("RDOK".encode(), addr_udp)
                print("Device RD01 was added at IP address %s", addr_udp[0])
            elif ('DL01' in data_udp.decode()):
                self.dladdr_queue.put(addr_udp[0])
                udpsocket.sendto("DLOK".encode(), addr_udp)
            print("Got UDP conn from %s" % addr_udp[0])
            print("UDP data: %s" % data_udp.decode())
            time.sleep(0.2)

class TCPThread(threading.Thread):
    stopper = None
    rdaddr_queue = None
    dladdr_queue = None
    def __init__(self, rdaddr_queue, dladdr_queue, stopper):
        super().__init__()
        self.rdaddr_queue= rdaddr_queue
        self.dladdr_queue= dladdr_queue
        self.stopper = stopper
    def run(self):
        while not self.stopper.is_set():
            rdaddr = self.rdaddr_queue.get() 
            dladdr = self.dladdr_queue.get() 
            print(rdaddr)
            print(dladdr)
#            client_tcp, addr_tcp = self.tcpsocket.accept()
#            data_tcp = client_tcp.recv(1024)
#            client_tcp.send("TCP hello".encode())
#            client_tcp.close()
#            print("Got TCP conn from %s" % addr_tcp[0])
#            print("TCP data: %s" % data_tcp.decode())
            time.sleep(0.2)

if __name__ == '__main__':
    rdaddr_queue = queue.Queue()
    dladdr_queue = queue.Queue()

    stopper = threading.Event()

    port = 5000

    udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_host = socket.gethostbyname("")
    udpsocket.bind((udp_host, port))
    udp = UDPThread(rdaddr_queue, dladdr_queue, stopper)

    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_host = get_ip()
    tcpsocket.bind((tcp_host, port))
    tcpsocket.listen(5)
    tcp = TCPThread(rdaddr_queue, dladdr_queue, stopper)

    udp.start()
    tcp.start()
    udp.join()
    tcp.join()
