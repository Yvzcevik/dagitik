import socket

s = socket.socket()
host = "127.0.0.1"
port = 12345
s.bind ((host, port))
s.listen(5)
while True:
    print "Waiting for connection"
    c, addr = s.accept()
    print 'Got a connection from', addr
