# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    # {"fm_unbind_router_fail": "app调用解绑定路由器_反例"},
    # {"dm_unbind_router_fail": "router调用解绑路由器_反例"},
    # {"fm_delete_family_fail": "删除家庭_反例"},
    {"fm_unbind_router": "app调用解绑定路由器"},
    {"dm_unbind_router": "router调用解绑路由器"},
    {"fm_delete_family": "删除家庭"}
]

def fm_unbind_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
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
        "uuid": config.phonenum,
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

def fm_unbind_router_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_unbind_router",
                "timestamp": 123456123,
                "req_id": 123,
                "params": {
                    "family_id": 1111,  #
                    "unbind_time": timestamp
                }
            }
    }

def dm_unbind_router_fail(family_id):
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
                    "unbind_time": 123           #
                }
            }
    }

def fm_delete_family_fail(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_delete_device",#
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": family_id
                }
            }
    }
