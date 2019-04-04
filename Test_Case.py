# -*- coding:utf-8 -*-
import config
phonenum = config.phonenum

case_aggr = {
    "um_auth":"APP自动登录",
    "fm_create_family":"创建家庭"
}

def um_get_phone_code(phonenum = config.phonenum):
    return {
        "uuid": "000c229d200000000000D0B60A0001C8",
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
        "uuid": "000c229d200000000000D0B60A0001C8",
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
