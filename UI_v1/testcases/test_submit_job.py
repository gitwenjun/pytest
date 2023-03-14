import allure
import pytest
from selenium import webdriver

from common.assert_result import AssertResults
from common.log_handler import logger
from common.screenshot import Screenshot
from common.yaml_handler import YamlHandler
from page.new_job_page import JobPage


@allure.epic("团队管理系统")
class TestSubmitJob:

    def setup_class(self):
        logger.info(f"------开始执行测试用例------")
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        logger.info(f"------测试用例执行结束------")
        self.driver.quit()

    @allure.title("发布新任务")
    @allure.testcase("www.baidu.com", name="测试用例链接")
    @allure.issue("www.jd.com", name="缺陷链接地址")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.L1
    @pytest.mark.parametrize("arg", YamlHandler().read_yaml('./data/submit_job.yaml'))
    def test_submit(self, arg):

        JobPage(self.driver).submit_job(**arg)
        res = JobPage(self.driver).result_newJob().text
        AssertResults().assert_messges("开始匹配任务", res)
        Screenshot.photo_screenshoot(self.driver, "发布新任务")
