#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import platform


def linux_sys_info():
    import SysInfoLinux
    return SysInfoLinux.collect()


def windows_sys_info():
    import SysInfoWin
    return SysInfoWin.collect()


class DeviceInfoCollector(object):

    def collect(self):
        # 收集平台信息
        # 首先判断当前平台，根据平台的不同，执行不同的方法
        try:
            func = getattr(self, platform.system())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统： [%s]! " % platform.system())

    def Darwin(self):
        pass
        # return mac_sys_info()

    def Linux(self):
        return linux_sys_info()

    def Windows(self):
        return windows_sys_info()

    def build_report_data(self, data):
        # 留下一个接口，方便以后增加功能或者过滤数据
        return data