#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-1-7 下午 10:13
# Author:ZhangChengkai
# @File    : sql_operation.py
# 本文件负责mysql的操作，插入设备和接口信息
import pymysql
import datetime
import time

import get_bigiot_data


class sql_operation(object):
    def get_conn(self):
        """
        数据库连接
        :return:失败信息
        """
        try:
            self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='industry', port=3306,
                                        charset='utf8')
        except pymysql.Error as e:
            print(e)
            print('数据库连接失败')

    def close_conn(self):
        """
        关闭连接
        :return: 失败信息
        """
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print(e)
            print('数据库关闭失败')

    def insert_device_info(self, id, title, desc, online, encrypt, onlinetime):
        """
        保存设备信息
        :param id: 设备id
        :param title: 设备名称
        :param desc: 设备描述
        :param online: 是否在线
        :param encrypt: 验证信息
        :param onlinetime: 是否在线
        :return: 都打印在console上
        """
        sql = 'INSERT INTO `device_info`(`id`,`title`,`description`,`online`,`encrypt`,`onlinetime`) VALUE(%s,%s,%s,%s,%s,%s)'
        try:
            self.get_conn()
            cursor = self.conn.cursor()
            cursor.execute(sql, (id, title, desc, online, encrypt, onlinetime))
            # 一定需要提交事务，要不不会显示，只会占位在数据库
            self.conn.commit()
            print('设备信息插入成功')
            return 1
        except AttributeError as e:
            print('Error:', e)
            return 0
        except TypeError as e:
            print('Error:', e)
            # 发生错误还提交就是把执行正确的语句提交上去
            # self.conn.commit()
            # 下面这个方法是发生异常就全部不能提交,但语句执行成功的就会占位
            self.conn.rollback()
            return 0
        finally:
            cursor.close()
            self.close_conn()

    def insert_interface(self, table, data_time, value):
        """
        传入接口的信息
        在数据库层面防止数据重复，进行内表not exist 操作
        :param table:表名
        :param data_time:时间
        :param value:参数
        :return:成功失败报错
        """
        sql = 'INSERT INTO ' + table + '(`time`,`value`) SELECT %s,%s FROM DUAL WHERE NOT EXISTS (SELECT `time` FROM '+table+' WHERE `time`= %s)'
        try:
            self.get_conn()
            cursor = self.conn.cursor()
            # 转换时间戳
            data_time = datetime.datetime.fromtimestamp(data_time)
            cursor.execute(sql, (data_time, value, data_time))
            # 一定需要提交事务，要不不会显示，只会占位在数据库
            self.conn.commit()
            return 1
        except AttributeError as e:
            print('Error:', e)
            return 0
        except TypeError as e:
            print('Error:', e)
            # 发生错误还提交就是把执行正确的语句提交上去
            # self.conn.commit()
            # 下面这个方法是发生异常就全部不能提交,但语句执行成功的就会占位
            self.conn.rollback()
            return 0
        finally:
            cursor.close()
            self.close_conn()

    def update(self):
        sql = 'UPDATE `new` SET `author`=%s WHERE `title`=%s'
        try:
            self.get_conn()
            cursor = self.conn.cursor()
            num = cursor.execute(sql, ('sergiojune', 'title'))
            # 提交事务
            self.conn.commit()
            cursor.close()
            return num
        except pymysql.Error as e:
            print(e)
            # 修改失败就回滚
            self.conn.rollback()

        finally:
            if self.conn:
                self.close_conn()

    def delete(self):
        sql = 'DELETE FROM `new` WHERE `view_count`=%s'
        try:
            self.get_conn()
            cursor = self.conn.cursor()
            num = cursor.execute(sql, ('0',))
            self.conn.commit()
            cursor.close()
            return num
        except pymysql.Error as e:
            print('删除数据失败')
            if self.conn:
                self.conn.rollback()
        finally:
            if self.conn:
                self.close_conn()

    def device_duplication(self,id):
        sql='SELECT `id` FROM `device_info` WHERE `id`=%s'
        try:
            self.get_conn()
            cursor = self.conn.cursor()
            cursor.execute(sql, (id))
            # 一定需要提交事务，要不不会显示，只会占位在数据库
            self.conn.commit()
            results = cursor.fetchall()
            print(results)

            return 1
        except AttributeError as e:
            print('Error:', e)
            return 0
        except TypeError as e:
            print('Error:', e)
            # 发生错误还提交就是把执行正确的语句提交上去
            # self.conn.commit()
            # 下面这个方法是发生异常就全部不能提交,但语句执行成功的就会占位
            self.conn.rollback()
            return 0
        finally:
            cursor.close()
            self.close_conn()