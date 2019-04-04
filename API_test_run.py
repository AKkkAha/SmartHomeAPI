#!/usr/bin/python
# -*- coding:utf-8 -*-
from Socket_API import Socket_Cls
import Test_Case
import config
import Get_Code
import json
import time

def get_token(socket_ins):
    socket_ins.send_msg(Test_Case.um_get_phone_code())
    socket_ins.recv_msg()
    time.sleep(3)
    code = Get_Code.get_phone_code(config.phonenum)
    print code
    socket_ins.send_msg(Test_Case.um_login_code(str(code)))
    msg = socket_ins.recv_msg()
    socket_ins.close_conn()
    msg = json.loads(msg)
    token_msg = msg["content"]["result"]
    return token_msg



def test_run():
    socket_api = Socket_Cls()
    socket_api.conn()
    print get_token(socket_api)
    socket_api.close_conn()



if __name__ == "__main__":
    test_run()