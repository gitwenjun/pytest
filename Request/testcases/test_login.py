import pytest
from Common.request import Request
from Common.yaml_req import YamlParams
from Common.logs import logger
import allure
from util.consel_fmt import ConselFmt


@allure.epic("登录接口总体描述")
@allure.feature('登录接口测试')
class TestLogin:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @allure.story('登录用例')
    @allure.description('用例描述')
    @allure.title('登录用例title==》》')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('http://www.baidu.com',name="点击跳转测试用例=>")
    @allure.step('步骤一')
    @pytest.mark.L1
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize('arg',YamlParams().yaml_read("G:\Project\Request\Data\yaml_re.yaml"))
    def test_login_01(self, arg):
        try:
            name = arg['name']
            method = arg['request']['method']
            url = arg['request']['url']
            data = arg['request']['data']
            exc = arg['assert'][0]['eq']['err_code'] #预期响应码
            res = Request().request_hanle(method=method,url=url,json=data).json()
            act = res['data']['err_code'] #实际响应码
            if exc == act:
                token = res["data"]["token"]
                uuid = res["data"]["uuid"]
                YamlParams().yaml_wirte("G:\Project\Request\Data\session.yaml",{"session":{"token": f'{token}',"uuid": f'{uuid}'}})
            ConselFmt().status_consel_fmt(name=name,method=method,url=url,data=data,response=res,exc=exc,act=act)
        except Exception as e:
            raise e




if __name__ == '__main__':
    pytest.main(['-v','q','--reruns','1','--reruns-delay','2','-n','auto'])
