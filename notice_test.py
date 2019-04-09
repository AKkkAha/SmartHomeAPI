#!/user/bin/env python
#coding=utf-8
'''
@project : $[PROJECT_NAME]
@author  : Lan Xin
#@file   : $[NAME].py
#@ide    : $[PRODUCT_NAME]
#@time   : $[YEAR]-$[MONTH]-$[DAY] $[HOUR]:$[MINUTE]:$[SECOND]
'''
import config

case_aggregate = [
    {"notice_upgrade_app": "通知app版本更新"},
    {"notice_upgrade_rounter": "通知rounter版本更新"}
]


# 通知app版本更新
def notice_upgrade_app(family_id):
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "push_msg",
                "timestamp": 1509087889,
                "req_id": 123,
                "msg_tag": "abcdebfasdfgdafs",
                "params": {
                    "method": "notice_upgrade_app",
                    "user_id": config.user_id,
                    "app_uuid": config.app_uuid
                }
            }
    }


# 通知rounter版本更新
def notice_upgrade_rounter(router_uuid):
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "push_msg",
                "timestamp": 1509087889,
                "req_id": 123,
                "msg_tag": "abcdebfasdfgdafs",
                "params": {
                    "method": "notice_upgrade_router",
                    "router_id": config.router_id,
                    "router_uuid": config.router_uuid
                }
            }
    }

