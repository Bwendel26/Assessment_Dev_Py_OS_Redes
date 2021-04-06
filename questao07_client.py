# -*- coding: utf-8 -*-

import os
import time
import socket
import psutil
import pickle
from psutil._common import bytes2human

#CLIENT
msgFromClient = " Hello UDP Server"
bytesToSend = msgFromClient.encode('ascii')

serverAddressPort = (socket.gethostname(), 9991)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(5)
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
acknowledged = False

print('===' * 25, 'Questão 07'.center(75), '===' * 25, sep='\n')

while not acknowledged:
    try:
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        _msg = pickle.loads(msgFromServer[0])
        acknowledged = True
        for name in _msg._fields:
            value = getattr(_msg, name)
            if name == 'total' or name == 'available':
                value = bytes2human(value)
                print('%-10s : %7s' % (name.capitalize(), value))
    except socket.timeout:
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
UDPClientSocket.close()