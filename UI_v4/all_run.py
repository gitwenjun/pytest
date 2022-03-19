# -*- encoding: utf-8 -*-
"""
@时间:   2021/10/30 21:55
@作者:   王齐涛
@文件:   all_run.py
"""
import os
import time
import pytest
from send_email.email_qq import send_Email_qq
from send_email.email_wechat import send_Email_wechat

if __name__ == '__main__':
    pytest.main()
    time.sleep(2)   # 等待出报告

    # send_Email_qq("./html_report/report.html")
    # send_Email_wechat("./html_report/report.html")
    os.system("allure generate ./allure_temps -o ./allure_report --clean")
    # os.system("allure open -h 192.168.4.4 -p 8083 ./allure_report/")  # 再次生成报告
    # os.system("allure open -h 192.168.4.4 -p 8083 ./allure_report/")  # 打开报告
