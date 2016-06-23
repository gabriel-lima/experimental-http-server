import socket

HOST = 'localhost'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)

    if not data: break

    request = data.split(' ')

    print request

    method = request[0]
    path = request[1]
    protocol = request[2]

    try:
        if path == '/':
            path = 'index.html'

        page = open(path, 'r').read()
        status = '200 OK\r\n'
    except IOError:
        page = open('404.html').read()
        status = '404 Not Found\r\n'

    import datetime
    date = datetime.datetime.utcnow().strftime('%A, %d %B %Y %H:%M:%S')

    header = 'HTTP/1.1 ' + status + \
    'Location: http://localhost:8000/\r\n' + \
    'Date: ' + date + '\r\n' + \
    'Server: MeuServidor/1.0\r\n' + \
    'Content-Type: text/html\r\n' + \
    'Content-Length: ' + str(len(page)) + '\r\n' + \
    'Connection: close\r\n\r\n'

    conn.sendall(header + page)

conn.close()
