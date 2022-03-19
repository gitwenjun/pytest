# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/15 16:19
@作者 ： 王齐涛
@文件名称： Base.py 
'''
import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import traceback
from common.all_paths import PTHOTOS_PATH
from config.element_type import LOCATE_MODE
from data.user_data import front_url
from common.logger_handler import GetLogger
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Base:

    url = front_url
    menuFrameName = "menu-frame"  # 左边列表框架
    mainFrameName = "main-frame"  # 输入页面框架
    topFrameName = "header-frame"  # 顶部框架
    log = GetLogger()

    def __init__(self,browser):
        """
        初始化浏览器
        :param browser:
         """
        self.driver = browser
        self.timeout = 10   # 显示等待中超时等待参数
        self.wait = WebDriverWait(self.driver,self.timeout)

    @staticmethod
    def element_locator(func,locator):  # locator 传过来是('name', 'username')
        name, value = locator  # name ,value =('name', 'username')
        return func(LOCATE_MODE[name], value)  # func(By.name,username)  name="by.name",value="username"

    def find_element(self,locator):
        """
        lambda表达式 表示等待10s，每隔1s去检查一次元素是否出现，出现了就执行下一步，直到10,结束后还没有出现就会抛出异常。
        lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
        """
        return Base.element_locator(lambda *args: self.wait.until(EC.presence_of_element_located(args)),locator) # ('xpath', "//a[text()='登录")


    def find_elements(self,locator):
        """此处注意，如果省略message=“”也就是locator，则By.ID外面是三层()  args就是('name', 'username')"""
        return Base.element_locator(lambda *args: self.wait.until(EC.presence_of_element_located(args)),locator)

    def element_num(self, locator):
        number = len(self.find_elements(locator))
        self.log.debug(f"{locator,number}相同的元素")
        return number

    def open_url(self):
        """
        打开网址并进行验证，本方法没有传入url参数，是因为在每个page中定义了url，直接调用就好，所以在定义时，不要忘记url参数
        :return:
        """
        self.driver.maximize_window()
        self.log.debug("浏览器最大化")
        # self.driver.set_page_load_timeout(10)   # 设置网页超时加载时间,默认页面会加载完成才进入到下一步
        try:
            self.driver.get(self.url)
            self.log.debug(f"读取url：{self.url}")
        except TimeoutException:
            raise TimeoutException(f"打开{self.url}超时请检查网络或网址服务器")

    def exit_driver(self):
        """
        退出驱动并关闭所有关联的窗口
        :return:
        """
        self.driver.quit()
        self.log.debug("退出驱动并关闭所有关联的窗口")

    # def find_element(self,ele_loc):
    #     """
    #     定位单个元素
    #     :param ele_loc: 传入的是元组 比如 （id,"name"）
    #     :return:
    #     """
    #
    #     try:
    #         # self.log.debug(f"定位元素的方法：{ele_loc[0]}，定位元素的属性：{ele_loc[1]}")
    #         print(ele_loc)
    #         ele = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(ele_loc),message="cuowu") # 定位成功后会返回一个True
    #         print(ele)
        #     if ele:
        #         self.log.debug(f"元素定位成功")
        #     else:
        #         start = datetime.now()   # 获取起始时间（显示的是年月日时分秒）
        #         while not ele:
        #             element = EC.presence_of_element_located(*ele_loc)  # 显示等待的另一种方法
        #             end = datetime.now()       # 获取结束时间
        #             if element:
        #                 self.log.debug(f"元素二次定位成功,所耗时间：{(start - end).seconds}")  # 计算时间差 其中.seconds忽略天 只看时分秒
        #                 break
        #             elif (start - end).seconds > 86389:  # 定位时间超过10秒就退出
        #                 self.log.debug(f"元素二次定位失败，元素是不可见的")
        #                 break
        #             else:
        #                 continue
        # except Exception as msg:
        #     # self.log.error(f"元素定位失败：{msg}")
        #     raise
        # else:
        #     return ele

        
        
    def wait_visible_element(self, ele_loc):
        """
        判断元素是否存在
        :param ele_loc:
        :return:
        """
        ele = self.find_element(ele_loc)
        if len(ele) == 1:
            return True
        else:
            return False

    def click(self, ele_loc):
        """
        元素点击
        :return:
        """
        ele = self.find_element(ele_loc)    #('xpath', "//a[text()='登录")
        ele.click()
        self.log.debug(f"点击元素：{ele_loc}")

    def send_keys(self,ele_loc,text,clear_first=True):
        """
        输入文本内容
        :param ele_loc:
        :param text: 输入的文本
        :param clear_first: 是否对文本框进行数据清空的选项。默认是
        :return:
        """
        ele = self.find_element(ele_loc)
        try:
            if clear_first:
                ele.clear()
                ele.send_keys(text)
                self.log.debug(f"输入的值：{text}")
            else:
                ele.send_keys(text)
                self.log.debug(f"输入的值：{text}")

        except BaseException as b:
            self.log.error(f"代码报错信息: {b}")

    def clear(self,ele_loc):
        """
        清空内容
        :param ele_loc:
        :return:
        """
        ele = self.find_element(*ele_loc)
        ele.clear()
        self.log.debug("清空输入框内容")

    def gain(self,ele_loc):
        """
        获取页面内容
        :param ele_loc:
        :return:
        """
        ele = self.find_element(*ele_loc)
        self.log.info(f"获取界面的信息：{ele.text}")
        return ele.text

    def select(self,ele_loc,method,data):
        """
        操作下拉框选项
        :param ele_loc: 定位下拉框的元素
        :param method: 选择哪一种方法定位下拉框选项
        :param data: 输入的值
        :return:
        """
        ele = self.find_element(*ele_loc)
        ele.click()
        if method == "value":
            Select(ele).select_by_value(f'{data}')

        elif method == "text":
            Select(ele).select_by_visible_text(f"{data}")

        elif method == "index":
            Select(ele).select_by_index(f'{data}')

    def switch_frame(self,input_one_level, input_two_level):
        """
        切换页面框架
        :param input_one_level:  输入左边列表菜单中的一级选项定位元素
        :param input_two_level:  输入左边列表菜单中的二级选项选项
        :return:
        """
        self.driver.switch_to.frame(self.menuFrameName)  # 切换到顶部框架
        self.click(input_one_level)     # 在data中global_variable.py文件已封装该元素
        self.click((By.XPATH, f"//a[@target='main-frame'][text()='{input_two_level}']"))
        self.driver.switch_to.default_content()  # 切换到最外部框架
        self.driver.switch_to.frame(self.mainFrameName)  # 切换到页面框架

    def new_window(self, new_url="输入新的URL地址"):
        """
        生成新的窗口
        :param new_url:
        :return:
        """
        js = "window.open('{}','_blank');"
        self.driver.execute_script(js.format(new_url))  # 生成一个变量存储新的网址

    def switch_new_window(self):
        """
        切换至新窗口
        :return:
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])  # 切换到最新的窗口

    def switch_old_window(self):
        """
        切换至旧窗口
        :return:
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def switch_to_default(self):
        """
        切换回默认窗口
        :return:
        """
        self.driver.switch_to.default_content()

    def upload_files(self,ele_loc, path):
        """
        上传文件：该方法只封装了input属性的上传文件，没有封装div属性
        :param ele_loc:
        :param path: 上传的文件绝对路径，注意转义
        :return:
        """
        try:
            self.send_keys(ele_loc, path)

        except Exception:
            self.log.error("上传文件失败：可能是文件路径不对或文件不存在")
            raise

    def pop_up_windows(self):
        """
        处理界面弹窗（有三个选择：获取文件内容、确认、取消）
        :return:
        """
        # text=self.driver.switch_to.alert.text # 获取文本
        self.driver.switch_to.alert.accept()  # 确认
        # self.driver.switch_to.alert.dismiss()  # 取消

    def exit_window(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()

    def browser_back(self):
        """
        浏览器导航栏的按钮：后退
        :return:
        """
        self.driver.back()

    def browser_forward(self):
        """
        浏览器导航栏的按钮：前进
        :return:
        """
        self.driver.forward()

    def browser_refresh(self):
        """
        浏览器导航栏的按钮：刷新
        :return:
        """
        self.driver.refresh()

    def get_browser_url(self):
        """
        获取浏览器窗口的url
        :return:
        """
        self.driver.current_url()

    def get_title(self):
        """
        获取浏览器的窗口标题
        :return:
        """
        self.driver.title()

    def get_page_source(self):
        """
        获取当前网页的源码
        :return:
        """
        self.driver.page_source()

    def screenshot(self, name):
        """
        截图（只截图当前浏览器页面，不是全屏）
        :param name:  截图的命名规范 【截屏时间_xx页面_xx操作.png】
        :return:
        """
        catalogue_name = datetime.now().strftime('%Y') # 一级目录
        file_name = datetime.now().strftime('%m-%d') # 二级目录
        dateDir = os.path.join(PTHOTOS_PATH, catalogue_name)
        if not os.path.exists(dateDir):
            os.mkdir(dateDir)
        timeDir = os.path.join(dateDir, file_name)
        if not os.path.exists(timeDir):
            os.mkdir(timeDir)
        photo_time = datetime.now().strftime('%H-%M-%S')
        path = os.path.join(timeDir, photo_time + name + '.png')
        try:
            self.driver.get_screenshot_as_file(path)
            self.log.info(f"截图成功：{photo_time + name}.png ,保存路径：{path}")
            return path
        except Exception:
            self.log.error(f"截图失败：{name} ,报错提示：{traceback.print_exc()}")
            raise

    def allure_attach(self, file_path, file_name, file_type):
        file_png = open(file_path, mode='rb').read()
        if file_type == "png":
            allure.attach(body=file_png, name=file_name,attachment_type=allure.attachment_type.PNG)
        elif file_type == "jpg":
            allure.attach(body=file_png, name=file_name, attachment_type=allure.attachment_type.JPG)
        elif file_type == "text":
            allure.attach(body=file_png, name=file_name, attachment_type=allure.attachment_type.TEXT)
        else:
            self.log.error("你输入的文件类型暂时不支持上传，需要自己去封装")


    def mouse_event(self, ele_loc, click_ele):
        """
        鼠标的悬停操作
        move_to_element(ele)方法鼠标移动到某个元素
        """
        ele = self.find_element(ele_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.click(click_ele)
    
    
    def keyboard_event(self, ele_loc)
        """
        键盘事件，一般send_keys用来模拟键盘输入
        """
        ele = self.find_element(ele_loc)
        ele.send_keys(Keys.ENTER)  #输入回车代替点击搜索按钮
        ele.send_keys(Keys.CONTROL, 'a')  #输入Control+a模拟全选
        ele.send_keys(Keys.SPACE)  #输入空格键
        

if __name__ == '__main__':
    loca=("id","case")
    a=Base.element_locator(loca)
    print(a)
