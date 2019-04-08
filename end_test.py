# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"fm_unbind_router": "解绑定路由器"},
    {"fm_delete_family": "删除家庭"}
]

def dm_unbind_router(family_id):
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
                    "user_id": 123,
                    "unbind_time": 1234567890
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
