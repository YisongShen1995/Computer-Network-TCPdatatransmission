#!/usr/bin/env python

"""
EE450 Homework 3 Client - STUB
Dr. Genevieve Bartlett
Fall 2017
"""
from collections import deque
import time
import socket
import sys
import select
import random
our_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost='127.0.0.1'
def connect_to_server():
    global our_socket
    #server_address = ('128.125.208.186', 65520)
    server_address = (localhost, 65520)
    our_socket.connect(server_address)
    return
def send_message():
    global our_socket
    size=random.randint(2000,1000000)
    msg_to_send='0'*size
    our_socket.sendall(msg_to_send.encode('utf-8'))
if __name__ == "__main__":
    connect_to_server()
    send_message()
    

     
