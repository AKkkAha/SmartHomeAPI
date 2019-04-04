#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import json

class Socket_Cls(object):
    def __init__(self):
        self.host = '119.23.168.152'
        self.port = 30086
        self.tcplink = None


    def conn(self):
        try:
            #print "prepare to connect to %s" % self.host
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            self.tcplink = sock
            #print "connect success"
            return sock
        except Exception as e:
            return e


    def send_msg(self, msg):
        msg = json.dumps(msg)+'\n'
        self.tcplink.send(msg)

    def recv_msg(self):
        msg = self.tcplink.recv(1024)
        return msg

    def check_msg(self, req_id, msg):
        if msg["req_id"] == req_id:
            return True
        else:
            return False

    def close_conn(self):
        self.tcplink.close()

