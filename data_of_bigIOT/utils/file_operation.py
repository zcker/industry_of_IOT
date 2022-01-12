#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-7 上午 09:59
# Author:ZhangChengkai
# @File    : file_operation.py
# 该文件用来控制文件的读写
import json


def save(data, path):
    """
    保存文件
    :param data: 数据
    :param path: 路径
    :return: 无
    """
    with open(path, 'w') as fp:
        fp.write(data)


def load(path):
    """
    根据路径加载数据
    :param path:路径
    """
    with open(path) as fp:
        data = json.load(fp)
    return data


def read_token(path):
    """
    直接返回access_token字符串
    :param path: 路径
    :return: access_token
    """
    data = load(path)
    return data['access_token']
