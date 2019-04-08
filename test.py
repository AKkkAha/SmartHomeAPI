#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import json
import time
from API_test_run import *
uuid = '000c229d200000000000D0B60A0001C8'
socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_test.connect(("119.23.168.152", 30086))
token = test_run()
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
send_msg = {
        "uuid": "000c229d200000000000D0B60A0001C8",
        "encry": "false",
        "content":
            {
                "method": "fm_create_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_name": "API测试的家"
                }
            }
    }
send_msg = json.dumps(send_msg)
print send_msg
socket_test.send(send_msg+'\n')
recv_msg = socket_test.recv(1024)
print recv_msg
socket_test.close()
