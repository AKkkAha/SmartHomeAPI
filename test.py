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

# socket_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_t.connect(("119.23.168.152", 30086))
socket_test.send(json.dumps(um_test.um_auth(token))+'\n')
print socket_test.recv(1024)
# socket_t.send(json.dumps(fm_test.fm_get_apply_code(config.R_family_id)) + '\n')
# rst = socket_t.recv(1024)
# socket_t.close()
# code = json.loads(rst)["content"]["result"]["code"]
# print code
# socket_test.send(json.dumps(member_test.um_login_pwd(123))+'\n')
# socket_test.recv(1024)
# socket_test.send(json.dumps(dm_router_test.fm_bind_router(22877))+'\n')
# socket_test.recv(1024)
# socket_test.send(json.dumps(dm_router_test.dm_auth_router(None))+'\n')
# socket_test.recv(1024)
# socket_test.send(json.dumps(dm_router_test.dm_bind_router(config.R_family_id))+'\n')
# socket_test.recv(1024)
# socket_test.send(json.dumps(dm_router_test.dm_auth_router(None))+'\n')
# socket_test.recv(1024)
timestamp = int(time.time())
send_msg = {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_register_user",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                            "pwd": "111111",
                            "secret": config.member_pwd,
                            "phone": "18122223333",
                            "os_type": "Android",
                            "app_version": "v0.5",
                            "os_version": "android4.3",
                            "hardware_version": "Huawei"
                }
            }
    }

send_msg = json.dumps(send_msg)
print "++++++++++++++++++++\n" + send_msg
socket_test.send(send_msg+'\n')
recv_msg = socket_test.recv(1024)
print "--------------------\n" + recv_msg
time.sleep(2)
# socket_test.send(json.dumps(end_test.fm_unbind_router(22877))+'\n')
# socket_test.recv(1024)
# socket_test.send(json.dumps(end_test.dm_unbind_router(config.R_family_id))+'\n')
# print socket_test.recv(1024)
socket_test.close()
