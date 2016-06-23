import socket

HOST = 'localhost'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
