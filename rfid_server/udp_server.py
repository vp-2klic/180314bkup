import socket

def get_ip():
  tmp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  tmp.connect(("8.8.8.8", 80))
  tmp_ip = tmp.getsockname()[0]
  tmp.close()
  return tmp_ip

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#host = get_ip()
host = socket.gethostbyname("")
print("Host IP: %s" % host)

port = 5000

udpsocket.bind((host, port))

while True:

  data_udp, addr_udp = udpsocket.recvfrom(1024)
  udpsocket.sendto("helloclient",addr_udp)
  print("Got a UDP connection from %s" % str(addr_udp))
  print("UDP Data receive: %s" % data_udp)

#  clientsocket.send("hello")
#  clientsocket.close()
#  udpsocket.close()
