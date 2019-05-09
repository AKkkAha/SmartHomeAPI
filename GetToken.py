#!/usr/bin/python
# -*- coding:utf-8 -*-
from API_test_run import *
from Socket_API import Socket_Cls

socket_token = Socket_Cls()
log = logger.rstcls.initial()
print get_token(socket_token, log)
