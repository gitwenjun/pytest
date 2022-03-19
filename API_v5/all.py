# -*- encoding: utf-8 -*-
"""
@时间:   2021/10/30 21:55
@作者:   王齐涛
@文件:   all.py 
"""
import os
import time
from datetime import datetime
import pytest
from common.all_paths import ALLURE_REPORT, ALLURE_PATH
from send_email.email_qq import send_Email_qq
from send_email.email_wechat import send_Email_wechat
from send_email.zip_file import zip_dir


if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system("allure generate ./allure/temps -o ./allure/report --clean")
    zip_dir(ALLURE_REPORT, ALLURE_PATH)    # 调用封装好的压缩文件夹方法
    time.sleep(2)

    # send_Email_qq(ALLURE_PATH)
    # send_Email_wechat(ALLURE_PATH)

    # os.system("allure open -h 192.168.4.4 -p 8083 ./allure_report/")  # 再次生成报告
    # os.system("allure open -h 192.168.4.4 -p 8083 ./allure_report/")  # 自动打开报告
    # 在cmd中输入allure serve "解压后的文件名"      就可以查看allure报告了
