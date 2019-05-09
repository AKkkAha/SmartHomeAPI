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
        self.msg_to_send = None

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
            self.log.log("connection exception: " + str(e))
            time.sleep(3)
            self.conn()


    def send_msg(self, msg):
        self.msg_to_send = json.dumps(msg) + '\n'
        print "------send------: " + self.msg_to_send
        try:
            self.tcplink.send(self.msg_to_send)
            self.log.log("----------send msg----------: "+self.msg_to_send)
        except Exception as e:
            self.log.log("send exception: " + str(e))
            print "send exception: " + str(e)
            time.sleep(3)
            self.conn()
            self.send_msg(json.loads(self.msg_to_send))

    def wash_msg(self, msg):
        try:
            msg = json.loads(msg)
            flag_msg = json.loads(self.msg_to_send)
            if msg["uuid"] == flag_msg["uuid"]:
                return True
            else:
                return False
        except:
            return False

    def recv_msg(self):
        msg = ""
        try:
            msg = self.tcplink.recv(2048)
            print "------recv------: " + msg
            self.log.log("----------recv msg----------: "+msg)
            for each_msg in msg.split("\n"):
                if self.wash_msg(each_msg):
                    print "washed msg: " + each_msg
                    return each_msg
            print "no target msg, receive again !!"
            return each_msg + self.recv_msg()
        except Exception as e:
            print "recv exception: " + str(e)
            self.log.log("recv exception: " + str(e))
            return msg

    def check_msg(self, req_id, msg):
        if msg["req_id"] == req_id:
            return True
        else:
            return False

    def close_conn(self):
        self.tcplink.close()
        self.log.log("disconnected to %s:%s" % (self.host, self.port))
