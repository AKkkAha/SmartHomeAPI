import logging
import config
import time
import os


class logcls:
    _singleton = None
    logger = None

    def __init__( self):
        pass

    @staticmethod
    def initial():
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        filename = "log\\"+now + r"_log.txt"
        if 'log' not in os.listdir(os.getcwd()):
            os.mkdir('log')
        if logcls._singleton is None:
            logcls._singleton = logcls()
        logger = logging.getLogger(__name__)
        if not logger.handlers:
            logger.setLevel(level=logging.INFO)
            handler = logging.FileHandler(filename)
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        logcls.logger=logger
        return logcls._singleton


    @staticmethod
    def log(msg):
        #if logcls._singleton is None:
            #logcls._singleton = logcls()
        logcls.logger.info(str(msg) + '\n')
        # logger.debug(msg)
        # logger.warning(msg)
        # logger.info(msg)




class rstcls:
    _singleton = None
    logger1 = None

    def __init__( self):
        pass

    @staticmethod
    def initial():
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        filename1 = "result\\"+now + r"_result.txt"
        if 'result' not in os.listdir(os.getcwd()):
            os.mkdir('result')
        if rstcls._singleton is None:
            rstcls._singleton = rstcls()
        logger1 = logging.getLogger("result")

        if not logger1.handlers:
            logger1.setLevel(level=logging.INFO)
            handler = logging.FileHandler(filename1)
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger1.addHandler(handler)
        rstcls.logger1=logger1
        return rstcls._singleton


    @staticmethod
    def log(msg):
        #if logcls._singleton is None:
            #logcls._singleton = logcls()
        rstcls.logger1.info(str(msg))
        # logger.debug(msg)
        # logger.warning(msg)
        # logger.info(msg)