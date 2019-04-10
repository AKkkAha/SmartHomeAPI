# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"dm_add_room": "添加房间"},
    {"dm_get_room_list": "获取房间列表"},
    {"dm_get_shortcut_list": "获取快捷方式列表"},
    {"dm_del_room": "删除房间"},
    # {"dm_add_room_fail": "添加房间_反例"},
    # {"dm_get_room_list_fail": "获取房间列表_反例"},
    # {"dm_get_shortcut_list_fail": "获取快捷方式列表_反例"},
    # {"dm_del_room_fail": "删除房间_反例"}
]

def dm_add_room(family_id):
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_room",
                "timestamp": 1490229730,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_room_list",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "user_id": config.user_id
                }
            }
    }

def dm_get_shortcut_list(family_id):
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dm_get_shortcut_list",
                "timestamp": 1490229730,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_room",
                "req_id": 123,
                "timestamp": 12312312312,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [1,
                             2]
                }
            }
    }

def dm_add_room_fail(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_room",
                "timestamp": 1490229730,
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
    return {
        #"uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_room_list",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "user_id": config.user_id
                }
            }
    }

def dm_get_shortcut_list_fail(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_shortcut_list",
                "timestamp": 1490229730,
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
                    # "list": [1,
                    #          2]
                }
            }
    }
