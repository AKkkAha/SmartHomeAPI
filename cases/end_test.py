# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"type": "app", "def": "fm_unbind_router_fail", "case_name": "app调用解绑定路由器，family_id错误", "code": -16027},
    {"type": "router", "def": "dm_unbind_router_fail", "case_name": "router调用解绑路由器，timestamp错误", "code": -16038},
    {"type": "app", "def": "fm_remove_member_fail", "case_name": "删除家庭成员，户主删除自己", "code": -16000},
    {"type": "app", "def": "fm_delete_family_fail", "case_name": "删除家庭，method错误", "code": -8003},
    {"type": "app", "def": "fm_unbind_router", "case_name": "app调用解绑定路由器", "code": 0},
    {"type": "router", "def": "dm_unbind_router", "case_name": "router调用解绑路由器", "code": 0},
    {"type": "app", "def": "fm_remove_member", "case_name": "删除家庭成员", "code": 0},
    {"type": "app", "def": "fm_delete_family", "case_name": "删除家庭", "code": 0}
]


def fm_remove_member_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_remove_member",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "target_user_id": config.user_id,
                    "family_id": config.R_family_id
                }
            }
    }


def fm_remove_member(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_remove_member",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "target_user_id": config.member_id,
                    "family_id": config.R_family_id
                }
            }
    }


def fm_unbind_router(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_unbind_router",
                "timestamp": timestamp,
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
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.user_id,
                    "unbind_time": timestamp
                }
            }
    }


def fm_delete_family(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_delete_family",
                "req_id": 123,
                "timestamp": timestamp,
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
                "timestamp": timestamp,
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
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.user_id,
                    "unbind_time": 123           #
                }
            }
    }


def fm_delete_family_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_delete_device",#
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": family_id
                }
            }
    }
