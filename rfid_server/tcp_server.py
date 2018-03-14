import socket

def get_ip():
  tmp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  tmp.connect(("8.8.8.8", 80))
  tmp_ip = tmp.getsockname()[0]
  tmp.close()
  return tmp_ip

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = get_ip()
print("Host IP: %s" % host)

port = 5000

tcpsocket.bind((host, port))
tcpsocket.listen(5)

while True:

  client_tcp, addr_tcp = tcpsocket.accept()
#  data_tcp = tcpsocket.recv(1024)
  data_tcp = client_tcp.recv(1024)
  client_tcp.send("hello client")
  print("Got a TCP connection from %s" % str(addr_tcp))
  print("TCP Data receive: %s" % str(data_tcp))
#  print("TCP Data receive: %s" % data_tcp)
  client_tcp.close()

#  clientsocket.send("hello")
#  clientsocket.close()
