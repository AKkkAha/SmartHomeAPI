# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"type": "router", "def": "dm_add_room", "case_name": "添加房间", "code": 0},
    {"type": "router", "def": "dm_get_room_list", "case_name": "获取房间列表", "code": 0},
    {"type": "router", "def": "dm_add_shortcut", "case_name": "添加快捷方式", "code": 0},
    {"type": "router", "def": "dm_sort_shortcut", "case_name": "修改快捷方式位置", "code": 0},
    {"type": "router", "def": "dm_update_shortcut_new", "case_name": "全量更新快捷方式", "code": 0},
    {"type": "router", "def": "dm_update_shortcut", "case_name": "修改快捷方式", "code": 0},
    {"type": "app", "def": "dm_get_shortcut_list", "case_name": "获取快捷方式列表", "code": 0},
    {"type": "router", "def": "dm_update_shortcut_visible", "case_name": "更新快捷方式是否可见", "code": 0},
    {"type": "router", "def": "dm_update_room", "case_name": "修改房间信息", "code": 0},
    {"type": "router", "def": "dm_update_room_new", "case_name": "全量刷新房间", "code": 0},
    {"type": "router", "def": "dm_update_room_order", "case_name": "修改房间图标位置", "code": 0},
    {"type": "router", "def": "dm_add_shortcut_fail", "case_name": "添加快捷方式，shortcut_id已存在", "code": -15024},
    {"type": "router", "def": "dm_sort_shortcut_fail", "case_name": "修改快捷方式位置，list错误", "code": -8003},
    {"type": "router", "def": "dm_update_shortcut_new_fail", "case_name": "全量更新快捷方式，family_id错误", "code": -15004},
    {"type": "router", "def": "dm_update_shortcut_fail", "case_name": "修改快捷方式，room_id缺失", "code": -8003},
    {"type": "router", "def": "dm_update_shortcut_visible_fail", "case_name": "更新快捷方式是否可见，app_visible缺失", "code": -8003},
    {"type": "router", "def": "dm_del_shortcut_fail", "case_name": "删除快捷方式，shortcut过长", "code": -15013},
    {"type": "router", "def": "dm_update_room_fail", "case_name": "修改房间信息，room_name错误", "code": -8003},
    {"type": "router", "def": "dm_update_room_new_fail", "case_name": "全量刷新房间，user_id错误", "code": -16039},
    {"type": "router", "def": "dm_update_room_order_fail", "case_name": "修改房间图标位置，family_id错误", "code": -16027},
    {"type": "router", "def": "dm_add_room_fail", "case_name": "添加房间，无family_id", "code": -8003},
    {"type": "router", "def": "dm_get_room_list_fail", "case_name": "获取房间列表，user_id错误", "code": -15004},
    {"type": "app", "def": "dm_get_shortcut_list_fail", "case_name": "获取快捷方式列表，room_id错误", "code": -8003},
    {"type": "router", "def": "dm_del_room_fail", "case_name": "删除房间，list错误", "code": -8003},
    {"type": "router", "def": "dm_del_shortcut", "case_name": "删除快捷方式", "code": 0},
    {"type": "router", "def": "dm_del_room", "case_name": "删除房间", "code": 0},
]


def dm_update_room_order_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_room_order",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_router_id,
                        "user_id": config.user_id,
                        "list": [{
                            "room_id": 3,
                            "order": 1
                        },
                            {
                                "room_id": 2,
                                "order": 2
                            },
                            {
                                "room_id": 1,
                                "order": 3
                            }]
                    }
                }
    }


def dm_update_room_new_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_room_new",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [{
                            "user_id": config.router_id,
                            "room_id": 1,
                            "is_default": 0,
                            "room_name": "客厅",
                            "order": 1,
                            "create_at": 123456789,
                            "update_at": 123456789
                        },
                            {
                                "user_id": config.router_id,
                                "room_id": 2,
                                "is_default": 0,
                                "room_name": "卧室1",
                                "order": 2,
                                "create_at": 123456789,
                                "update_at": 123456789
                            }]
                    }
                }
    }


def dm_update_room_fail(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_room",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [{
                            "room_id": 1001,
                            "room_name": 12321
                        },
                            {
                                "room_id": 1002,
                                "room_name": "我的房间2"
                            }]
                    }
                }
    }


def dm_del_shortcut_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_del_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            999,
                            888,
                            777,
                            1,
                            2,
                            3,
                            4,
                            5,
                            6,
                            7,
                            8,
                            9,

                        ]
                    }
                }
    }


def dm_update_shortcut_visible_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_shortcut_visible",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "room_id": 3,
                        "user_id": config.user_id,
                        "list": [
                            {
                                "shortcut_id": 3,
                                # "app_visible": 66
                            },
                            {
                                "shortcut_id": 2,
                                "app_visible": 0
                            }
                        ]
                    }
                }
    }


def dm_update_shortcut_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                # "room_id": "",
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "app_visible": 0,
                                "content": [
                                    {
                                        "device_uuid": "test123123",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            },
                            {
                                "room_id": 2001,
                                "shortcut_id": 124,
                                "name": "shortcut 001",
                                "app_visible": 0,
                                "content": [
                                    {
                                        "device_uuid": "test123124",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }


def dm_update_shortcut_new_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_shortcut_new",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_router_id,
                        "list": [
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "device_category_id": -2,
                                "order": 3,
                                "app_visible": 1,
                                "content": [
                                    {
                                        "device_uuid": "test123123",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            },
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "device_category_id": -1,
                                "order": 3,
                                "app_visible": 1,
                                "content": [
                                    {
                                        "device_uuid": "test123124",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }


def dm_sort_shortcut_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_sort_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "room_id": 3,
                        "user_id": config.router_pwd,
                        "list": [
                            {
                                # "shortcut_id": 3,
                                "order": 1
                            },
                            {
                                "shortcut_id": 2,
                                "order": 2
                            },
                            {
                                "shortcut_id": 1,
                                "order": 3
                            }
                        ]
                    }
                }
    }


def dm_add_shortcut_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_add_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "device_category_id": -2,
                                "order": 3,
                                "content": [
                                    {
                                        "device_uuid": "11223344556677",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }


def dm_update_shortcut_visible(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_shortcut_visible",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "room_id": 3,
                        "user_id": config.user_id,
                        "list": [
                            {
                                "shortcut_id": 3,
                                "app_visible": 1
                            },
                            {
                                "shortcut_id": 2,
                                "app_visible": 0
                            }
                        ]
                    }
                }
    }


def dm_del_shortcut(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_del_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            123,
                            234,
                            456
                        ]
                    }
                }
    }


def dm_update_shortcut_new(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_shortcut_new",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "device_category_id": -2,
                                "order": 3,
                                "app_visible": 1,
                                "content": [
                                    {
                                        "device_uuid": "test123123",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            },
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "device_category_id": -1,
                                "order": 3,
                                "app_visible": 1,
                                "content": [
                                    {
                                        "device_uuid": "test123124",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }


def dm_sort_shortcut(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_sort_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "room_id": 3,
                        "user_id": config.user_id,
                        "list": [
                            {
                                "shortcut_id": 3,
                                "order": 1
                            },
                            {
                                "shortcut_id": 2,
                                "order": 2
                            },
                            {
                                "shortcut_id": 1,
                                "order": 3
                            }
                        ]
                    }
                }
    }


def dm_update_shortcut(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "app_visible": 0,
                                "content": [
                                    {
                                        "device_uuid": "test123123",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            },
                            {
                                "room_id": 2001,
                                "shortcut_id": 124,
                                "name": "shortcut 001",
                                "app_visible": 0,
                                "content": [
                                    {
                                        "device_uuid": "test123124",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }


def dm_add_shortcut(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_add_shortcut",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                "room_id": 2001,
                                "shortcut_id": 123,
                                "name": "shortcut 001",
                                "device_category_id": -2,
                                "order": 3,
                                "content": [
                                    {
                                        "device_uuid": "11223344556677",
                                        "mode": "off",
                                        "name": "空调",
                                        "control": "tmp"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }


def dm_update_room_order(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_room_order",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "user_id": config.user_id,
                        "list": [{
                            "room_id": 3,
                            "order": 1
                        },
                            {
                                "room_id": 2,
                                "order": 2
                            },
                            {
                                "room_id": 1,
                                "order": 3
                            }]
                    }
                }
    }


def dm_update_room_new(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_room_new",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [{
                            "user_id": config.user_id,
                            "room_id": 1,
                            "is_default": 0,
                            "room_name": "客厅",
                            "order": 1,
                            "create_at": 123456789,
                            "update_at": 123456789
                        },
                            {
                                "user_id": config.user_id,
                                "room_id": 2,
                                "is_default": 0,
                                "room_name": "卧室1",
                                "order": 2,
                                "create_at": 123456789,
                                "update_at": 123456789
                            }]
                    }
                }
    }


def dm_update_room(phonenum = config.phonenum):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_room",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [{
                            "room_id": 1001,
                            "room_name": "我的房间"
                        },
                            {
                                "room_id": 1002,
                                "room_name": "我的房间2"
                            }]
                    }
                }
    }


def dm_add_room(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_room",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [{
                        "user_id": config.user_id,
                        "room_id": 1,
                        "is_default": 0,
                        "room_name": "API1",
                        "order": 1,
                        "create_at": 123456789,
                        "update_at": 123456789
                    },
                        {
                            "user_id": config.user_id,
                            "room_id": 2,
                            "is_default": 0,
                            "room_name": "API2",
                            "order": 2,
                            "create_at": 123456789,
                            "update_at": 123456789
                        }]
                }
            }
    }


def dm_get_room_list(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_room_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "user_id": config.user_id
                }
            }
    }


def dm_get_shortcut_list(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dm_get_shortcut_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "room_id": 1001,
                    "family_id": config.R_family_id,
                    "page":
                        {
                            "size": 10,
                            "begin": 0
                    }
                }
        }
    }


def dm_del_room(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_room",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [1,
                             2]
                }
            }
    }


def dm_add_room_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_room",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    #"family_id": family_id,
                    "list": [{
                        "user_id": config.user_id,
                        "room_id": 1,
                        "is_default": 0,
                        "room_name": "API1",
                        "order": 1,
                        "create_at": 123456789,
                        "update_at": 123456789
                    },
                        {
                            "user_id": config.user_id,
                            "room_id": 2,
                            "is_default": 0,
                            "room_name": "API2",
                            "order": 2,
                            "create_at": 123456789,
                            "update_at": 123456789
                        }]
                }
            }
    }


def dm_get_room_list_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_room_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.router_id #
                }
            }
    }


def dm_get_shortcut_list_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_shortcut_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "room_id": '1',#
                    "family_id": family_id,
                    "page":
                        {
                            "size": 10,
                            "begin": 0
                    }
                }
        }
    }


def dm_del_room_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_room",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": family_id,
                    # "list": [1,
                    #          2]
                }
            }
    }
