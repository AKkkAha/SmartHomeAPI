# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"fm_unbind_router": "app调用解绑定路由器"},
    {"dm_unbind_router": "router调用解绑路由器"},
    {"fm_delete_family": "删除家庭"}
]

def fm_unbind_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "fm_unbind_router",
                "timestamp": 123456123,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "unbind_time": timestamp
                }
            }
    }

def dm_unbind_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_unbind_router",
                "timestamp": 123456123,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.user_id,
                    "unbind_time": timestamp
                }
            }
    }

def fm_delete_family(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "fm_delete_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": family_id
                }
            }
    }
