from Common.all_path import PHOTO_PATH
import os
from datetime import datetime
from Common.logs import logger
import traceback

class ScreenShot:

    # 一级目录
    @staticmethod
    def dateDir():
        dateDir = os.path.join(PHOTO_PATH,datetime.now().strftime('%Y'))
        if not os.path.exists(dateDir):
            os.mkdir(dateDir)
        return dateDir


    # 二级目录
    @staticmethod
    def timeDir():
        timeDir = os.path.join(ScreenShot().dateDir(),datetime.now().strftime("%m-%d"))
        if not os.path.exists(timeDir):
            os.mkdir(timeDir)
        return timeDir

    #截图方法
    @staticmethod
    def screeshotPhoto(driver,name):
        file_time = datetime.now().strftime("%H-%M-%S")
        photoName = os.path.join(ScreenShot().timeDir(),name+file_time+'.jpg')
        try:
            driver.get_screenshot_as_file(photoName)
            logger.info(f"截图成功，保存位置：{ScreenShot.timeDir()}")
        except Exception:
            logger.debug(f"截图失败,报错提示：{traceback.print_exc()}")
            raise


# if __name__ == '__main__':
#     s = ScreenShot()
#     driver = webdriver.Chrome()
#     s.screeshotPhoto(driver,'测试')