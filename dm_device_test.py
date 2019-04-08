# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"dm_add_device": "添加设备"},
    {"dm_update_device": "刷新设备"},
    {"dm_get_device_info": "获取设备信息"},
    {"dm_get_devices_by_family": "按照家庭获取设备列表"},

]

def dm_add_device(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_device",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "list": [{
                        "device_id": 123123,
                        "device_uuid": "test123123",
                        "bussiness_user_id": 123,
                        "device_category_id": 11,
                        "device_name": "lamp_01",
                        "attribute": {
                            "test": 11
                        },
                        "room_id": 1,
                        "user_id": 12312,
                        "create_at": 123456789,
                        "update_at": 123456789
                    },
                        {
                            "device_id": 123124,
                            "device_uuid": "test123124",
                            "bussiness_user_id": 124,
                            "device_category_id": 11,
                            "device_name": "lamp_02",
                            "attribute": {
                                "test": 11
                            },
                            "room_id": 1,
                            "user_id": 12312,
                            "create_at": 123456789,
                            "update_at": 123456789
                        }]
                }
            }
    }

def dm_update_device(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_update_device",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "list": [{
                        "device_id": 123123,
                        "device_uuid": "test123123",
                        "room_id": 1,
                        "bussiness_user_id": "test123123",
                        "device_name": "lamp_01",
                        "device_category_id": 11,
                        "attribute": {
                            "switch": "on"
                        }
                    },
                        {
                            "device_id": 123124,
                            "device_uuid": "test123124",
                            "room_id": 1,
                            "bussiness_user_id": "test123123",
                            "device_name": "lamp_02",
                            "device_category_id": 11,
                            "attribute": {
                                "switch": "on"
                            }
                        }]
                }
            }
    }

def dm_get_device_info(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_device_info",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "router_id": 11,
                    "device_id": 123123,
                    "device_uuid": "test123123",
                    "user_id": 123
                }
            }
    }

def dm_get_devices_by_family(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_family",
                "req_id": 123,
                "timestamp": 123121211,
                "params": {
                    "router_id": 1001,
                    "family_id": family_id,
                    "device_category_id": 11,
                    "user_id": 123,
                    "page": {
                        "size": 10,
                        "begin": 0
                    }
                }
            }
    }