#!/usr/bin/python
# -*- coding:utf-8 -*-
from API_test_run import *
from Socket_API import Socket_Cls

socket_token = Socket_Cls()
# log = logger.rstcls.initial()
timestamp = int(time.time())
socket_token.conn()
send_msg = {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_register_user",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                            "pwd": config.member_password,
                            "secret": config.member_pwd,
                            "phone": "18223332333",
                            "os_type": "Android",
                            "app_version": "v0.5",
                            "os_version": "android4.3",
                            "hardware_version": "Huawei"
                }
        }
    }


print "++++++++++++++++++++\n"
socket_token.send_msg(send_msg)
recv_msg = socket_token.recv_msg()
print "--------------------\n" + recv_msg
time.sleep(2)
# socket_test.send(json.dumps(end_test.fm_unbind_router(22877))+'\n')
# socket_test.recv(1024)
# socket_test.send(json.dumps(end_test.dm_unbind_router(config.R_family_id))+'\n')
# print socket_test.recv(1024)
socket_token.close_conn()
