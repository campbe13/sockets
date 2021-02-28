#!/usr/bin/env python3 
'''
create a socket for local connection only
listen on localhost:8111
read the data sent by client
and send it back to the client
demonstrating simple sockets for 440

good ref for students http://realpython.com/python-sockets/

p.m.campbell
2021-02-26
'''
import socket
import logging as log

''' 
socket closed when client killed or quit\n\n given
ex: nc -v -n 127.0.0.1 8111
'''

def makeSocket(IP, PORT):
   ''' address family: INET, socket type: STREAM '''
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.bind((IP,PORT))
      sock.listen()
      connection, address = sock.accept()
      with connection:
        log.info('New connection, addr ')
        log.info(address)
        while True:
           payload = connection.recv(1024)  # receive 
           if not payload:
             break
           # default UTF-8
           data = payload.decode()
           if data.startswith('quit'):
             log.info("quit requested ")
             connection.close()
             break
           log.info("received: "+ data.rstrip('\n'))
           connection.sendall(payload) # send

IP  = "127.0.0.1"  # loopback
PORT = 8111	   # unassigned, non privileged ports > 1023

# filemode defaults to a, append
#log.basicConfig(level=log.DEBUG, filename='sockets.log', format='%(asctime)s-%(process)d-$(levelname)s-%(name)s-%(message)s')
log.basicConfig(level=log.DEBUG, filename='sockets.log', format='%(asctime)s: pid%(process)d   %(message)s')
log.info(f'binding to {IP}:{PORT}')

makeSocket(IP, PORT)
