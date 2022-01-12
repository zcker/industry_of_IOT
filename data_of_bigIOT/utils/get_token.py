#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-7 上午 10:56
# Author:ZhangChengkai
# @File    : get_token.py
# 本文件负责爬取access_token并存储在文件中,access_token有效期2天
# 千万不能随便爬取使用

import requests
import file_operation

path = "../token.json"
url = "https://www.bigiot.net/oauth/token"
params = {'client_id': '1179',
          'client_secret': '8bcc6ddd97',
          'username': '17867',
          'password': '39c5c82d1e',
          'grant_type': 'password'}


def get_token(url, params, path):
    """
    获取token的函数
    :param url:网址
    :param params:参数
    :param path:地址
    :return:token
    """
    response = requests.post(url, params)
    print(response.content.decode())
    file_operation.save(response.text, path)


get_token(url, params, path)
