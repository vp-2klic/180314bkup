import socket
import sys
import types

def ListenServer():
    # Listen init signal from Server to send data

    any_host = ''                 # Symbolic name meaning all available interfaces
    udp_port = 5000              # Arbitrary non-privileged port

    # UDP Socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((any_host, udp_port))
    data, addr = udp_socket.recvfrom(1024)
    print data 

    test_host = socket.gethostbyname("<broadcast>")
    type_host = type(test_host)
    print type_host
#     if data == 'Authen':
    if 'Authen' in data:
        SocketConnect(addr[0])

def SocketConnect(tcp_host):
    # Connect to Server to send data
    print tcp_host
    tcp_port = 6000              # The same port as used by the server

    # Create Socket
    print "Create Socket"
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: %s" %e
        sys.exit(1)

    # Connect
    print "Connect"
    try:
        tcp_socket.connect((tcp_host, tcp_port))
    except socket.error, e:
        print "Connection error: %s" %e
        sys.exit(1)

    # Send Data
    print "Send Data"
    try:
        tcp_socket.sendall('Hello, world')
    except socket.error, e:
        print "Error sending data: %s" % e
        sys.exit(1)


    # Close Socket
    tcp_socket.close()
    print "Close Socket"

ListenServer()
