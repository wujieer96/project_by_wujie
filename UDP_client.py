#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'kzc', b'qwe', b'asd']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

s.close()201752011003