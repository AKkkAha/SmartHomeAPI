#!/user/bin/env python
#coding=utf-8
import config
import time

case_aggregate = [
    {"type": "app", "def": "acc_logout", "case_name": "客户端退出登陆", "code": 0},
    {"type": "app", "def": "acc_check_client_online", "case_name": "判断客户端是否在线", "code": 0},
    {"type": "app", "def": "acc_check_client_online_fail", "case_name": "判断客户端是否在线，client_id错误", "code": -1},
]


def acc_check_client_online_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "acc_check_client_online",
                "req_id": 123,
                "timestamp": timestamp,
                "params":
                    {
                        "client_id": config.R_family_id
                    }
            }
    }


def acc_logout(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "acc_logout",
                "timestamp": timestamp,
                "req_id": 123
            }
    }


def acc_check_client_online(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "acc_check_client_online",
                "req_id": 123,
                "timestamp": timestamp,
                "params":
                    {
                        "client_id": config.user_id
                    }
            }
    }


def acc_get_system_time(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "acc_get_system_time",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                }
            }
    }
