# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"fm_update_family": "更新家庭基本信息"},
    {"fm_get_member_list": "获取成员信息列表"},
    {"fm_create_member": "创建家庭成员"},
    {"fm_get_apply_code": "获取用户申请码"},
    {"fm_get_family_list": "获取用户加入的家庭列表"},
    # {"fm_create_family_fail": "创建家庭_反例"}
    # {"fm_update_family_fail": "更新家庭基本信息_反例"},
    # {"fm_get_member_list_fail": "获取成员信息列表_反例"},
    # {"fm_create_member_fail": "创建家庭成员_反例"},
    # {"fm_get_apply_code_fail": "获取用户申请码_反例"},
    # {"fm_get_family_list_fail": "获取用户加入的家庭列表_反例"},
    #{"fm_delete_family": "删除家庭"}
]

def fm_create_family():
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_name": "API测试的家"
                }
            }
    }

def fm_update_family(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_update_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": family_id,
                    "family_name": "API更新的家",
                    "family_avatar": "",
                    "family_background": "http://111"
                }
            }
    }

def fm_get_member_list(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_member_list",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": family_id
                }
            }
    }

def fm_create_member(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_member",
                "req_id": 123,
                "timestamp": 12312312,
                "params": {
                    "family_id": family_id,
                    "code": "123456"
                }
            }
    }

def fm_get_apply_code(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_apply_code",
                "timestamp": 123456123,
                "req_id": 123,
                "params": {
                    "family_id": family_id
                }
            }
    }

def fm_get_family_list(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_family_list",
                "req_id": 123,
                "timestamp": 12312312
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

def fm_create_family_fail():
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_name": "API'测试'的家"    #
                }
            }
    }

def fm_update_family_fail(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_update_family",
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": config.router_id,    #
                    "family_name": "API更新的家",
                    "family_avatar": "",
                    "family_background": "http://111"
                }
            }
    }

def fm_get_member_list_fail(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_member_",    #
                "req_id": 123,
                "timestamp": 123456890,
                "params": {
                    "family_id": family_id
                }
            }
    }

def fm_create_member_fail(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_create_member",
                "req_id": 123,
                "timestamp": 12312312,
                "params": {
                    "family_id": family_id,
                    "code": "123456"
                }
            }
    }

def fm_get_apply_code_fail(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_apply_code",
                "timestamp": 123456123,
                #"req_id": 123,
                "params": {
                    "family_id": family_id
                }
            }
    }

def fm_get_family_list_fail(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "fm_get_family_list",
                "req_id": 123,
                #"timestamp": 12312312
            }
    }

