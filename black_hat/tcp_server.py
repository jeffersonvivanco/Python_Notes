import socket
import threading

# TODO: Look up what is a tcp server
# TODO: Look up threading lib
# TODO: Read about decoding and encoding messages

bind_ip = '0.0.0.0'
bind_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

# tells the server to start listening with a max backlog of connections set to 5
server.listen(5)

print('[*] Listening on %s:%d' % (bind_ip, bind_port))

# this is our client handling thread
# the handle client function performs the recv() and then sends a simple message
# back to the client
def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)

    print('[*] Received %s' % request.decode())

    # send back a packet
    client_socket.send('ACK!'.encode())

    client_socket.close()

# main loop where server is waiting for incoming connection
while True:
    # When a client connects, we receive the client socket into the client variable, and
    # the remote connection details into the addr variable
    client, addr = server.accept()

    print('[*] Accepted connection from %s:%d' % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    # start the thread to handle client connection
    client_handler.start()

