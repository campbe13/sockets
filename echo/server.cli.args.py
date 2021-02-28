#!/usr/bin/env python3 
'''
create a socket for local connection only
listen on localhost:8111
read the data sent by client
and send it back to the client
demonstrating simple sockets for 440

p.m.campbell
2021-02-26
'''
import socket
import sys
import getopt

def makeSocket():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.bind((IP,PORT))
      sock.listen()
      connection, address = sock.accept()
      with connection:
        print("New connection, addr", address)
        while True:
           payload = connection.recv(1024)  # receive 
           if not payload:
             break
           connection.sendall(payload) # send
def checkargs():
   try:
     opts, args = getopt.getopt(sys.argv,"i:p")
   except:
     print(opts)
     print(args)
     print('server.py -i <ip address> -p <port>')
     sys.exit(5)
   for opt, arg in opts:
     if opt == '-i':
       IP = arg
     else:
       PORT = arg
   return IP, PORT

IP  = "127.0.0.1"  # loopback
PORT = 8111	   # unassigned, non privileged ports > 1023
IP, PORT = checkargs()
print (f"Will listen on {IP}:{PORT}")
makeSocket(IP, PORT)


