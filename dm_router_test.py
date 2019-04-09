# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"fm_bind_router": "app调用绑定路由器"},
    {"dm_bind_router": "router调用绑定路由器"},
    {"mdp_msg": "MDP家庭路由转发"},
    {"dm_auth_router": "路由器校验登录"},
    {"dm_get_router_info": "获取路由器信息"},
    {"dm_check_router": "验证路由器有效性"}
]

def fm_bind_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "fm_bind_router",
                "timestamp": 123456123,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "router_uuid": config.router_uuid,
                    "router_pwd": config.router_pwd,
                    "bind_time": timestamp
                }
            }
    }

def dm_bind_router(family_id):
    timestamp = int(time.time())
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
                    "user_id": config.user_id,
                    "bind_time": timestamp
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
                    "pwd": config.router_pwd,
                    "uuid": config.router_uuid
                }
            }
    }

def mdp_msg(family_id):
    return  {
                "uuid": config.router_uuid,
                "encry": "false",
                "content": {
                    "method": "mdp_msg",
                    "timestamp": 123456789,
                    "req_id": 123,
                    "params": {
                        "msg_type": "P2R",
                        "target_id": config.router_id,
                        "content": "hello my router!"
                    }
                }
            }

