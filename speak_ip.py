#!/usr/bin/env python
# coding=utf-8

import os
import time
import socket
import subprocess

voice_path = os.path.join(os.path.abspath(os.curdir),'voice')
player = "omxplayer"


def getLocalIP():
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 0))
        ip =  s.getsockname()[0]
    except:
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
    if ip.startswith("127."):
        cmd = '''/sbin/ifconfig | grep "inet " | cut -d: -f2 | awk '{print $1}' | grep -v "^127."'''
        a = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        a.wait()
        out = a.communicate()
        ip = out[0].strip().split("\n") # 所有的列表
        ip = "完".join(ip)
    return ip


def getFilePath(filename):
    return os.path.join(voice_path, "%s.mp3" % filename)


def play(voice):
    os.system("%s %s > /dev/null 2>&1" % (player, getFilePath(voice)))


def speak(ip):
    for i in ip:
        if i == ".":
            play("点")
        else:
            play(i)
    play("完")

if __name__=='__main__':
    count = 0
    while True:
        ip = getLocalIP()
        print ip
        if ip.startswith("127"):
            play("正在获取网络地址")
        else:
            count += 1
            speak(ip)
        if count == 10:
            break
        time.sleep(1)
