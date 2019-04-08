# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"dm_add_room": "添加房间"},
    {"dm_get_room_list": "获取房间列表"},
    {"dm_get_shortcut_list": "获取快捷方式列表"},
    {"dm_del_room": "删除房间"}
]

def dm_add_room(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_room",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "list": [{
                        "user_id": 1001,
                        "room_id": 1,
                        "is_default": 0,
                        "room_name": "API1",
                        "order": 1,
                        "create_at": 123456789,
                        "update_at": 123456789
                    },
                        {
                            "user_id": 1001,
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
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_room_list",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": 123
                }
            }
    }

def dm_get_shortcut_list(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_shortcut_list",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "room_id": 1001,
                    "family_id": family_id,
                    "page":
                        {
                            "size": 10,
                            "begin": 0
                    }
                }
        }
    }

def dm_del_room(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_room",
                "req_id": 123,
                "timestamp": 12312312312,
                "params": {
                    "family_id": family_id,
                    "list": [1,
                             2]
                }
            }
    }