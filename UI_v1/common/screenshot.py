import os
from datetime import datetime
from common.all_path import Photos_path
from common.log_handler import logger
import traceback


class Screenshot:

    @staticmethod
    def dateDir():
        date_dir = os.path.join(Photos_path, datetime.now().strftime("%Y"))
        if not os.path.exists(date_dir):
            os.mkdir(date_dir)
        return date_dir

    @staticmethod
    def time_Dir():
        time_Dir = os.path.join(Screenshot.dateDir(), datetime.now().strftime("%m-%d"))
        if not os.path.exists(time_Dir):
            os.mkdir(time_Dir)
        # print(time_Dir)
        return time_Dir

    @staticmethod
    def photo_screenshoot(driver,name):
        photo_time = datetime.now().strftime("%H:%M-%S")
        photo_name = os.path.join(Screenshot.time_Dir(),photo_time+name+'.png')
        try:
            driver.get_screenshot_as_file(photo_name)
            logger.info(f"截图成功-{name}.png，保存位置：{Screenshot.time_Dir()}")
        except:
            logger.error(f"截图失败,报错提示{traceback.print_exc()}")
            raise



if __name__ == '__main__':
    s = Screenshot()
    s.time_Dir()
