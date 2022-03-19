# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/21 18:02
@作者 ： 王齐涛
@文件名称： zip_file.py 
'''
import os
import zipfile
from common.logger_handler import GetLogger

log = GetLogger()

def zip_dir(dir_path, zip_path):
    """
    :param dir_path: 需要压缩的文件目录
    :param zip_path: 压缩后存放的位置
    :return:
    """
    zip_name = ".zip"
    with zipfile.ZipFile(zip_path+zip_name, "w", zipfile.ZIP_DEFLATED) as f:
        for dirpath, dirnames, filenames in os.walk(dir_path):
            fpath = dirpath.replace(dir_path,'')    # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''     # 这句话理解我也很纳闷，实现当前文件夹以及包含的所有文件的压缩
            for filename in filenames:
                f.write(os.path.join(dirpath, filename), fpath+filename)
    log.debug(f"文件：{dir_path} 压缩成功! 存放的位置：{zip_path}")


# if __name__ == '__main__':
#     zip_dir(r"G:\Python_code\Interface_Automation_v2\allure_report",r"G:\Python_code\Interface_Automation_v2\html_report\allure")