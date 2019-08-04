import socket

# TODO: Look up what is udp client
# Because udp is a connectionless protocol, there is no call to connect() beforehand

target_host = '0.0.0.0'
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto('AAABBBCCC'.encode(), (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)

