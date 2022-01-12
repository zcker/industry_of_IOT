#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-8 下午 03:56
# Author:ZhangChengkai
# @File    : store_data.py
from get_bigiot_data import get_bigiot_data
from tqdm import tqdm


class store_data(get_bigiot_data):
    def store_interface_value(self, table, id):
        """
        存储接口信息
        :param table: 表名
        :param id:接口号
        :return:tqdm界面
        """
        tem_data = self.get_interface_history(id)
        for keyvalue in tqdm(tem_data):
            self.insert_interface(table, int(keyvalue['time']), keyvalue['value'])

    def store_device_data(self, id):
        """
        存入设备的信息
        :param id: 设备id
        :return: log信息
        """
        device_data = self.get_device_data(id)
        self.insert_device_info(device_data['id'], device_data['title'], device_data['description'],
                                device_data['online'], device_data['encrypt'], device_data['online_time'])
