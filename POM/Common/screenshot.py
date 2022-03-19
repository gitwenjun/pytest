from Common.all_path import PHOTO_PATH
import os
from datetime import datetime
from Common.logs import logger
import traceback

class ScreenShot:

    # 一级目录名
    @staticmethod
    def curren_date():
        date_name = os.path.join(PHOTO_PATH,datetime.now().strftime('%Y'))
        if not os.path.exists(date_name):
            os.mkdir(date_name)
        return date_name

    # 二级目录名
    @staticmethod
    def time_dir():
        time_name = os.path.join(ScreenShot().curren_date(),datetime.now().strftime('%m-%d'))
        if not os.path.exists(time_name):
            os.mkdir(time_name)
        return time_name

    # 截图方法
    @staticmethod
    def screen_shot(driver,name):
        # 生成当前时间
        file_time = datetime.now().strftime('%H-%M-%S')
        # 文件名
        photo_name = os.path.join(ScreenShot().time_dir(),name+file_time+".png")
        try:
            driver.get_screenshot_as_file(photo_name)
            logger.debug(f"截图成功：{name},保存路径为：{ScreenShot().time_dir()}")
        except Exception:
            logger.error(f"截图失败：{name},报错提示：{traceback.print_exc()}")
            raise


if __name__ == '__main__':
    s = ScreenShot()
    s.screen_shot('测试')