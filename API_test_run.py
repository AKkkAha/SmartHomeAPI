#!/usr/bin/python
# -*- coding:utf-8 -*-
from Socket_API import Socket_Cls
import config
import um_test
import fm_test
import Get_Code
import json
import time
import logger

#获取登陆token
def get_token(socket_ins, log):
    socket_ins.conn()
    socket_ins.send_msg(um_test.um_get_phone_code())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
        log.log("用例 获取手机登陆验证码 成功")
        print "用例 获取手机登陆验证码 成功"
    else:
        log.log("用例 获取手机登陆验证码 失败")
        print "用例 获取手机登陆验证码 失败"
        #print msg
    code = Get_Code.get_phone_code(config.phonenum)
    print "login code: " + code
    socket_ins.send_msg(um_test.um_login_code(code))
    msg = json.loads(socket_ins.recv_msg())
    socket_ins.close_conn()
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例 APP验证码登陆 成功")
        print "用例 APP验证码登陆 成功"
    else:
        log.log("用例 APP验证码登陆 失败")
        print "用例 APP验证码登陆 失败"
        #print msg
    try:
        token_msg = msg["content"]["result"]
    except:
        return False
    return token_msg

#注册app账号
def regist_user(socket_ins, log):
    socket_ins.conn()
    socket_ins.send_msg(um_test.um_register_user())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例 获取手机注册验证码 成功")
        print "用例 获取手机注册验证码 成功"
    else:
        log.log("用例 获取手机注册验证码 失败")
        print "用例 获取手机注册验证码 失败"
        #print msg
        return
    #print socket_ins.recv_msg()
    code = Get_Code.get_phone_code(config.phonenum)
    print "regist code: " + code
    socket_ins.send_msg(um_test.um_check_phone_code(code))
    msg = json.loads(socket_ins.recv_msg())
    socket_ins.close_conn()
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例 校验手机验证码 成功")
        print "用例 校验手机验证码 成功"
    else:
        log.log("用例 校验手机验证码       失败")
        print "用例 校验手机验证码 失败"
        #print msg

def get_fmid(socket_ins, log):
    socket_ins.conn()
    socket_ins.send_msg(fm_test.fm_create_family())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例 创建家庭 成功")
        print "用例 创建家庭 成功"
    else:
        log.log("用例 创建家庭 失败")
        print "用例 创建家庭 失败"
        #print msg
        return
    family_id = msg["content"]["result"]["family_id"]
    return family_id

def test_run():
    log = logger.rstcls.initial()
    socket_api = Socket_Cls()
    # regist_user(socket_api, log)
    # time.sleep(10)
    for aggr_name in config.Test_Case:
        aggr = __import__(aggr_name)
        if aggr_name == "um_test":
            token = get_token(socket_api, log)
            if not token:
                token = get_token(socket_api, log)
            arg = token
        elif aggr_name == "fm_test":
            family_id = get_fmid(socket_api, log)
            arg = family_id
        test_case = aggr.case_aggregate
        for operation in test_case:
            print operation
            operate, case_name = operation.items()[0]
            time.sleep(2)
            socket_api.conn()
            msg = getattr(aggr, operate)(arg)
            socket_api.send_msg(msg)
            msg = json.loads(socket_api.recv_msg())
            if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
                log.log("用例 $s 成功" % case_name)
                print "用例 $s 成功" % case_name
            else:
                log.log("用例 %s           失败" % case_name)
                print "用例 %s 失败" % case_name
                print msg
    #socket_api.close_conn()
    #return token






if __name__ == "__main__":
    test_run()
