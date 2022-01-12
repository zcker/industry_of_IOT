#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-9 下午 04:34
# Author:ZhangChengkai
# @File    : report_error.py
import mail_operation
from get_bigiot_data import get_bigiot_data
import time
import datetime


class report_error(get_bigiot_data):
    def error_trigger(self, id, device):
        """
        警报发出器
        :param id: 设备接口
        :param device: 设备名
        :return: 邮件
        """
        json_data = self.get_interface_history(id)
        for keyvalue in json_data:
            if (keyvalue['value'] == '999') and (time.time() - float(keyvalue['time']) < 500):
                data_time = datetime.datetime.fromtimestamp(keyvalue['time'])
                report = mail_operation.SendMail('smtp.163.com', 25, '18962507373@163.com', 'AKHKCJNKNLTAKDBM')
                report.send('ooffiioo@qq.com', device, '设备于' + data_time + '发出警报，危险！请及时处理！')
