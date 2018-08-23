#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
pip install pypiwin32
pip install wmi
'''

import logging
import sys
import time
import json
import traceback
import urllib.parse
import urllib.request

from constant import constant
from DeviceInfoCollector import DeviceInfoCollector


def usage():
    """
    帮助说明
    :return:
    """
    msg = '''
    usage:
    python main.py opt
    
    opt:
    collect_data        收集硬件信息
    report_data         收集硬件信息并汇报
    test_data           汇报测试用硬件信息
    '''
    logging.info(msg)


def collect_data():
    """收集硬件信息"""
    info = DeviceInfoCollector()
    asset_data = info.collect()
    logging.info(asset_data)
    return asset_data


def report_data(data):
    """
    将信息发送到服务器
    :return:
    """
    data = {"asset_data": json.dumps(data)}
    url = 'http://{}:{}{}'.format(constant.SERVER, constant.PORT, constant.URL)
    logging.info('正在将数据发送至：{}'.format(url))
    try:
        # 使用Python内置的urllib.request库，发送post请求。
        # 需要先将数据进行封装，并转换成bytes类型
        data_encode = urllib.parse.urlencode(data).encode()
        response = urllib.request.urlopen(url=url, data=data_encode, timeout=constant.REQUEST_TIMEOUT)
        message = response.read().decode()
        logging.info("发送完毕, 返回结果：%s" % message)
    except Exception as e:
        logging.error('发送失败: {}'.format(str(e)))


def initlogging(logFile=u"log.txt", toFile=False):
    '''
    示例：
    star.initlogging()
    logging.debug(u"%s %d", u"哈", 1)
    '''
    if toFile is False:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)-6s %(filename)20s:%(lineno)-4d  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            stream=sys.stdout,
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)-6s %(filename)20s:%(lineno)-4d  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=logFile,
            filemode='a',
        )


def main(args):
    if len(args) < 2:
        usage()
    else:
        param = args[1][0:1]
        if param == 'c':
            collect_data()
        elif param == 'r':
            report_data(collect_data())
        elif param == 't':
            report_data(constant.TEST_DATA_WINDOWS_DEVICE)
            report_data(constant.TEST_DATA_LINUX_DEVICE)


if __name__ == '__main__':
    try:
        initlogging()
        main(sys.argv)
    except:
        print(traceback.format_exc())
