from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base import Base


class JobPage(Base):
    url = 'https://team.pescms.com/?g=Team&m=Login&a=index'
    # 登录按钮
    login_btu = (By.CSS_SELECTOR, ".am-btn-primary")
    # 发布新任务
    new_job = (By.LINK_TEXT, "新任务")
    # 选择任务
    select_sub = (By.NAME, "project_id")
    # 任务标题
    title = (By.NAME, "title")
    # 任务优先级
    priority = (By.NAME, "priority")
    # 任务审核人
    reviewed_person = (By.CSS_SELECTOR, ".select-check-user")
    # 部门
    department = (By.CSS_SELECTOR, ".department")
    # 开始日期
    date = (By.NAME, "start_time")
    time = (By.XPATH, "/html/body/div[4]/div[3]/table/tbody/tr[4]/td[4]")
    minute = (By.XPATH, "/html/body/div[4]/div[2]/table/tbody/tr/td/span[15]")
    # 结束日期
    end_time = (By.NAME, "end_time")
    js = "$('input[name=end_time]').removeAttr('readonly')"
    # 任务条目
    task_list = (By.NAME, "tasklist")
    # 任务说明
    explain = (By.CSS_SELECTOR, "body[class=view]")
    # 重复天数
    repeat_day = (By.CSS_SELECTOR, "div>.form-text-input[name=repeat]")
    # 阅读权限
    read = (By.NAME, "read_permission")
    # 发布任务按钮
    submit = (By.CSS_SELECTOR, ".am-radius")
    # 切换框架
    frame = (By.ID,"ueditor_0")
    # 断言发布成功的结果
    res = (By.CSS_SELECTOR,".am-btn-primary")

    def submit_job(self, title, endTime, task_list, explain, reepeat_day):
        self.open_url(self.url)
        self.click_element(self.login_btu)
        self.click_element(self.new_job)
        self.select(self.select_sub, "index", 2)
        self.send_keys(self.title, title)
        self.select(self.priority, "index", 2)
        self.select(self.reviewed_person, "index", 2)
        self.select(self.department, "index", 2)
        sleep(2)
        self.click_element(self.date)
        self.click_element(self.time)
        self.click_element(self.minute)
        self.execute_script(self.js)
        self.send_keys(self.end_time, endTime)
        sleep(1)
        self.find_element(self.end_time).send_keys(Keys.TAB)
        sleep(1)
        self.send_keys(self.task_list, task_list)
        self.switch_frame(self.frame)
        self.send_keys(self.explain, explain)
        sleep(1)
        self.switch_default_wind()
        self.send_keys(self.repeat_day, reepeat_day)
        sleep(1)
        self.find_elements(self.read)[1].click()
        sleep(2)
        self.click_element(self.submit)
        sleep(2)

    def result_newJob(self):
        return self.find_element(self.res)
