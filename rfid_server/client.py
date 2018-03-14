import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
host = socket.gethostbyname("<broadcast>")
#host = '192.168.0.255'
print("Host is: %s" % host)

port = 5000
print("Port is: %s" % port)

#s.connect((host, port))

#data = s.recv(1024)

s.sendto("helloserver",(host,port))
data,addr = s.recvfrom(1024)

s.close()

print("data receive: %s" % data)
print("address response: %s" % str(addr))
