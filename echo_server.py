import sys, socket, thread

#ECHO SERVER CLASS
class echo_server:
    #Create an echo socket
    def __init__(self, host, port):
        self.echo_sock = new_socket(host, port)
        self.echo_sock.send('echo')
    #Run the main loop.
    #Listen for data, upon receive either forward it back up through the
    #echo server & print client data otherwise close the socket on error
    def run_loop(self):
        listening = True
        while listening:
            data = self.echo_sock.recv(4096)
            if data is not None:
                self.echo_sock.send(data)
                if data == 'new_client':
                    self.echo_sock = new_socket(host, port)
                    self.echo_sock.send('client')
                print data
            else:
                listening = False
        self.echo_sock.close()

def new_socket(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
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
    #Build the echo server and run the main loop
    server = echo_server(host, port)
    try:
        server.run_loop()
    except KeyboardInterrupt:
        print 'Ctrl-C'
        sys.exit(1)
