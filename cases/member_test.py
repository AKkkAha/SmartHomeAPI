#!/user/bin/env python
#coding=utf-8
import config
import time
from Socket_API import Socket_Cls
import json
import fm_test
import um_test


def get_invite_code():
    socket_invite = Socket_Cls()
    socket_invite.conn()
    socket_invite.send_msg(um_test.um_auth(config.token))
    socket_invite.recv_msg()
    socket_invite.send_msg(fm_test.fm_get_apply_code(config.R_family_id))
    rst = socket_invite.recv_msg()
    code = json.loads(rst)["content"]["result"]["code"]
    socket_invite.close_conn()
    return code


case_aggregate = [
    {"type": "login", "def": "um_login_pwd", "case_name": "APP密码登录", "code": 0},
    {"type": "member", "def": "um_set_pwd", "case_name": "用户修改密码", "code": 0},
    {"type": "member", "def": "fm_update_member", "case_name": "修改成员昵称", "code": 0},
    {"type": "member", "def": "fm_exit_family", "case_name": "用户退出加入家庭", "code": 0},
    {"type": "member", "def": "fm_create_member_fail", "case_name": "创建家庭成员，邀请码错误", "code": -16011},
    {"type": "member", "def": "fm_create_member", "case_name": "创建家庭成员", "code": 0},
    {"type": "login", "def": "um_login_pwd_fail", "case_name": "APP密码登录，密码错误", "code": -17026},
    {"type": "member", "def": "um_set_pwd_fail", "case_name": "用户修改密码，旧密码错误", "code": -17027},
    {"type": "member", "def": "fm_update_member_fail", "case_name": "修改成员昵称，target_user_id错误", "code": -16020},
    {"type": "member", "def": "fm_exit_family_fail", "case_name": "用户退出加入家庭，family_id错误", "code": -16027},
]


def um_register_user_fail(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_register_user",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "pwd": "111111",
                        "secret": config.member_pwd,
                        "phone": "18123123212",
                        "os_type": "Android",
                        "app_version": "v0.5",
                        "os_version": "android4.3",
                        "hardware_version": "Huawei"
                    }
                }
    }


def um_register_user(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_register_user",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "pwd": config.member_password,
                        "secret": config.member_pwd,
                        "phone": config.member_phonenum,
                        "os_type": "Android",
                        "app_version": "v0.5",
                        "os_version": "android4.3",
                        "hardware_version": "Huawei"
                    }
                }
    }


def fm_exit_family_fail(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "fm_exit_family",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "params": {
                        "family_id": config.user_id
                    }
                }
    }


def fm_update_member_fail(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "fm_update_member",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "real_id": config.member_id,
                    "params": {
                        "user_name": "API_TEST",
                        "target_user_id": config.user_id,
                        "family_id": config.R_family_id
                    }
                }
    }


def fm_create_member_fail(arg):
    timestamp = int(time.time())
    code = get_invite_code()
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "fm_create_member",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "params": {
                        "family_id": config.R_family_id,
                        "code": config.R_router_pwd
                    }
                }
    }


def um_set_pwd_fail(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_set_pwd",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "pwd_old": config.router_pwd,
                        "pwd_new": config.member_pwd
                    }
                }
    }


def um_login_pwd_fail(arg):
    timestamp = int(time.time())
    phonenum = "18565637021"
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_login_pwd",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "phone": phonenum,
                        "pwd": config.router_pwd,
                        "os_type": "Android",
                        "app_version": "v0.5",
                        "os_version": "android4.3",
                        "hardware_version": "Huawei",
                        "phone_name": "abccc",
                        "sso": 1
                        }
                }
    }


def fm_exit_family(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "fm_exit_family",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "params": {
                        "family_id": config.R_family_id
                    }
                }
    }


def fm_update_member(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "fm_update_member",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "real_id": config.member_id,
                    "params": {
                        "user_name": "API_TEST",
                        "target_user_id": config.member_id,
                        "family_id": config.R_family_id
                    }
                }
    }


def fm_create_member(arg):
    timestamp = int(time.time())
    code = get_invite_code()
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "fm_create_member",
                    "req_id": 123,
                    "timestamp": timestamp,
                    "params": {
                        "family_id": config.R_family_id,
                        "code": code
                    }
                }
    }


def um_set_pwd(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_set_pwd",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "pwd_old": config.member_pwd,
                        "pwd_new": config.member_pwd
                    }
                }
    }


def um_login_pwd(arg):
    timestamp = int(time.time())
    return {
            "uuid": config.member_phonenum,
            "encry": "false",
            "content":
                {
                    "method": "um_login_pwd",
                    "timestamp": timestamp,
                    "req_id": 123,
                    "params": {
                        "phone": config.member_phonenum,
                        "pwd": config.member_pwd,
                        "os_type": "Android",
                        "app_version": "v0.5",
                        "os_version": "android4.3",
                        "hardware_version": "Huawei",
                        "phone_name": "abccc",
                        "sso": 1
                        }
                }
    }
