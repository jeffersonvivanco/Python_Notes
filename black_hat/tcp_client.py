import socket

# TODO: Read what is a tcp client, overall what is tcp
# TODO: socket python lib???


target_host = '0.0.0.0'
target_port = 80

# create a socket object
# AF_INET is saying we are going to use standard IPv4 address or hostname
# SOCK_STREAM indicates that this will be a tcp client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send('Hello'.encode())

# receive some data
response = client.recv(4096)

print(response.decode())

