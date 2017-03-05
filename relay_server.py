import sys, socket, thread

#RELAY SERVER CLASS
class relay_server:
    #Initialize the relay server with a new socket & list of ports
    def __init__(self, host, port):
        self.relay_sock = new_socket(host, port)
        self.echo_port_list = []

    #Run the main loop to listen for incoming connections
    #On accept start a new thread and handle the echo socket connection
    def run_loop(self):
        while 1:
            echo_sock, echo_addr = self.relay_sock.accept()
            thread.start_new_thread(self.on_accept, (echo_sock, host, port))

    #When a new echo socket connection has been made
    def on_accept(self, echo_sock, host, port):
        #Configure the correct host & port to be sent back to the echo socket connection
        #If this is the first connection increment current port by 1 and append to port list
        if len(self.echo_port_list) < 1:
            echo_port = port + 1
            self.echo_port_list.append(echo_port)
        #Otherwise increment last port in the list by one and append
        else:
            echo_port = self.echo_port_list[len(self.echo_port_list)-1]
            self.echo_port_list.append(echo_port)
        #configure and send back the message to the echo socket
        echo_message = 'established relay address: '+ host + ':' + str(echo_port)
        echo_sock.send(echo_message)

        #now we are handing client connections to echo_port
        client_sock = new_socket(host, echo_port)
        client_sock, client_addr = client_sock.accept()

        #Run a loop to listen for connections
        listening = True
        while listening:
            #Recieve 4096 bytes of data from the client
            client_info = client_sock.recv(4096)
            #Send back the data to the client if the client sent data
            if client_info is not None:
                client_sock.send(client_info)
            #Close the connection, something went wrong
            else:
                listening = False
        #If the loop has been exited, something has gone wrong
        #Close the echo socket and the client socket connections
        echo_sock.close()
        client_sock.close()

#Helper method to create a new socket
def new_socket(host, port):
    #Build a new socket according to the Python standards:
    #https://docs.python.org/2/howto/sockets.html
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(200)
    except socket.error, v:
        errorcode=v[0]
        if errorcode==errno.ECONNREFUSED:
            print "Connection Refused"
        self.socket.close()
        sys.exit(1)
    return sock

if __name__=='__main__':
    #Grab the host & port from the user.
    #If it doesn't exist use a default of 'localhost' 3000
    if len(sys.argv) < 2:
        host = 'localhost'
        port = 3000
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
    #Build the relay server and try to run the main loop
    server =  relay_server(host, port)
    try:
        server.run_loop()
    except KeyboardInterrupt:
        print 'Ctrl-C'
        sys.exit(1)
