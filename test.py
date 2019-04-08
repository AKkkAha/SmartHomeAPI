#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import json
import time
import config
from API_test_run import *
uuid = '000c229d200000000000D0B60A0001C8'
socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_test.connect(("119.23.168.152", 30086))
token = config.token
send_msg = {
        "uuid": "000c229d200000000000D0B60A0001C8",
        "encry": "false",
        "content":
            {
                "method": "um_auth",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "user_id": token['user_id'],
                    "token": token["token"],
                    "os_type": "Android"
                }
            }
    }
send_msg = json.dumps(send_msg)
print send_msg
socket_test.send(send_msg+'\n')
recv_msg = socket_test.recv(1024)
print recv_msg
family_id = 22624
for i in range(2):
    family_id += 3
    send_msg = {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "fm_get_family_list",
                "req_id": 123,
                "timestamp": 12312312
            }
    }
    send_msg = json.dumps(send_msg)
    print send_msg
    socket_test.send(send_msg+'\n')
    recv_msg = socket_test.recv(1024)
    print recv_msg
    time.sleep(1)
socket_test.close()
