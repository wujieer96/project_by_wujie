#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999....')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s. ' % addr)
    s.sendto(b'Hello, %s!' % data, addr)