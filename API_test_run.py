#!/usr/bin/python
# -*- coding:utf-8 -*-
from Socket_API import Socket_Cls
import config
import Get_Code
import json
import time
import logger
import cases.um_test as um_test
import cases.fm_test as fm_test
import cases.dm_router_test as dm_router_test
import cases.member_test as member_test
import cases.end_test as end_test
import cases.dm_room_test as dm_room_test
import sys
import os
sys.path.append(os.path.join(os.path.dirname((os.path.abspath(__file__))), "cases"))


# 获取登陆token
def get_token(socket_ins, log):
    socket_ins.conn()
    socket_ins.send_msg(um_test.um_get_phone_code(arg=0))
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["msg"] == "success":
        log.log("用例    PASS    获取手机登陆验证码")
        print "用例    PASS    获取手机登陆验证码\n"
    else:
        log.log("用例    FAIL    获取手机登陆验证码  code: %s msg: %s" % (str(msg["content"]["code"]), str(msg["content"]["msg"])))
        print "用例    FAIL    获取手机登陆验证码  code: %s msg: %s\n" % (str(msg["content"]["code"]), str(msg["content"]["msg"]))
        # print msg
    code = Get_Code.get_phone_code(config.phonenum)
    # code = "790797"
    print "login code: " + code
    socket_ins.send_msg(um_test.um_login_code(code))
    msg = json.loads(socket_ins.recv_msg().split("\n")[0])
    socket_ins.close_conn()
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例    PASS    APP验证码登陆")
        print "用例    PASS    APP验证码登陆\n"
    else:
        log.log("用例    FAIL    APP验证码登陆  code: %s msg: %s" % (str(msg["content"]["code"]), str(msg["content"]["msg"])))
        print "用例    FAIL    APP验证码登陆  code: %s msg: %s\n" % (str(msg["content"]["code"]), str(msg["content"]["msg"]))
        # print msg
    try:
        token_msg = msg["content"]["result"]
    except:
        return False
    return token_msg


# 注册app账号
def regist_user(socket_ins, log):
    socket_ins.conn()
    socket_ins.send_msg(um_test.um_register_user())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例    PASS    获取手机注册验证码")
        print "用例 PASS    获取手机注册验证码\n"
    else:
        log.log("用例    PASS    获取手机注册验证码  code: %s msg: %s" % (str(msg["content"]["code"]), str(msg["content"]["msg"])))
        print "用例    PASS    获取手机注册验证码  code: %s msg: %s\n" % (str(msg["content"]["code"]), str(msg["content"]["msg"]))
        # print msg
        return
    # print socket_ins.recv_msg()
    code = Get_Code.get_phone_code(config.phonenum)
    print "regist code: " + code
    socket_ins.send_msg(um_test.um_check_phone_code(code))
    msg = json.loads(socket_ins.recv_msg())
    socket_ins.close_conn()
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例    PASS    校验手机验证码")
        print "用例    PASS    校验手机验证码\n"
    else:
        log.log("用例    FAIL    校验手机验证码  code: %s msg: %s" % (str(msg["content"]["code"]), str(msg["content"]["msg"])))
        print "用例    FAIL    校验手机验证码  code: %s msg: %s\n" % (str(msg["content"]["code"]), str(msg["content"]["msg"]))
        # print msg


# 获取调用接口生成的家庭的family_id
def get_fmid(socket_ins, log, token):
    socket_ins.conn()
    socket_ins.send_msg(um_test.um_auth(token))
    msg = json.loads(socket_ins.recv_msg())
    # if msg["content"]["req_id"] != 123 or msg["content"]["code"] != 0:
    #     print "authory login failed"
    #     socket_ins.send_msg(um_test.um_auth(token))
    #     socket_ins.recv_msg()
    socket_ins.send_msg(fm_test.fm_create_family())
    msg = json.loads(socket_ins.recv_msg())
    if msg["content"]["req_id"] == 123 and msg["content"]["code"] == 0:
        log.log("用例    PASS    创建家庭")
        print "用例    PASS    创建家庭\n"
    else:
        log.log("用例    FAIL    创建家庭  code: %s msg: %s" % (str(msg["content"]["code"]), str(msg["content"]["msg"])))
        print "用例    FAIL    创建家庭  code: %s msg: %s\n" % (str(msg["content"]["code"]), str(msg["content"]["msg"]))
        # print msg
        return
    family_id = msg["content"]["result"]["family_id"]
    return family_id


def test_run():
    log = logger.rstcls.initial()
    logl = logger.logcls.initial()
    socket_api = Socket_Cls()
    # regist_user(socket_api, log)
    # time.sleep(10)
    # token = get_token(socket_api, log)
    token = config.token
    family_id = None
    for aggr_name in config.Test_Case:
        aggr = __import__(aggr_name)
        if aggr_name == "um_test":
            if token is None:
                token = get_token(socket_api, log)
            arg = token
        elif family_id is None:
            family_id = get_fmid(socket_api, log, token)
            arg = family_id
        test_case = aggr.case_aggregate
        for operation in test_case:
            API_type = operation["type"]
            # time.sleep(2)
            operate = operation["def"]
            case_name = operation["case_name"]
            socket_api.conn()
            if API_type == "router":
                if operate in ["dm_auth_router", "dm_unbind_router", "dm_bind_router", "dm_unbind_router_fail"]:
                    socket_api.send_msg(dm_router_test.dm_auth_router(None))  # 登陆虚拟路由器
                else:
                    socket_api.send_msg(dm_router_test.dm_auth_router(arg))  # 登陆真实路由器
                socket_api.recv_msg()
            elif API_type == "member":  # 登陆家庭成员app账户
                socket_api.send_msg(member_test.um_login_pwd(arg))
                socket_api.recv_msg()
            elif API_type == "login":  # 接口属于登陆类型时不做预先登陆
                pass
            elif API_type == "app":   # 登陆户主app账户
                socket_api.send_msg(um_test.um_auth(token))
                socket_api.recv_msg()
            msg_to_send = getattr(aggr, operate)(arg)
            socket_api.send_msg(msg_to_send)
            msg = socket_api.recv_msg()
            socket_api.close_conn()
            if msg == "":
                log.log("用例    FAIL    %s  time out" % (str(case_name)))
                logl.log("用例    FAIL    %s  time out" % (str(case_name)))
                print "用例    FAIL    %s  time out\n" % (str(case_name))
            else:
                try:
                    msg = json.loads(msg)
                    if msg["uuid"] == msg_to_send["uuid"] and msg["content"]["code"] in operation["code"]:
                        log.log("用例    PASS    %s" % str(case_name))
                        logl.log("用例    PASS    %s" % str(case_name))
                        print "用例    PASS    %s\n" % str(case_name)
                    else:
                        log.log("用例    FAIL    %s  code: %s msg: %s" % (str(case_name), str(msg["content"]["code"]), str(msg["content"]["msg"])))
                        logl.log("用例    FAIL    %s  code: %s msg: %s" % (str(case_name), str(msg["content"]["code"]), str(msg["content"]["msg"])))
                        print "用例    FAIL    %s  code: %s msg: %s\n" % (str(case_name), str(msg["content"]["code"]), str(msg["content"]["msg"]))
                except Exception as e:
                    log.log("用例    PASS    %s    %s" % (str(case_name), e))
                    logl.log("用例    PASS    %s    %s" % (str(case_name), e))
                    print "用例    PASS    %s    %s\n" % (str(case_name), e)
    # return token


if __name__ == "__main__":
    # test_run()
    i = 0
    while i < 50:
        log = logger.rstcls.initial()
        i += 1
        log.log("\r\n----------第%s轮测试----------\n" % i)
        test_run()
        time.sleep(10)
