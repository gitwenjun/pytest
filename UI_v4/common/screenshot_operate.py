# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 23:24
@作者 ： 王齐涛
@文件名称： screenshot_operate.py
'''
import os
import traceback
from datetime import datetime
from common.all_paths import PTHOTOS_PATH
from common.logger_handler import GetLogger


log = GetLogger()

class ScreenshotOperate:


    @staticmethod   #直接类名.属性名或类名.方法名调用
    def currenDate():
        """目录，以年月日 命名"""
        catalogue_name=datetime.now().strftime('%Y')
        return catalogue_name


    @staticmethod
    def currenTime():
        """目录下的子文件，以小时分钟 命名"""
        file_name=datetime.now().strftime('%m-%d')
        return file_name


    @staticmethod
    def currenpath():
        """判断目录和目录下的文件是否存在，不存在就创建"""
        dateDir = os.path.join(PTHOTOS_PATH,ScreenshotOperate().currenDate())
        if not os.path.exists(dateDir):
            os.mkdir(dateDir)
        timeDir = os.path.join(dateDir,ScreenshotOperate().currenTime())
        if not os.path.exists(timeDir):
            os.mkdir(timeDir)
        return timeDir


    @staticmethod
    def screenshot_operate_method(driver, name):
        """命名规范 【xx页面_xx操作_截屏时间.png 】"""
        """外部调用的方法，其中savepat默认调用内部封装的currenpath方法"""
        photo_name = datetime.now().strftime('%H-%M-%S')
        path = os.path.join(ScreenshotOperate().currenpath(), name+photo_name+'.png')
        try:
            driver.get_screenshot_as_file(path)
            log.info(f"截图成功：{name}.png ,保存路径：{ScreenshotOperate().currenpath()}")
        except Exception:
            log.error(f"截图失败：{name} ,报错提示：{traceback.print_exc()}")
            raise









