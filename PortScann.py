#!/usr/bin/python

import socket
s.settimeout(5)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip=input("Enter IP: ")
port=int(input("Enter port: "))

def PortScann(port):
    if s.connect_ex((ip,port)):
        print("Port closed")
    else:
        print("Port open")

PortScann(port)
