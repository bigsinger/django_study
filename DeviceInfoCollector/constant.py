#!/usr/bin/env python
# -*- coding:utf-8 -*-


class constant:
    @staticmethod
    def test():
        pass


# 服务器配置
constant.SERVER = '10.240.208.158'
constant.PORT = 8001
constant.URL = '/assets/report/'
constant.REQUEST_TIMEOUT = 30

constant.TEST_DATA_WINDOWS_DEVICE = {
    "os_type": "Windows",
    "os_release": "7 64bit  6.1.7601 ",
    "os_distribution": "Microsoft",
    "asset_type": "server",
    "cpu_count": 2,
    "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
    "cpu_core_count": 8,
    "ram": [
        {
            "slot": "A1",
            "capacity": 8,
            "model": "Physical Memory",
            "manufacturer": "kingstone ",
            "sn": "456"
        },

    ],
    "manufacturer": "Intel",
    "model": "P67X-UD3R-B3",
    "wake_up_type": 6,
    "sn": "00426-OEM-8992662-7777",
    "physical_disk_driver": [
        {
            "iface_type": "unknown",
            "slot": 0,
            "sn": "3830414130423230343234362020202020202020",
            "model": "KINGSTON SV100S264G ATA Device",
            "manufacturer": "(标准磁盘驱动器)",
            "capacity": 128
        },
        {
            "iface_type": "SATA",
            "slot": 1,
            "sn": "383041413042323023234362020102020202020",
            "model": "KINGSTON SV100S264G ATA Device",
            "manufacturer": "(标准磁盘驱动器)",
            "capacity": 2048
        },

    ],
    "nic": [
        {
            "mac": "0A:01:27:00:00:00",
            "model": "[00000013] VirtualBox Host-Only Ethernet Adapter",
            "name": 13,
            "ip_address": "192.168.56.1",
            "net_mask": [
                "255.255.255.0",
                "64"
            ]
        },
        {
            "mac": "24:CF:22:FF:48:34",
            "model": "[00000017] Microsoft Virtual WiFi Miniport Adapter",
            "name": 17,
            "ip_address": "",
            "net_mask": ""
        },
        {
            "mac": "24:CF:22:FF:48:34",
            "model": "Intel Adapter",
            "name": 17,
            "ip_address": "192.1.1.1",
            "net_mask": ""
        },
    ]
}

constant.TEST_DATA_LINUX_DEVICE = {
    "asset_type": "server",
    "manufacturer": "innotek GmbH",
    "sn": "00007",
    "model": "VirtualBox",
    "uuid": "E8DE611C-4279-495C-9B58-502B6FCED076",
    "wake_up_type": "Power Switch",
    "os_distribution": "Ubuntu",
    "os_release": "Ubuntu 16.04.3 LTS",
    "os_type": "Linux",
    "cpu_count": "2",
    "cpu_core_count": "4",
    "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
    "ram": [
        {
            "slot": "A1",
            "capacity": 8,
        }
    ],
    "ram_size": 3.858997344970703,
    "nic": [],
    "physical_disk_driver": [
        {
            "model": "VBOX HARDDISK",
            "size": "50",
            "sn": "VBeee1ba73-09085302"
        }
    ]
}
