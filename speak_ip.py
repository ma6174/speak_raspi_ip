#!/usr/bin/env python
# coding=utf-8

import os
import time
import socket


voice_path = "/home/pi/speak_ip/voice"

def getLocalIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 0))
        return s.getsockname()[0]
    except:
        name = socket.gethostname()
        ip_addr = socket.gethostbyname(name)
        return ip_addr

def getFilePath(filename):
    return  os.path.join(voice_path,"%s.mp3"%filename)

def speak(ip):
   for i in ip:
       if i == ".":
           os.system("mpg123 %s > /dev/null 2>&1"%getFilePath("点"))
       else:
           os.system("mpg123 %s > /dev/null 2>&1"%getFilePath(i))
   os.system("mpg123 %s > /dev/null 2>&1"%getFilePath("完"))

count = 0
while True:
    ip = getLocalIP()
    print ip
    if ip.startswith("127"):
        os.system("mpg123 %s > /dev/null 2>&1"%getFilePath("正在获取网络地址"))
    else:
        count += 1
        speak(ip)
    if count == 10:
        break
    time.sleep(1)
