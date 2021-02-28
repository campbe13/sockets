# code for creating sockets
for teaching/learning about sockets
the underlying TCP transport layer comms channel
for all internet protocols
#  echo
see echo/server.py   logs to socket.log (appends, you may have to delete old)
* run in background `./server.py &`
   * binds to 127.0.0.1:8111
   * check it with `netstat -lan |less`  note the state LISTSEN
   * if it crashes or has just ended the ip&port may still be bound, in a TIME_WAIT status instead of LISTEN,
     you can see this through netstat, you will have to wait for it to end
* fake out client comms with netcat ` nc -v -n 127.0.0.1 8111`
   * will echo the data you type in back at you
   * `quit` will end the connection
   * check the socket source & dest while you are talking to the server `netstat -lan|less`
# Questons: 
1.  Can you talk to it from another user on the same box?   Why or  why not?
1.  Can you talk to it from another box?   Why or why not?
1.  Can you run the server code many times in the background?  Why or why not?
1.  Can you run the server code using a different port? 
	1. copy the code to server2.py, change the port 
	2. run both `./server.py &` and `./server2.py &` at the same time, in the background
	3. does it work? Why or why not?

# multi connections
