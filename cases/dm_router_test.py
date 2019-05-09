# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"type": "login", "def": "dm_auth_router_fail", "case_name": "路由器校验登录，uuid缺失", "code": -8003},
    {"type": "app", "def": "dm_check_router_fail", "case_name": "验证路由器有效性，uuid错误", "code": -8003},
    {"type": "app", "def": "fm_bind_router_fail", "case_name": "app调用绑定路由器，router_pwd错误", "code": -8003},
    {"type": "router", "def": "dm_bind_router_fail", "case_name": "router调用绑定路由器，bind_time错误", "code": -16038},
    {"type": "app", "def": "dm_get_user_account_fail", "case_name": "获取用户账户信息，list账户信息缺失", "code": -8003},
    {"type": "router", "def": "dm_get_router_info_fail", "case_name": "获取路由器信息，encry错误", "code": -14003},
    {"type": "app", "def": "mdp_msg_fail", "case_name": "MDP家庭路由转发，msg_type错误", "code": -14005},
    {"type": "login", "def": "dm_auth_router", "case_name": "路由器校验登录", "code": 0},
    {"type": "app", "def": "dm_check_router", "case_name": "验证路由器有效性", "code": 0},
    {"type": "app", "def": "fm_bind_router", "case_name": "app调用绑定路由器", "code": 0},
    {"type": "router", "def": "dm_bind_router", "case_name": "router调用绑定路由器", "code": 0},
    {"type": "router", "def": "dm_get_router_info", "case_name": "获取路由器信息", "code": 0},
    {"type": "app", "def": "dm_get_user_account", "case_name": "获取用户账户信息", "code": 0},
    {"type": "app", "def": "mdp_msg", "case_name": "MDP家庭路由转发", "code": 0},
]


def dm_get_user_account_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dm_get_user_account",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    # "list": [config.R_family_id]
                }
            }
    }


def dm_get_user_account(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dm_get_user_account",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "list": [config.user_id]
                }
            }
    }


def fm_bind_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_bind_router",
                "timestamp": timestamp,
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
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.user_id,
                    "bind_time": timestamp
                }
            }
    }


def dm_auth_router(family_id):
    timestamp = int(time.time())
    if family_id is None:
        router_uuid = config.router_uuid
        router_pwd = config.router_pwd
    else:
        router_uuid = config.R_router_uuid
        router_pwd = config.R_router_pwd
    return {
        "uuid": router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_auth_router",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "uuid": router_uuid,
                    "pwd": router_pwd,
                    "hardware_version": "v1.0",
                    "router_version": "v1.0",
                    "zigbee_version": "v1.0",
                    "bluetooth_version": "v1.0"
                }
            }
    }


def dm_get_router_info(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_router_info",
                "timestamp": timestamp,
                "req_id": 123
            }
    }


def dm_check_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dm_check_router",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "pwd": config.router_pwd,
                    "uuid": config.router_uuid
                }
            }
    }


def mdp_msg(family_id):
    timestamp = int(time.time())
    return{
                "uuid": config.R_router_uuid,
                "encry": "false",
                "content": {
                    "method": "mdp_msg",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "msg_type": "P2R",
                        "target_id": config.R_router_id,
                        "content": "hello my router!"
                    }
                }
            }


def fm_bind_router_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "fm_bind_router",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "router_uuid": config.router_uuid,
                    #"router_pwd": config.router_pwd,
                    "bind_time": timestamp
                }
            }
    }


def dm_bind_router_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_bind_router",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.user_id,
                    "bind_time": 1        #
                }
            }
    }


def dm_auth_router_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_auth_router",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    # "uuid": config.router_id,  #
                    "pwd": config.router_pwd,
                    "hardware_version": "v1.0",
                    "router_version": "v1.0",
                    "zigbee_version": "v1.0",
                    "bluetooth_version": "v1.0"
                }
            }
    }


def dm_get_router_info_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "True",  #
        "content":
            {
                "method": "dm_get_router_info",
                "timestamp": timestamp,
                "req_id": 123
            }
    }


def dm_check_router_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_check_router",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "pwd": config.router_pwd,
                    "uuid": config.router_id    #
                }
            }
    }


def mdp_msg_fail(family_id):
    timestamp = int(time.time())
    return {
                "uuid": config.router_uuid,
                "encry": "false",
                "content": {
                    "method": "mdp_msg",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "msg_type": "P2F",   #
                        "target_id": config.router_id,
                        "content": "hello my router!"
                    }
                }
            }
