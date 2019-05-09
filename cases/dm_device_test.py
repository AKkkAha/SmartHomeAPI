# -*- coding:utf-8 -*-
import config
import time

case_aggregate = [
    {"type": "router", "def": "dm_add_device", "case_name": "添加设备", "code": 0},
    {"type": "router", "def": "dr_new_device_join_notice", "case_name": "陌生设备第一次接入", "code": 0},
    {"type": "router", "def": "dm_update_device", "case_name": "刷新设备", "code": 0},
    {"type": "router", "def": "dm_get_device_info", "case_name": "获取设备信息", "code": 0},
    {"type": "router", "def": "dm_get_devices_by_family", "case_name": "按照家庭获取设备列表", "code": 0},
    {"type": "router", "def": "dm_get_devices_by_room", "case_name": "按照房间获取设备列表", "code": 0},
    {"type": "router", "def": "dm_get_family_dev_type_list", "case_name": "获取家庭设备品类列表", "code": 0},
    {"type": "router", "def": "dr_get_dev_status_list", "case_name": "获取设备状态列表", "code": 0},
    {"type": "router", "def": "dm_update_device_new", "case_name": "全量刷新设备", "code": 0},
    {"type": "router", "def": "dr_report_dev_status", "case_name": "上报设备状态", "code": 0},
    {"type": "router", "def": "dr_delete_dev_status", "case_name": "删除设备状态", "code": 0},
    {"type": "router", "def": "da_get_dev_alert_list", "case_name": "获取设备告警列表", "code": 0},
    {"type": "router", "def": "da_report_dev_alert", "case_name": "上报设备告警", "code": 0},
    {"type": "router", "def": "da_delete_dev_alert", "case_name": "删除设备告警", "code": 0},
    {"type": "router", "def": "dm_del_device", "case_name": "删除设备", "code": 0},
    {"type": "app", "def": "dr_subscibe_push", "case_name": "订阅消息推送", "code": 0},
    {"type": "app", "def": "dr_unsubscibe_push", "case_name": "去订阅消息推送", "code": 0},
    {"type": "router", "def": "dm_add_device_fail", "case_name": "添加设备，device_uuid错误", "code": -8003},
    {"type": "router", "def": "dr_new_device_join_notice_fail", "case_name": "陌生设备第一次接入，device_name缺失", "code": -8003},
    {"type": "router", "def": "dm_update_device_fail", "case_name": "刷新设备，device_uuid错误", "code": -8003},
    {"type": "router", "def": "dm_get_device_info_fail", "case_name": "获取设备信息，device_id错误", "code": -15009},
    {"type": "router", "def": "dm_get_devices_by_family_fail", "case_name": "按照家庭获取设备列表，family_id错误", "code": -8003},
    {"type": "router", "def": "dm_update_device_new_fail", "case_name": "全量刷新设备，bussiness_user_id错误", "code": -8003},
    {"type": "router", "def": "dr_report_dev_status_fail", "case_name": "上报设备状态，family_id缺失", "code": -8003},
    {"type": "router", "def": "dr_delete_dev_status_fail", "case_name": "删除设备状态，device_category_id缺失", "code": -8003},
    {"type": "router", "def": "da_get_dev_alert_list_fail", "case_name": "获取设备告警列表，status错误", "code": -8003},
    {"type": "router", "def": "da_report_dev_alert_fail", "case_name": "上报设备告警，title错误", "code": -8003},
    {"type": "router", "def": "da_delete_dev_alert_fail", "case_name": "删除设备告警，del_time缺失", "code": -8003},
    {"type": "router", "def": "dm_get_devices_by_room_fail", "case_name": "按照房间获取设备列表，device_category_id错误", "code": -8003},
    {"type": "router", "def": "dm_get_family_dev_type_list_fail", "case_name": "获取家庭设备品类列表，family_id错误", "code": -15004},
    {"type": "router", "def": "dr_get_dev_status_list_fail", "case_name": "获取设备状态列表，device_id错误", "code": -8003},
    {"type": "router", "def": "dm_del_device_fail", "case_name": "删除设备，method错误", "code": -8003},
    {"type": "app", "def": "dr_subscibe_push_fail", "case_name": "订阅消息推送，app_uuid缺失", "code": -8003},
    {"type": "app", "def": "dr_unsubscibe_push_fail", "case_name": "去订阅消息推送，family_id错误", "code": -8003},
]


def dr_unsubscibe_push_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.phonenum,
            "encry": "false",
            "content":
                {
                    "method": "dr_unsubscibe_push",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.router_uuid,
                        "app_uuid": config.app_uuid
                    }
                }
    }


def dr_subscibe_push_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.phonenum,
            "encry": "false",
            "content":
                {
                    "method": "dr_subscibe_push",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": family_id,
                        # "app_uuid": config.app_uuid
                    }
                }
    }


def da_delete_dev_alert_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "da_delete_dev_alert",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.user_id,
                        "device_uuid": "test123123",
                        # "del_time": 123456798
                    }
                }
    }


def da_report_dev_alert_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "da_report_dev_alert",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": 2013,
                        "list": [
                            {
                                "device_id": 11,
                                "device_uuid": "test123123",
                                "device_category_id": 11,
                                "product_id": "sfdal",
                                "manufacturer": "hair",
                                "code": "e6",
                                "level": 1,
                                "status": 1,
                                "push_rights": 0,
                                "push_type": 0x01,
                                "updated_at": 123456789,
                                "tip_type": 1,
                                "title": 123,
                                "text": "xxx发生故障",
                                "attribute": {
                                        }
                            },
                            {
                                "device_id": 123124,
                                "device_uuid": "test123124",
                                "device_category_id": 11,
                                "product_id": "sfdal",
                                "manufacturer": "hair",
                                "code": "e6",
                                "level": 1,
                                "status": 1,
                                "push_rights": 0,
                                "push_type": 0x01,
                                "updated_at": 123456789,
                                "tip_type": 1,
                                "title": "fire warning",
                                "text": "xxx发生故障",
                                "attribute": {
                                    "msg": "door is broken!"
                                    }
                            }]
                        }
                }
    }


def da_get_dev_alert_list_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "da_get_dev_alert_list",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                                "family_id": config.R_family_id,
                                "product_id": "",
                                "date_start": "20180419",
                                "date_end": "20190420",
                                "level": 1,
                                "code": "e7",
                                "status": [9, 2, 3],
                                "page": {
                                    "size": 1,
                                    "begin": 0
                                }
                }
        }
    }


def dr_delete_dev_status_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dr_delete_dev_status",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.user_id,
                        "device_id": 123123,
                        "device_uuid": "test123123",
                        # "device_category_id": 11,
                        "del_time": 123456798
                    }
                }
    }


def dr_report_dev_status_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dr_report_dev_status",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        # "family_id": 1,
                        "list": [{
                                "device_id": 123123,
                                "device_uuid": "test12312",
                                "device_category_id": -33,
                                "type": "switch",
                                "status_modified_at": 12312312312,
                                "attribute": {
                                                 "switch": "on"
                                             },
                                 "updated_at": 123456789
                                },
                                {
                                "device_id": 123124,
                                "device_uuid": "test12314",
                                "device_category_id": 0,
                                "type": "switch",
                                "status_modified_at": 12312312312,
                                "attribute": {
                                                 "switch": "on"
                                             },
                                "updated_at": 123456789
                                }]
                            }
                }
    }


def dm_update_device_new_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_device_new",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "list": [{
                                "device_id": 123123,
                                "device_uuid": "test123123",
                                "bussiness_user_id": config.user_id,
                                "device_category_id": 11,
                                "device_name": "lamp_01",
                                "attribute": {
                                    "test": 11
                            }
                        }]
                    }
                }
    }


def dr_new_device_join_notice_fail(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dr_new_device_join_notice",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "user_id": config.user_id,
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                "mac": "",
                                "ip": "",
                                #"device_name": "name",
                                "brand_name": "name",
                                "type": "new",
                                "updated_at": 123456789,
                                "attribute": {
                                    "connect_type": "2.4G"
                                }
                            }
                        ]
                    }
                }
    }


def dr_new_device_join_notice(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dr_new_device_join_notice",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "user_id": config.user_id,
                        "family_id": config.R_family_id,
                        "list": [
                            {
                                "mac": "",
                                "ip": "",
                                "device_name": "name",
                                "brand_name": "name",
                                "type": "new",
                                "updated_at": 123456789,
                                "attribute": {
                                    "connect_type": "2.4G"
                                }

                            }
                        ]
                    }
                }
    }


def dm_update_device_new(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dm_update_device_new",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
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
                            "user_id": config.user_id,
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
                                "user_id": config.user_id,
                                "create_at": 123456789,
                                "update_at": 123456789
                            }]
                    }
                }
    }


def dr_unsubscibe_push(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.phonenum,
            "encry": "false",
            "content":
                {
                    "method": "dr_unsubscibe_push",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": family_id,
                        "app_uuid": config.app_uuid
                    }
                }
    }


def dr_subscibe_push(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.phonenum,
            "encry": "false",
            "content":
                {
                    "method": "dr_subscibe_push",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": family_id,
                        "app_uuid": config.app_uuid
                    }
                }
    }


def da_delete_dev_alert(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "da_delete_dev_alert",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "device_uuid": "test123123",
                        "del_time": 123456798
                    }
                }
    }


def dr_delete_dev_status(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dr_delete_dev_status",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": config.R_family_id,
                        "device_id": 123123,
                        "device_uuid": "test123123",
                        "device_category_id": 11,
                        "del_time": 123456798
                    }
                }
    }


def dr_report_dev_status(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.R_router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "dr_report_dev_status",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                    "family_id": 1,
                    "list": [{
                                "device_id": 123123,
                                "device_uuid": "test123123",
                                "device_category_id": 11,
                                "type": "switch",
                                "status_modified_at": 12312312312,
                                "attribute": {
                                                 "switch": "on"
                                             },
                                 "updated_at": 123456789
                                },
                                {
                                "device_id": 123124,
                                "device_uuid": "test123124",
                                "device_category_id": 11,
                                "type": "switch",
                                "status_modified_at": 12312312312,
                                "attribute": {
                                                 "switch": "on"
                                             },
                                "updated_at": 123456789
                                }]
                            }
                }
    }


def da_report_dev_alert(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "da_report_dev_alert",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "family_id": 2013,
                        "list": [
                            {
                                "device_id": 123123,
                                "device_uuid": "test123123",
                                "device_category_id": 11,
                                "product_id": "sfdal",
                                "manufacturer": "hair",
                                "code": "e6",
                                "level": 1,
                                "status":1,
                                "push_rights": 0,
                                "push_type": 0x01,
                                "updated_at": 123456789,
                                "tip_type": 1,
                                "title":"fire warning",
                                "text": "xxx发生故障",
                                "attribute": {
                                    "msg": "door is broken!"
                                        }
                            },
                            {
                                "device_id": 123124,
                                "device_uuid": "test123124",
                                "device_category_id": 11,
                                "product_id": "sfdal",
                                "manufacturer": "hair",
                                "code": "e6",
                                "level": 1,
                                "status":1,
                                "push_rights": 0,
                                "push_type": 0x01,
                                "updated_at": 123456789,
                                "tip_type": 1,
                                "title":"fire warning",
                                "text": "xxx发生故障",
                                "attribute": {
                                    "msg": "door is broken!"
                                    }
                            }]
                        }
                }
    }


def da_get_dev_alert_list(family_id):
    timestamp = int(time.time())
    return {
            "uuid": config.router_uuid,
            "encry": "false",
            "content":
                {
                    "method": "da_get_dev_alert_list",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                                  "family_id": config.R_family_id,
                                  "product_id": "",
                                "date_start": "20180419",
                                "date_end": "20190420",
                                "level": 1,
                                "code": "e7",
                                "status": [1, 2, 3],
                                "page": {
                                    "size": 1,
                                    "begin": 0
                                }
                }
        }
    }


def dm_add_device(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_device",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
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
                        "user_id": config.user_id,
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
                            "user_id": config.user_id,
                            "create_at": 123456789,
                            "update_at": 123456789
                        }]
                }
            }
    }


def dm_update_device(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_update_device",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [{
                        "device_id": 123123,
                        "device_uuid": "test123123",
                        "room_id": 1,
                        "bussiness_user_id": 123,
                        "device_name": "lamp_01",
                        "device_category_id": 11,
                        "attribute": {
                            "switch": "on"
                        },
                        "user_id": config.user_id,
                        "create_at": 123456789,
                        "update_at": 123456789
                    },
                        {
                            "device_id": 123124,
                            "device_uuid": "test123124",
                            "room_id": 1,
                            "bussiness_user_id": 124,
                            "device_name": "lamp_02",
                            "device_category_id": 11,
                            "attribute": {
                                "switch": "on"
                            },
                            "user_id": config.user_id,
                            "create_at": 123456789,
                            "update_at": 123456789
                        }]
                }
            }
    }


def dm_get_device_info(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_device_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "router_id": config.R_router_id,
                    "device_id": 123123,
                    "device_uuid": "test123123",
                    "user_id": config.user_id
                }
            }
    }


def dm_get_devices_by_family(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_family",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_id": config.R_router_id,
                    "family_id": config.R_family_id,
                    "device_category_id": 11,
                    "user_id": config.user_id,
                    "page": {
                        "size": 10,
                        "begin": 0
                    }
                }
            }
    }


def dm_get_devices_by_room(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_room",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_id": config.R_router_id,
                    "family_id": config.R_family_id,
                    "room_id": 1,
                    "device_category_id": 11,
                    "user_id": config.user_id,
                    "page": {
                        "size": 10,
                        "begin": 0
                    }
                }
            }
    }


def dm_get_family_dev_type_list(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_family_dev_type_list",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.R_family_id
                }
            }
    }


def dr_get_dev_status_list(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dr_get_dev_status_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                              "family_id": config.R_family_id,
                              "device_id": 123123,
                              "date": "20170101",
                              "device_uuid": "112233445566778810",
                              "type": "key",
                              "page":
                                  {
                                    "size": 10,
                                    "begin": 0
                                }
                        }
        }
    }


def dm_del_device(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_device",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [123123,
                             123124]
                }
            }
    }


def dm_add_device_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_device",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [{
                        "device_id": 123123,
                        #"device_uuid": "test123123",
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
                            #"device_category_id": 11,
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


def dm_update_device_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_update_device",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [{
                        "device_id": 123123,
                        #"device_uuid": "test123123",
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
                            #"bussiness_user_id": "test123123",
                            "device_name": "lamp_02",
                            "device_category_id": 11,
                            "attribute": {
                                "switch": "on"
                            }
                        }]
                }
            }
    }


def dm_get_device_info_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_device_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "family_id": family_id,
                    "router_id": config.router_id,
                    "device_id": 123123,
                    #"device_uuid": "test123123",
                    "user_id": config.user_id
                }
            }
    }


def dm_get_devices_by_family_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_family",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_id": config.router_id,
                    #"family_id": family_id,
                    "device_category_id": 11,
                    "user_id": config.user_id,
                    "page": {
                        "size": 10,
                        "begin": 0
                    }
                }
            }
    }


def dm_get_devices_by_room_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_room",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_id": config.router_id,
                    "family_id": family_id,
                    "room_id": 1,
                    #"device_category_id": 11,
                    "user_id": config.user_id,
                    "page": {
                        "size": 10,
                        "begin": 0
                    }
                }
            }
    }


def dm_get_family_dev_type_list_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_family_dev_type_list",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": 1111
                }
            }
    }


def dr_get_dev_status_list_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dr_get_dev_status_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                              "family_id": family_id,
                              #"device_id": 1231231111,#
                              "date": "20170101",
                              #"device_uuid": "112233445566",#
                              "type": "key",
                              "page":
                                  {
                                    "size": 10,
                                    "begin": 0
                                }
                        }
        }
    }


def dm_del_device_fail(family_id):
    timestamp = int(time.time())
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_devi",#
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "family_id": family_id,
                    "list": [123123,
                             123124]
                }
            }
    }
