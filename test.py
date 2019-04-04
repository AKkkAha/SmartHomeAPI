#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import json
import time
uuid = '000c229d200000000000D0B60A0001C8'
socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_test.connect(("119.23.168.152", 30086))
send_msg = {
        "uuid": "000c229d200000000000D0B60A0001C8",
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": "18200183087",
                    "type": 2
                }
            }
    }
send_msg = json.dumps(send_msg)
print send_msg
socket_test.send(send_msg+'\n')
time.sleep(10)
send_msg = {
        "uuid": "000c229d200000000000D0B60A0001C8",
        "encry": "false",
        "content":
            {
                "method": "um_login_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": "18200183087",
                    "code": "123456",
                    "os_type": "Android",
                    "app_version":"v0.5",
                    "os_version":"android4.3",
                    "hardware_version":"Huawei",
                    "phone_name":"xxxxxxxx",
                    "sso":1
                }
        }
    }
send_msg = json.dumps(send_msg)
print send_msg
socket_test.send(send_msg+'\n')
recv_msg = socket_test.recv(1024)
print recv_msg
socket_test.close()
