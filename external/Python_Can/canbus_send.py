#!/usr/bin/python3

import socket
import struct
import sys

can_frame_fmt = "=IB3x8s"

def build_can_frame(can_id, data):
    can_dlc = len(data)
    print(data)
    data = data.ljust(8, b'\x00')
    return struct.pack(can_frame_fmt, int(can_id), can_dlc, data)
 

if len(sys.argv) < 4:
    print('Usage: ./canbus_send.py iface CANID(int) data(byte) [data(byte)] [...]')
    sys.exit(0)

s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind((sys.argv[1],))

 
try:
    data = b''
    for i in sys.argv[3:]:
        data += struct.pack("B", int(i))
    s.send(build_can_frame(sys.argv[2], data))
except socket.error:
    print('Error sending CAN frame')

