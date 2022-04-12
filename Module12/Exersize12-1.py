import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = input('Enter a url:')

if cmd == 'http://data.pr4e.org/intro-short.txt':
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
else:
    print(cmd)

try:
    mysock.send(cmd)
except:
    print('please enter a valid url.')
    quit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
