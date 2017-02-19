# tcp-relay
Example session:
$ ./relay 8080 &
$ ./echoserver localhost 8080 &
established relay address: localhost:8081
$ telnet localhost 8081
Hello, world
Hello, world
