# coding=gbk
from get_bigiot_data import *
from sql_operation import *
from store_data import *
from report_error import *
import threading
import time
import schedule


def main_process():
    store_data.store_interface_value('temperature', '22026')
    store_data.store_interface_value('gas', '22028')
    store_data.store_interface_value('weight', '22030')
    store_data.store_interface_value('water', '22027')
    store_data.store_interface_value('door', '22031')
    store_data.store_interface_value('fire', '22029')
    report_error.error_trigger('22027', '锅炉水位报警！危险！')
    report_error.error_trigger('22029', '明火出现报警！危险！')
    report_error.error_trigger('22031', '重要设备误动报警！危险！')

    return main_process()


if __name__ == '__main__':
    store_data = store_data()
    report_error = report_error()

    # 每3分钟爬取数据
    schedule.every(3).minutes.do(main_process())
    while True:
        schedule.run_pending()
        time.sleep(1)
