#!/usr/bin/env python

"""
EE450 Homework 3 Server - STUB
Dr. Genevieve Bartlett
Fall 2017
"""

# You are not required to use any of the code in this stub,
# however you may find it a helpful starting point.
from collections import deque
import time
import socket
import sys
import select
import threading
host='128.125.208.186'
port=65520
localhost='127.0.0.1'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def init_server():
    global s
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #s.bind((host,port))
    s.bind((localhost,port))
    s.listen(5)
    s.settimeout(1000*10)
def behave(client,address):
    size = 0
    while True:
        data=client.recv(1000).decode('utf-8')
        if not data:
            break
        if len(data)==1000: 
            size=size+1
            print("Received 1000 bytes from client"+str(client.getpeername()) +". Total: "+str(1000*size))
    client.close()
def run_loop():
    global s
    while True:
        try:
            client,address=s.accept()
            print "client connecting:"+str(client.getpeername())
            thread = threading.Thread(target=behave,args=(client,address))
            thread.start()
        except KeyboardInterrupt:
            s.close()
            return
        except Exception as e:
            print("Unhandled exception 0: %s" % e)
            return
    s.close()    
if __name__ == "__main__":
    init_server()
    run_loop()
