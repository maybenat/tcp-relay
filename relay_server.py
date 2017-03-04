import sys, socket, thread

class relay_server:
    def __init__(self, host, port):
        self.relay_sock = new_socket(host, port)
        self.echo_port_list = []

    def run_loop(self):
        while 1:
            echo_sock, echo_addr = self.relay_sock.accept()
            thread.start_new_thread(self.on_accept, (echo_sock, host, port))

    def on_accept(self, echo_sock, host, port):
        if len(self.echo_port_list) < 1:
            echo_port = port + 1
            self.echo_port_list.append(echo_port)
        else:
            echo_port = self.echo_port_list[len(self.echo_port_list)-1]
            self.echo_port_list.append(echo_port)
        echo_message = 'HOST: '+ host + ' PORT: ' + str(echo_port)
        echo_sock.send(echo_message )

        #now we are handing client connections to echo_port
        client_sock = new_socket(host, echo_port)
        client_sock, client_addr = client_sock.accept()

        listening = True
        while listening:
            client_info = client_sock.recv(4096)
            if client_info is not None:
                client_sock.send(client_info)
            else:
                listening = False
        echo_sock.close()
        client_sock.close()


def new_socket(host, port):
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
    if len(sys.argv) < 2:
        host = 'localhost'
        port = 3000
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])

    server =  relay_server(host, port)
    try:
        server.run_loop()
    except KeyboardInterrupt:
        print 'Ctrl-C'
        sys.exit(1)
