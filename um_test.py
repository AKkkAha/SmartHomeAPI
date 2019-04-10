# -*- coding:utf-8 -*-
import config
phonenum = config.phonenum

case_aggregate = [
    {"um_auth": "APP自动登录"},
    # {"um_get_phone_code": "获取手机登陆验证码_反例"},
    # {"um_login_code": "app验证码登陆_反例"},
    # {"um_register_user": "获取手机注册验证码_反例"},
    # {"um_check_phone_code": "校验手机验证码_反例"}
    # {"um_kickoff_client": "踢出其他终端用户"},
    # {"fm_update_family": "更新家庭基本信息"},
    # {"fm_create_family": "创建家庭"}
]

def um_get_phone_code(phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 2
                }
            }
    }

def um_login_code(code, phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_login_code",
                "timestamp": 12345667,
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

def um_register_user(phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 1
                }
            }
    }

def um_check_phone_code(code, phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_check_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 1,
                    "code": code
                }
        }
    }

def um_auth(token):
    return{
        "uuid": phonenum,
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

def um_kickoff_client(token):
    return

def um_get_phone_code_fail(phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": "adbadfga", #
                    "type": 2
                }
            }
    }

def um_login_code_fail(code, phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_login_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
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
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_get_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 9                #
                }
            }
    }

def um_check_phone_code_fail(code, phonenum = config.phonenum):
    return {
        "uuid": phonenum,
        "encry": "false",
        "content":
            {
                "method": "um_check_phone_code",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "phone": phonenum,
                    "type": 1,
                    "code": "adfaef"           #
                }
        }
    }
