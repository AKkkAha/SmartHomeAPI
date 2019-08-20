# -*- coding:utf-8 -*-
phonenum = 'xxxxxxxxxx'    # 测试用户主账号
router_uuid = "xxxxxxxxxxxxxxxxxxxxxxxxxx"        # 未绑定账号的路由器uuid，不需要真实路由器，需要在云端注册
R_router_uuid = "xxxxxxxxxxxxxxxxxxxxxxxxx"        # 绑定测试账号的路由器uuid
router_pwd = "xxxxxxxxxxxxxxxxxxxx"                 # 未绑定账号的路由器随机码
R_router_pwd = "xxxxxxxxxxxxxxxx"                 # 绑定测试账号的路由器随机码
R_router_id = xxxxx                        # 绑定测试账号的路由器云端id
router_id = xxxxx                          # 未绑定账号的路由器云端id
member_phonenum = "xxxxxxxxxxx"            # 成员账号
member_password = "123456"                # 成员密码
member_pwd = "xxxxxxxxxxxxxxxxxx"   # 成员密码 MD5
member_id = xxxxxxx                                  # 成员用户id

# 账号登陆token，有时效，失效后可通过运行GetToken脚本获得
token = {"token": "eyJ1c2VyX2lkIjoyMTc2NiwicGhvbmUiOiIxODkyNjU5MjAxMCIsInRva2VuX3R5cGUiOjMsImNyZWF0ZV90aW1lIjoxNTU3Mjk5MjYyLCJleHBpcmVfdGltZSI6MTU1NzU1ODQ2MiwiZnJvbSI6IlNlcnZlciIsIm5vbmNlIjoidmZwcHFsY2ciLCJzaWciOiI4M2M4MDEzMTNjYzY2ZGQxOGE5NTRmZGEwYWZiMWI2MjYyNTFmZDE3In0=", "user_id": 21766}
app_uuid = "191994auuj8rh969vpq09b8g26ibq7u6"
user_id = xxxxxxxx           # 创建账号的用户id，云端获取
R_family_id = xxxxxxxxxx         # 绑定路由器的家庭family_id，云端获取

# 需要执行的用例模块，请务必添加 end_test 模块来删除测试中产生的家庭，避免创建过多家庭导致后续测试中家庭列表过长
Test_Case = [
            "um_test",
            "fm_test",
            "dm_router_test",
            "dm_room_test",
            "dm_device_test",
            "mg_test",
            "3d_test",
            "member_test",
            "acc_test",
            "dl_test",
            "end_test"
            ]
