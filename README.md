# tcp-relay
## How to get started 
  1. Clone the repo <br />
  2. cd into the project and run ```python relay_server.py localhost 3000``` (or whatever host/port you want). This will start a relay server which can accept connections from an echo server. <br />
  3. Run ```python echo_server.py localhost 3000``` to connect to the relay server. You will receive a message indicating the port and host you can now connect your clients to. <br />
  4. Use telnet to connect to the provided relay address. Type a command and the command will be echoed back to you. Configure additional steps of your liking here. (i.e: execute a program instead of receive just a message from the client) <br />
  5. You should be all set up with a relay server. :) 

###Example session:
```sh
$ ./relay 8080 &
$ ./echoserver localhost 8080 &
established relay address: localhost:8081
$ telnet localhost 8081
Hello, world
Hello, world
```
###How to enable a program to use this TCP Relay:<br />
  1. Install the relay server somewhere it is accessible. (i.e: an S3 bucket for the relay to live) <br />
  2. Establish a connection to the relay server using the example echo server to test the connection. The echo server will accept data and forward it back to a client that has connected. In order to run a program instead of send a message configure the the echo and relay servers to not just receive data but run a command upon accept of a client, the relevant code sections are run_loop(). 
