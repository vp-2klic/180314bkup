from netaddr import IPAddress
import socket
import sys
import ipaddress
import time


def FindAgent():
    udp_port = 5000          # Port use to find Agent

    #Find broadcast address

    """IPAddress("255.255.255.0").netmask_bits()        #Convert Subnet Mask to Prefix Length, Result is 24"""
    try :
        udp_host = str(ipaddress.ip_network(u'192.168.10.0/24')[-1])
    except ValueError as e :
        """e = sys.exc_info()[0]  # Find Exception you need"""
        print e

    # UDP client
    print udp_host 
    MESSAGE = "Authen"
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for x in range(0,2):
        udp_sock.sendto(MESSAGE, (udp_host, udp_port))


def ListenClient():
    # Listen Client sent data
    tcp_host = socket.gethostbyname_ex(socket.gethostname())
    usr_tmp = socket.gethostname()
    print usr_tmp
    print tcp_host
    tcp_port = 8000
    # TCP socket

    # Create Socket
    print "Create Socket"
    try:
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: %s" %e
        sys.exit(1)

    # Bind
    print "Bind"
    try:
        tcp_sock.bind((tcp_host, tcp_port))
    except socket.error, e:
        print "Error bind: %s" %e
        sys.exit(1)

    # Listen
    print "Listen"
    try:
        tcp_sock.listen(10)
    except socket.error, e:
        print "Error listen: %s" %e
        sys.exit(1)

    # Accept data from client
    print "Accept data from client"
    try:
        conn, addr = tcp_sock.accept()
        data = tcp_sock.recv(1024)
    except socket.error, e:
        print "Error listen: %s" %e
        sys.exit(1)

    print data
    tcp_sock.close()

# FindAgent()
ListenClient()
