#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import json
import logger
import time

class Socket_Cls(object):
    def __init__(self):
        self.host = '119.23.168.152'
        self.port = 30086
        self.tcplink = None
        self.log = logger.logcls.initial()



    def conn(self):
        try:
            #print "prepare to connect to %s" % self.host
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.host, self.port))
            self.log.log("connected to %s:%s" % (self.host, self.port))
            self.tcplink = sock
            #print "connect success"
            return sock
        except Exception as e:
            self.log.log("connection exception: " + e)
            time.sleep(3)
            self.conn()


    def send_msg(self, msg):
        msg = json.dumps(msg) + '\n'
        print "------send------: " + msg
        try:
            self.tcplink.send(msg)
            self.log.log("----------send msg----------: "+msg)
        except Exception as e:
            self.log.log("send exception: " + e)
            time.sleep(3)
            self.conn()
            self.send_msg(msg)

    def recv_msg(self):
        try:
            msg = self.tcplink.recv(2048)
            print "------recv------: " + msg
            self.log.log("----------recv msg----------: "+msg)
            return msg.split("\n")[0]
        except Exception as e:
            self.log.log("recv exception: " + e)

    def check_msg(self, req_id, msg):
        if msg["req_id"] == req_id:
            return True
        else:
            return False

    def close_conn(self):
        self.tcplink.close()
        self.log.log("disconnected to %s:%s" % (self.host, self.port))

