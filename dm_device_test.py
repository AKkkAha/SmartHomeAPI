# -*- coding:utf-8 -*-
import config

case_aggregate = [
    {"dm_add_device": "添加设备"},
    {"dm_update_device": "刷新设备"},
    {"dm_get_device_info": "获取设备信息"},
    {"dm_get_devices_by_family": "按照家庭获取设备列表"},
    {"dm_get_devices_by_room": "按照房间获取设备列表"},
    {"dm_get_family_dev_type_list": "获取家庭设备品类列表"},
    {"dr_get_dev_status_list": "获取设备状态列表"},
    {"dm_del_device": "删除设备"},
    # {"dm_add_device_fail": "添加设备_反例"},
    # {"dm_update_device_fail": "刷新设备_反例"},
    # {"dm_get_device_info_fail": "获取设备信息_反例"},
    # {"dm_get_devices_by_family_fail": "按照家庭获取设备列表_反例"},
    # {"dm_get_devices_by_room_fail": "按照房间获取设备列表_反例"},
    # {"dm_get_family_dev_type_list_fail": "获取家庭设备品类列表_反例"},
    # {"dr_get_dev_status_list_fail": "获取设备状态列表_反例"},
    # {"dm_del_device_fail": "删除设备_反例"}
]

def dm_add_device(family_id):
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_device",
                "timestamp": 1490229730,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_update_device",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                    "family_id": config.R_family_id,
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
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_device_info",
                "timestamp": 1490229730,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_family",
                "req_id": 123,
                "timestamp": 123121211,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_room",
                "req_id": 123,
                "timestamp": 123121211,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_family_dev_type_list",
                "req_id": 123,
                "timestamp": 123121211,
                "params": {
                    "family_id": config.R_family_id
                }
            }
    }

def dr_get_dev_status_list(family_id):
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dr_get_dev_status_list",
                "timestamp": 1490229730,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_device",
                "req_id": 123,
                "timestamp": 123456789,
                "params": {
                    "family_id": config.R_family_id,
                    "list": [123123,
                             123124]
                }
            }
    }

def dm_add_device_fail(family_id):
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_add_device",
                "timestamp": 1490229730,
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
    return {
        "uuid": config.R_router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_update_device",
                "timestamp": 1490229730,
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
                    "router_id": config.router_id,
                    "device_id": 123123,
                    #"device_uuid": "test123123",
                    "user_id": config.user_id
                }
            }
    }

def dm_get_devices_by_family_fail(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_family",
                "req_id": 123,
                "timestamp": 123121211,
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
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_devices_by_room",
                "req_id": 123,
                "timestamp": 123121211,
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
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_get_family_dev_type_list",
                "req_id": 123,
                "timestamp": 123121211,
                "params": {
                    "family_id": 1111
                }
            }
    }

def dr_get_dev_status_list_fail(family_id):
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dr_get_dev_status_list",
                "timestamp": 1490229730,
                "req_id": 123,
                "params": {
                              "family_id": family_id,
                              "device_id": 1231231111,#
                              "date": "20170101",
                              "device_uuid": "112233445566",#
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
    return {
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dm_del_devi",#
                "req_id": 123,
                "timestamp": 123456789,
                "params": {
                    "family_id": family_id,
                    "list": [123123,
                             123124]
                }
            }
    }
