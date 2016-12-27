#!/usr/bin/python3

import socket
import struct
import sys

can_frame_fmt = "=IB3x8s"

def dissect_can_frame(frame):
    can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
    return (can_id, can_dlc, data[:can_dlc])

if len(sys.argv) != 2:
    print('Usage: ./canbus_listen.py iface')
    sys.exit(0)

s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind((sys.argv[1],))

while True:
 
    cf, addr = s.recvfrom(16)
 
    print('Received: can_id=%x, can_dlc=%x, data=%s' % dissect_can_frame(cf))

