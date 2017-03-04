import sys, socket, thread

class echo_server:
    def __init__(self, host, port):
        self.echo_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.echo_sock.connect((host, port))
        self.recv_data = self.echo_sock.recv(4096)
        print self.recv_data
    def run_loop(self):
        listening = True
        while listening:
            client_data = self.echo_sock.recv(4096)
            if client_data is not None:
                self.echo_sock.send(client_data)
            else:
                listening = False
        self.echo_sock.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        host = 'localhost'
        port = 3000
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])

    server = echo_server(host, port)

    try:
        server.run_loop()
    except KeyboardInterrupt:
        print 'Ctrl-C'
        sys.exit(1)
