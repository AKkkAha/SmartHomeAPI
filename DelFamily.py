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

family_id = 23026
for i in range(5):
    # # 解绑家庭与路由器（如果家庭绑定了路由器无法删除）
    # timestamp = int(time.time())
    # send_msg = {
    #         "uuid": config.phonenum,
    #         "encry": "false",
    #         "content":
    #             {
    #                 "method": "fm_unbind_router",
    #                 "timestamp": 123456123,
    #                 "req_id": 123,
    #                 "params": {
    #                     "family_id": family_id,
    #                     "unbind_time": timestamp
    #                 }
    #             }
    #     }
    # send_msg = json.dumps(send_msg)
    # print send_msg
    # socket_test.send(send_msg+'\n')
    # recv_msg = socket_test.recv(1024)
    # print recv_msg
    # 删除家庭
    send_msg = {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "fm_delete_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": family_id
                }
            }
    }
    send_msg = json.dumps(send_msg)
    print send_msg
    socket_test.send(send_msg+'\n')
    recv_msg = socket_test.recv(1024)
    print recv_msg
    time.sleep(1)
    family_id += 1

#查询家庭列表
send_msg = {
        "uuid": config.phonenum,
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
recv_msg = socket_test.recv(2048)
print recv_msg
# recv_msg = socket_test.recv(1024)
# print recv_msg
socket_test.close()
