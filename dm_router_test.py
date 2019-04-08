# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"dm_bind_router": "绑定路由器"},
    {"dm_auth_router": "路由器校验登录"},
    {"dm_get_router_info": "获取路由器信息"},
    {"dm_check_router": "验证路由器有效性"}
]

def dm_bind_router(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_bind_router",
                "timestamp": 123456123,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": 123,
                    "bind_time": 1234567890
                }
            }
    }

def dm_auth_router(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_auth_router",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "uuid": config.router_uuid,
                    "pwd": config.router_pwd,
                    "hardware_version": "v1.0",
                    "router_version": "v1.0",
                    "zigbee_version": "v1.0",
                    "bluetooth_version": "v1.0"
                }
            }
    }

def dm_get_router_info(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_router_info",
                "timestamp": 1490229730,
                "req_id": 123
            }
    }

def dm_check_router(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_check_router",
                "timestamp": 12345667,
                "req_id": 123,
                "params": {
                    "pwd": "",
                    "uuid": ""
                }
            }
    }