# tcp-relay
Example session:
```sh
$ ./relay 8080 &
$ ./echoserver localhost 8080 &
established relay address: localhost:8081
$ telnet localhost 8081
Hello, world
Hello, world
```
How to enable a program to use this TCP Relay:
1) Install the relay server somewhere it is accessible. (i.e: an S3 bucket for the relay to live)
2) Establish a connection to the relay server using the example echo server to test the connection. The echo server will accept data and forward it back to a client that has connected. In order to run a program instead of send a message configure the echo server to execute the program upon accept of a client. The relevant function in echo_server.py is run_loop(). 
