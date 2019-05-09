#!/user/bin/env python
#coding=utf-8
import config
import time

case_aggregate = [
    {"type": "app", "def": "_3d_get_dev_key_property", "case_name": "获取品类的属性列表", "code": 0},
    {"type": "app", "def": "_3d_get_dev_product_list", "case_name": "获取产品列表", "code": 0},
    {"type": "app", "def": "_3d_get_dev_type_list", "case_name": "获取设备品类列表", "code": 0},
    {"type": "app", "def": "_3d_get_product_guide_info", "case_name": "获取产品的引导信息", "code": 0},
    {"type": "app", "def": "_3d_get_product_key_property", "case_name": "获取具体产品的属性", "code": 0},
    {"type": "app", "def": "_3d_get_device_fault_info", "case_name": "获取设备故障配置列表", "code": 0},
    {"type": "app", "def": "_3d_get_dev_addtype", "case_name": "添加方式设置信息查询", "code": 0},
    {"type": "app", "def": "_3d_get_distributor_list", "case_name": "获取渠道商列表", "code": 0},
    {"type": "app", "def": "_3d_get_event_msg_info", "case_name": "获取事件配置列表", "code": 0},
    {"type": "app", "def": "_3d_get_manufacturer_licence", "case_name": "获取品牌licence列表", "code": 0},
    {"type": "app", "def": "_3d_get_moji_weather", "case_name": "获取墨迹天气服务", "code": 0},
    {"type": "app", "def": "_3d_get_product_by_url", "case_name": "通过二维码链接获取产品信息", "code": 0},
    {"type": "app", "def": "_3d_get_product_by_firmware", "case_name": "通过渠道设备的固件信息获取产品信息", "code": 0},
]


def _3d_get_product_by_firmware_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_by_firmware",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "pid": "123123",
                    "model": "WA-7501FK",
                    "category": 18,
                    "category_sub": 5019,
                    "channel": "SUNING",
                    "mac": "xx",
                    "sn": "xxx",
                    "manufacturer_name": "海尔"
                }
            }
    }


def _3d_get_product_by_url_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_by_url",
                "timestamp": timestamp,
                "req_id": 123,
                "params":
                    {
                        "url": "www.baidu.com"
                    }
            }
    }


def _3d_get_moji_weather_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_moji_weather",
                "timestamp": timestamp,
                "req_id": 10086,
                "params": {
                    "city_id": "abc"
                }
            }
    }


def _3d_get_distributor_list_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_distributor_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params":
                    {
                        "parent_type_id": 1,  # // 1级品类id，非必传参数
                        "type_id": 4294967299
                    }
            }
    }


def _3d_get_device_fault_info_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_device_fault_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    # "time": 0,
                    "number": 10
                }
            }
    }


def _3d_get_product_by_firmware(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_by_firmware",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "pid": "000794c940",
                    "model": "WA-7501FK",
                    "category": 18,
                    "category_sub": 5019,
                    "channel": "SUNING",
                    "mac": "xx",
                    "sn": "xxx",
                    "manufacturer_name": "海尔"
                }
            }
    }


def _3d_get_product_by_url(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_by_url",
                "timestamp": timestamp,
                "req_id": 123,
                "params":
                    {
                        "url": "http://mapp.suning.com/a.php?s=qrcode/offline&f=website&pack=com.suning.smarthome&pid=0001000500040000&bind=snlink"
                    }
            }
    }


def _3d_get_moji_weather(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_moji_weather",
                "timestamp": timestamp,
                "req_id": 10086,
                "params": {
                    "city_id": 123
                }
            }
    }


def _3d_get_manufacturer_licence(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_manufacturer_licence",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "time": 1511424694,
                    "number": 10
                }
            }
    }


def _3d_get_event_msg_info(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_event_msg_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "time": 0,
                    "number": 10
                }
            }
    }


def _3d_get_distributor_list(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_distributor_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params":
                    {
                        "parent_type_id": 1,  # // 1级品类id，非必传参数
                        "type_id": 5000
                    }
            }
    }


def _3d_get_dev_addtype(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_addtype",
                "timestamp": timestamp,
                "req_id": 123,
            }
    }


def _3d_get_device_fault_info(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_device_fault_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "time": 0,
                    "number": 10
                }
            }
    }


def _3d_get_product_key_property_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_key_property",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "product_id": -1,
                }
            }
    }


def _3d_get_product_key_property(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_key_property",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "product_id": 1,
                }
            }
    }


def _3d_get_product_guide_info_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_guide_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "product_id": "",
                    "type_id": 5008
                }
            }
    }


def _3d_get_product_guide_info(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_product_guide_info",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "product_id": "0007e0bbb2",
                    "type_id": 5008
                }
            }
    }


def _3d_get_dev_type_list_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_type_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "time": 0,
                    "number": 10,
                    "is_need_child_type": 0,
                    "app_id": "100001"
                }
            }
    }


def _3d_get_dev_type_list(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_type_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "time": 1511424694,
                    "number": 10,
                    "is_need_child_type": 0,
                    "app_id": "100001"
                }
            }
    }


def _3d_get_dev_product_list_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_product_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "parent_type_id": -1,
                    "status": 0,
                    "time": 1511424694,
                    "number": 10
                }
            }
    }


def _3d_get_dev_product_list(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_product_list",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "parent_type_id": 0,
                    "status": 0,
                    "time": 1511424694,
                    "number": 10
                }
            }
    }


def _3d_get_dev_key_property_fail(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_key_property",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "type_id": 1,
                    "type_id_arr": []
                }
            }
    }


def _3d_get_dev_key_property(arg):
    timestamp = int(time.time())
    return {
        "uuid": config.phonenum,
        "encry": "false",
        "content":
            {
                "method": "3d_get_dev_key_property",
                "timestamp": timestamp,
                "req_id": 123,
                "params": {
                    "type_id": 1,
                    "type_id_arr": [1, 2, 3]
                }
            }
    }
