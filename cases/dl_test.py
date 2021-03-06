#!/user/bin/env python
#coding=utf-8
import config
import time

case_aggregate = [
    {"type": "app", "def": "dl_upgrade_app", "case_name": "APP检查升级", "code": 0},
    {"type": "app", "def": "dl_upgrade_h5", "case_name": "H5资源包检查升级", "code": 0},
    {"type": "router", "def": "dl_upgrade_router", "case_name": "路由器检查升级", "code": 0},
    {"type": "app", "def": "dl_upgrade_version_switch", "case_name": "ios审核版本开关", "code": 0},
    {"type": "app", "def": "dl_upgrade_version_switch_fail", "case_name": "ios审核版本开关，版本缺失", "code": 0},
    {"type": "router", "def": "dl_upgrade_router_fail", "case_name": "路由器检查升级，router_id错误", "code": 0},
]


# 获取oss_sts -- 开发说已经删除
# def dl_oss_sts(sts_type):
#     return{
#         "uuid": config.router_uuid,
#         "encry": "false",
#         "content":
#             {
#                 "method": "dl_oss_sts",
#                 "timestamp": 12345667,
#                 "req_id": 123,
#                 "params": {
#                     "type": sts_type  # 传入此参数则为开放平台的sts，不传或者为空则为智能家居平台的Sts
#                 }
#             }
#     }


def dl_upgrade_router_fail(family_id):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_router",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_version": "0.0.1",
                    "android_system_version": "0.0.1",
                    "router_id": config.R_router_pwd,
                    "router_uuid": "a",
                    "list": [
                        {
                            "device_uuid": "abc",
                            "product_id": "a",
                            "version": "1",
                            "android_system_version": "0.2"
                        },
                        {
                            "device_uuid": "abd",
                            "product_id": "b",
                            "version": "1",
                            "android_system_version": "0.2"
                        },
                        {
                            "device_uuid": "abe",
                            "product_id": "a",
                            "version": "2",
                            "android_system_version": "0.2"
                        }
                    ]
                }
            }
    }


# 升级结果回调
def dl_upgrade_version_switch_fail(family_id):
    timestamp = int(time.time())
    return{
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_version_switch",
                "req_id": 123,
                "timestamp": timestamp,
                # "ios_version": "0.6.0"
            }
    }


def dl_upgrade_version_switch(family_id):
    timestamp = int(time.time())
    return{
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_version_switch",
                "req_id": 123,
                "timestamp": timestamp,
                "ios_version": "0.6.0"
            }
    }


def dl_upgrade_router(family_id):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_router",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_version": "0.0.1",
                    "android_system_version": "0.0.1",
                    "router_id": config.R_router_id,
                    "router_uuid": "a",
                    "list": [
                        {
                            "device_uuid": "abc",
                            "product_id": "a",
                            "version": "1",
                            "android_system_version": "0.2"
                        },
                        {
                            "device_uuid": "abd",
                            "product_id": "b",
                            "version": "1",
                            "android_system_version": "0.2"
                        },
                        {
                            "device_uuid": "abe",
                            "product_id": "a",
                            "version": "2",
                            "android_system_version": "0.2"
                        }
                    ]
                }
            }
    }


def dl_report_upgrade_sta(family_id):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_report_upgrade_sta",
                "timestamp": timestamp,
                "req_id": 123,
                "msg_tag": "xx",
                "params": {
                            "version": "0.1.5",
                            "pkg_type": 1,  # UPGRADE_PKG_TYPE
                            "product_id": "000c229d20",
                            "upgrade_sta": 0, #  0 - 未开始、1 - 升级中、2 - 已完成、3 - 升级失败
                            "uuid": config.router_uuid,
                            "family_id": family_id,
                            "device_name": ""
                }
            }
    }


# APP检查升级
def dl_upgrade_app(app_uuid):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_app",
                "timestamp": timestamp,
                "req_id": 123,
                "msg_tag": "xx",
                "params": {
                            "os_type": "Android/Android_Pad/IOS/IOS_Pad", # 大小写敏感
                            "app_version": "0.1.0",
                            "router_version": "0.1.0",
                            "app_uuid": config.app_uuid,
                            "router_uuid": config.router_uuid,
                            "user_id": config.user_id
                }
            }
    }


# H5资源包检查升级

def dl_upgrade_h5(app_uuid):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_h5",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "app_version": "0.1.0",
                    "os_type": "ios",
                    "router_version": "0.1.0",
                    "router_uuid": config.router_uuid,
                    "app_uuid": config.app_uuid,
                    "user_id": config.user_id,
                    "list": [
                        {
                            "product_id": "a",
                            "version": "0.0.1"
                        }
                    ]
                }
            }
    }


# 路由器检查升级
def dl_upgrade_rounter(family_id):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_router",
                "req_id": 123,
                "timestamp": timestamp,
                "params": {
                    "router_version": "0.0.1",
                    "android_system_version": "0.0.1",
                    "router_id": config.router_id,
                    "router_uuid": "a",
                    "list": [
                        {
                            "device_uuid": config.router_uuid,
                            "product_id": "000c229d20",
                            "version": "1",
                            "android_system_version": "0.2"
                        }
                    ]
                }
            }
    }


def dl_upgrade_app_fail(app_uuid):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_app",
                "timestamp": timestamp,
                "req_id": 123,
                "msg_tag": "xx",
                "params": {
                            "os_type": "Android", # 大小写敏感
                            "app_version": "0.1.0",
                            "router_version": "0.1.0",
                            "app_uuid": config.app_uuid,
                            "router_uuid": config.router_id,      #
                            "user_id": config.user_id
                }
            }
    }


def dl_upgrade_h5_fail(app_uuid):
    timestamp = int(time.time())
    return{
        "uuid": config.router_uuid,
        "encry": "false",
        "content":
            {
                "method": "dl_upgrade_h5",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "app_version": "0.1.0",
                    "os_type": "ios",
                    "router_version": "0.1.0",
                    "router_uuid": config.router_id,          #
                    "app_uuid": config.app_uuid,
                    "user_id": config.user_id,
                    "list": [
                        {
                            "product_id": "a",
                            "version": "0.0.1"
                        }
                    ]
                }
            }
    }
