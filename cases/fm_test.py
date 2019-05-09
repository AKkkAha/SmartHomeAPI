# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"type": "app", "def": "fm_update_family", "case_name": "更新家庭基本信息", "code": 0},
    {"type": "app", "def": "fm_get_member_list", "case_name": "获取成员信息列表", "code": 0},
    {"type": "app", "def": "fm_get_apply_code", "case_name": "获取用户申请码", "code": 0},
    {"type": "app", "def": "fm_get_family_list", "case_name": "获取用户加入的家庭列表", "code": 0},
    {"type": "app", "def": "fm_update_member_rights", "case_name": "修改家庭成员的权限", "code": 0},
    {"type": "app", "def": "fm_transfer_owner", "case_name": "转让户主", "code": 0},
    {"type": "app", "def": "fm_get_family_info", "case_name": "获取家庭基本信息", "code": 0},
    {"type": "app", "def": "fm_get_backgroud_list", "case_name": "获取家庭背景图片列表", "code": 0},
    {"type": "app", "def": "fm_create_family_fail", "case_name": "创建家庭，家庭名称非法", "code": -8003},
    {"type": "app", "def": "fm_update_family_fail", "case_name": "更新家庭基本信息，family_id错误", "code": -16027},
    {"type": "app", "def": "fm_get_member_list_fail", "case_name": "获取成员信息列表，family_id错误", "code": -8003},
    {"type": "app", "def": "fm_create_member_fail", "case_name": "创建家庭成员，family_id错误", "code": -8003},
    {"type": "app", "def": "fm_get_apply_code_fail", "case_name": "获取用户申请码，family_id错误", "code": -16027},
    {"type": "app", "def": "fm_get_family_list_fail", "case_name": "获取用户加入的家庭列表，timestamp错误", "code": -8003},
]


def fm_update_member_rights(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_update_member_rights",
                "timestamp": timestamp,
                "req_id": 123,
                "msg_tag": "xxx",
                "params": {
                    "family_id": config.R_family_id,
                    "list": [{
                        "user_id": config.user_id,
                        "rights": {
                            "visual_intercom": "open",  # // 可视对讲，open有权限，close无权限，默认有权限
                            "visual_doorbell": "open"  # // 可视门铃，open有权限，close无权限，默认有权限
                        }
                    }]
                }
            }
    }


def fm_get_backgroud_list(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_backgroud_list",
                "req_id": 123,
                "timestamp": timestamp
            }
    }


def fm_get_family_info(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_family_info",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.R_family_id
                }
            }
    }


def fm_transfer_owner(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_transfer_owner",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "new_owner_id": config.user_id,
                    "family_id": config.R_family_id
                }
            }
    }


def fm_create_family(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_family",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_name": "API测试的家"
                }
            }
    }


def fm_update_family(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_update_family",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": family_id,
                    "family_name": "API更新的家",
                    "family_avatar": "",
                    "family_background": "http://111"
                }
            }
    }


def fm_get_member_list(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_member_list",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": family_id
                }
            }
    }


def fm_get_apply_code(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_apply_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id
                }
            }
    }


def fm_get_family_list(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_family_list",
                "req_id": 123,
                "timestamp": timestamp
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


def fm_create_family_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_family",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_name": '"API测试1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890的家"' #
                }
            }
    }


def fm_update_family_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_update_family",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.router_id,    #
                    "family_name": "API更新的家",
                    "family_avatar": "",
                    "family_background": "http://111"
                }
            }
    }


def fm_get_member_list_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_member_list",    #
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.phonenum
                }
            }
    }


def fm_create_member_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_member",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.router_uuid,
                    "code": config.R_router_pwd
                }
            }
    }


def fm_get_apply_code_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_apply_code",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.user_id
                }
            }
    }


def fm_get_family_list_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_family_list",
                "req_id": 123,
                #"timestamp": timestamp
            }
    }

