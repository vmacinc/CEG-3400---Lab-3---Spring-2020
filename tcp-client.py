import socket

# Code sample from https://nostarch.com/blackhatpython
# Forked from https://github.com/WillPennell/Python

target_host = "www.wright.edu"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send('GET / HTTP/1.1\r\nHost: www.wright.edu\r\n\r\n')

# receive data
response = client.recv(4096)

print response

