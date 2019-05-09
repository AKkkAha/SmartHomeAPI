#!/user/bin/env python
#coding=utf-8
import config
import time

case_aggregate = [
    {"type": "app", "def": "mg_ack_msg", "case_name": "消息已读确认", "code": 0},
    {"type": "app", "def": "mg_add_msg", "case_name": "添加消息", "code": 0},
    {"type": "app", "def": "mg_del_msg", "case_name": "删除消息", "code": 0},
    {"type": "app", "def": "mg_get_msg_list", "case_name": "加载消息列表", "code": 0},
    {"type": "app", "def": "mg_get_msg_number", "case_name": "获取满足条件的消息总数", "code": 0},
    {"type": "app", "def": "mg_modify_msg", "case_name": "修改消息", "code": 0},
    {"type": "app", "def": "mg_add_msg_fail", "case_name": "添加消息，target_type错误", "code": -8003},
    {"type": "app", "def": "mg_get_msg_list_fail", "case_name": "加载消息列表，msg_status错误", "code": -8003},
    {"type": "app", "def": "mg_get_msg_number_fail", "case_name": "获取满足条件的消息总数，user_id缺失", "code": -8003},
    {"type": "app", "def": "mg_modify_msg_fail", "case_name": "修改消息，msg_id错误", "code": -8003},
]


def mg_modify_msg_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_modify_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "msg_id": "111",
                    "title": "title",
                    "content": "hello",
                    "from": "upgrade",
                }
            }
    }


def mg_get_msg_number_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_get_msg_number",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    # "user_id": 1234,
                    "family_id": 123,  # // 非必带参数，如果有，则用来过滤指定家庭的消息
                    "msg_state": 111,
                    "timestamp": 1516794910500122
                }
            }
    }


def mg_get_msg_list_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_get_msg_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": 1234,
                    "family_id": 123,  # // 非必带参数，对于设备消息可以用来过滤不同家庭
                    "msg_type": 2,
                    "msg_state": 1111,
                    "timestamp": 1516794910500122,
                    "page": {
                        "begin": 0,
                        "size": 10

                    }
                }
            }
    }


def mg_del_msg_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_del_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": config.user_id,
                    "mid_list": ["adb", 13]
                }
            }
    }


def mg_add_msg_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_add_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "msg_type": 2,
                    "is_need_push": 1,  # // 是否需要发送极光，1（需要），0（不需要），不带默认为1
                    "title": "title",
                    "content": "hello",
                    "from": "upgrade",
                    "target_type": -100,
                    "target_id": 0,
                    "target_ext": "ext"
                }
            }
    }


def mg_ack_msg_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_ack_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    # "user_id": config.R_family_id,
                    "mid_list": [12, 13, 14, 15, 16],  # // 指定确认消息的id，可不带
                    "timestamp": 1234567,  # // 指定确认消息的时间，可不带
                    "family_id": 111,  # // 与timestamp配合使用
                    "msg_type": 1  # // 与timestamp配合使用
                }
            }
    }


def mg_modify_msg(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_modify_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "msg_id": 111,
                    "title": "title",
                    "content": "hello",
                    "from": "upgrade",
                }
            }
    }


def mg_get_msg_number(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_get_msg_number",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": 1234,
                    "family_id": 123,  # // 非必带参数，如果有，则用来过滤指定家庭的消息
                    "msg_state": 111,
                    "timestamp": 1516794910500122
                }
            }
    }


def mg_get_msg_list(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_get_msg_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": 1234,
                    "family_id": 123,  # // 非必带参数，对于设备消息可以用来过滤不同家庭
                    "msg_type": 2,
                    "msg_state": 111,
                    "timestamp": 1516794910500122,
                    "page": {
                        "begin": 0,
                        "size": 10
                    }
                }
            }
    }


def mg_del_msg(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_del_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": config.user_id,
                    "mid_list": [12, 13]
                }
            }
    }


def mg_add_msg(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_add_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "msg_type": 2,
                    "is_need_push": 1,  # // 是否需要发送极光，1（需要），0（不需要），不带默认为1
                    "title": "title",
                    "content": "hello",
                    "from": "upgrade",
                    "target_type": 1,
                    "target_id": 0,
                    "target_ext": "ext"
                }
            }
    }


def mg_ack_msg(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "mg_ack_msg",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "user_id": config.user_id,
                    "mid_list": [12, 13, 14, 15, 16],  # // 指定确认消息的id，可不带
                    "timestamp": 1234567,  # // 指定确认消息的时间，可不带
                    "family_id": 111,  # // 与timestamp配合使用
                    "msg_type": 1  # // 与timestamp配合使用
                }
            }
    }