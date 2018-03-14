import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.106'

port = 6000

s.connect((host, port))

# s.send("hello server".encode())

data = s.recv(1024)

s.close()

print data
