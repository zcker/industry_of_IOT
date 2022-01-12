#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-7 上午 10:53
# Author:ZhangChengkai
# @File    : get_bigiot_data.py
# desc: 本文件负责从贝壳物联获取数据，包括设备信息，接口历史信息
import requests
import file_operation
import json

from sql_operation import sql_operation


class get_bigiot_data(sql_operation):
    access_token = ''
    path = "token.json"

    def __init__(self):
        self.access_token = file_operation.read_token(self.path)

    def get_interface_history(self, id):
        """
        通过接口去取得数据并返回为python的字典嵌套数组
        :param id: 接口的名称,字符串格式
        :return: python的字典嵌套数组，通过data[][]调用
        {'value': '-25', 'time': '1641377771'}
        """
        url = 'https://www.bigiot.net/oauth/historydata?access_token=' + self.access_token + '&id=' + id
        response = requests.get(url)
        # print(response.content.decode(encoding="utf-8-sig"))
        response = response.content.decode(encoding="utf-8-sig")  # 转换格式，防止'gbk' codec can't encode character '\ufeff'
        json_data = json.loads(response)
        print('设备信息 get_interface_history:')
        print(json_data)
        return json_data

    def get_device_data(self, id):
        """
        设备信息
        :param id:设备的编号
        :return: python的dict
        [{'id': '24409', 'uid': '17867', 'title': 'industry_sim', 'category_id': '0',
         'description': '模拟工业设备', 'open': '1', 'open_listen': '1', 'online': '0',
          'encrypt': '0', 'image': '', 'lat': '32.1951159', 'lng': '119.4302895', 'online_time': '49813'}
        """
        url = 'https://www.bigiot.net/oauth/dev?access_token=' + self.access_token + '&id=' + id
        response = requests.get(url)
        response = response.content.decode(encoding="utf-8-sig")  # 转换格式，防止'gbk' codec can't encode character '\ufeff'
        # print(response)
        json_data = json.loads(response)
        print('设备信息 get_device_data:')
        print(json_data)
        return json_data
