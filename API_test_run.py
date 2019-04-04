#!/usr/bin/python
# -*- coding:utf-8 -*-
from Socket_API import Socket_Cls
import Test_Case
import config
import Get_Code
import json
import time

def get_token(socket_ins):
    socket_ins.conn()
    socket_ins.send_msg(Test_Case.um_get_phone_code())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
        print "用例 获取手机登陆验证码 成功"
    else:
        print "用例 获取手机登陆验证码 失败"
        print msg
    code = Get_Code.get_phone_code(config.phonenum)
    print "login code: " + code
    socket_ins.send_msg(Test_Case.um_login_code(code))
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
        print "用例 APP验证码登陆 成功"
    else:
        print "用例 APP验证码登陆 失败"
        print msg
    socket_ins.close_conn()
    socket_ins.close_conn()
    try:
        token_msg = msg["content"]["result"]
    except:
        return False
    return token_msg

def regist_user(socket_ins):
    socket_ins.conn()
    socket_ins.send_msg(Test_Case.um_register_user())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
        print "用例 获取手机注册验证码 成功"
    else:
        print "用例 获取手机注册验证码 失败"
        print msg
    #print socket_ins.recv_msg()
    code = Get_Code.get_phone_code(config.phonenum)
    print "regist code: " + code
    socket_ins.send_msg(Test_Case.um_check_phone_code(code))
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
        print "用例 校验手机验证码 成功"
    else:
        print "用例 校验手机验证码 失败"
        print msg
    socket_ins.close_conn()



def test_run():
    socket_api = Socket_Cls()
    regist_user(socket_api)
    time.sleep(20)
    token = get_token(socket_api)
    # print token
    for operation in Test_Case.case_aggregate:
        for operate, case_name in operation.items()[0]:
            socket_api.conn()
            msg = getattr(Test_Case, operate)(token)
            socket_api.send_msg(msg)
            msg = json.loads(socket_api.recv_msg())
            if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
                print "用例 $s 成功" % case_name
            else:
                print "用例 %s 失败" % case_name
                print msg






if __name__ == "__main__":
    test_run()
