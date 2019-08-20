#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import paramiko
import re
import logger

def get_phone_code(phonenumber, timeouts=5):
    try:
        time.sleep(3)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('xx.xx.xx.xx', xx, 'xxxxxxxxxxx', 'xxxxxxxxxxxxxxxx', timeout=timeouts)
        sftp_client = client.open_sftp()
        remote_file = sftp_client.open('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'r')
        temp_file = remote_file.read()
        #temp_file = bytes.decode(temp_file)
        #print "check file"
        if re.match('.*mobiles=%s.*' % phonenumber, temp_file, re.DOTALL):
            auth_code = re.findall('.*?mobiles=%s&.*\[(.*?[\d])\].*?' % phonenumber, temp_file)
            response = str(auth_code[-1])
        else:
            response = 'None'
        remote_file.close()
        # stdin, stdout, stderr = client.exec_command(
        #     'redis-cli -h localhost -p 6379 -a hdiot HMGET Phone:code_%s_4 code' % phonenumber)
        # res, err = stdout.read(), stderr.read()
        # response = bytes.decode(res).rstrip('\n')
        client.close()
        msg = '获取验证码：%s' % response
        if response == None:
            print "get code failed, try again!"
            logger.logcls.initial().log("get code failed, try again!")
        #logger.logger.info(msg)
        return response
    except:
        # print(traceback.format_exc())
        # raise CustomException('获取验证码失败')
        print "get code failed"
        logger.logcls.initial().log("get code failed!!")
