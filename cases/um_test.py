# -*- coding:utf-8 -*-
import config
import time
phonenum = config.phonenum

case_aggregate = [
    {"type": "app", "def": "um_get_phone_code_fail", "case_name": "获取手机登陆验证码，phone错误", "code": -8003},
    {"type": "login", "def": "um_login_code_fail", "case_name": "app验证码登陆，phone缺失", "code": -8003},
    {"type": "app", "def": "um_register_user_fail", "case_name": "获取手机注册验证码，type错误", "code": -8003},
    {"type": "app", "def": "um_check_phone_code_fail", "case_name": "校验手机验证码，手机号已注册", "code": -17006},
    {"type": "app", "def": "um_can_login_token", "case_name": "APP是否可用token登录", "code": 0},
    {"type": "login", "def": "um_auth", "case_name": "APP自动登录", "code": 0},
    {"type": "app", "def": "um_get_other_login_clients", "case_name": "获取其他登录的终端列表", "code": 0},
    {"type": "app", "def": "um_check_exist", "case_name": "检查用户是否存在", "code": 0},
    {"type": "app", "def": "um_sip_call_auth", "case_name": "sip呼叫权限校验", "code": 0},
    {"type": "app", "def": "um_get_user_account", "case_name": "获取用户帐号信息", "code": 0},
    {"type": "app", "def": "um_update_user_profile", "case_name": "用户更新资料", "code": 0},
    {"type": "app", "def": "um_get_user_profile", "case_name": "获取指定用户的信息", "code": 0},
]


def um_can_login_token(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_can_login_token",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "user_id": config.user_id,
                        "uuid": "2005",
                        "os_type": "Android_Phone",
                        "sso": 1
                    }
                }
    }


def um_update_user_profile(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_update_user_profile",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "name": "啊哈" + str(timestamp),
                    "nick": "啊哈" + str(timestamp),
                    "gender": 1,
                    "avatar": "http://iotv03.app/image/7",
                    "birthday": "1986-12-12",
                    "app_version": "2.1.0"
                }
            }
    }


def um_get_user_profile(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_user_profile",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": config.user_id
                }
            }
    }


def um_get_user_account(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_user_account",
                "timestamp": timestamp,
                "req_id": 123
            }
    }


def um_sip_call_auth(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_sip_call_auth",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "srcAVURL": "sip:P2P_2003@10.101.70.109",
                    "dstAVURL": "sip:P2P_2003@10.101.70.109",
                    "token": config.token["token"]
                }
            }
    }


def um_check_exist(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_check_exist",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": config.phonenum
                }
            }
    }


def um_get_other_login_clients(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_other_login_clients",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                }
            }
    }


def um_get_phone_code(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": config.phonenum,
                    "type": 2
                }
            }
    }


def um_login_code(code, phonenum=config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_login_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "code": code,
                    "os_type": "Android",
                    "app_version":"v0.5",
                    "os_version":"android4.3",
                    "hardware_version":"Huawei",
                    "phone_name":"xxxxxxxx",
                    "sso":1
                }
        }
    }


def um_register_user(phonenum=config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 1
                }
            }
    }


def um_check_phone_code(code, phonenum=config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_check_phone_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 1,
                    "code": code
                }
        }
    }


def um_auth(token):
    timestamp = int(time.time())
    return{
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_auth",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": token['user_id'],
                    "token": token["token"],
                    "os_type": "Android"
                }
            }
    }


def um_kickoff_client(token):
    return


def um_get_phone_code_fail(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": "adbadfga", #
                    "type": 2
                }
            }
    }


def um_login_code_fail(code):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_login_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    # "phone": config.user_id,#
                    "code": "1232123",         #
                    "os_type": "Android",
                    "app_version":"v0.5",
                    "os_version":"android4.3",
                    "hardware_version":"Huawei",
                    "phone_name":"xxxxxxxx",
                    "sso":1
                }
        }
    }


def um_register_user_fail(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": config.phonenum,
                    "type": 9                #
                }
            }
    }


def um_check_phone_code_fail(code):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_check_phone_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "phone": config.phonenum,
                    "type": 1,
                    "code": "adfaef"           #
                }
            }
    }
