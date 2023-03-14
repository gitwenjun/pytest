# -*-coding:GBK -*-
import allure
import pytest
from time import sleep
from Common.logs import logger
from Common.replace_params import Relace
from Common.yaml_req import YamlParams
from testcases.test_login import TestLogin
from util.request_result import ResuiltParams


@allure.epic("��Ա�ӿ���������")
@allure.feature('��Ա�ӿڲ�������')
class TestInfoVip:
    def setup_class(self):
        logger.info("ִ�е�¼����ȡsession")
        TestLogin().test_login_01
        sleep(2)

    def teardown_class(self):
        YamlParams().yaml_clean("G:\Project\Request\Data\session.yaml")
        logger.info("����ִ����ɣ����session")

    @allure.story('��ȡ��Ա��Ϣ�ӿ�')
    @allure.description('��ȡ��������')
    @allure.title('��ȡ��Ա����title==��')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('http://www.baidu.com',name="�����ת��������=>")
    @allure.step('����һ')
    @pytest.mark.L1
    @pytest.mark.run(order=2)
    # @pytest.mark.skip(reason="��������")
    @pytest.mark.parametrize('arg',YamlParams().yaml_read("G:\Project\Request\Data\info_vip.yaml"))
    def test_info_01(self, arg):
        ResuiltParams().resuilt_ast_mgs(arg)

    @allure.story('�޸Ļ�Ա��Ϣ�ӿ�')
    @allure.description('�޸���������')
    @allure.title('�޸Ļ�Ա����title==��')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('http://www.baidu.com', name="�����ת��������=>")
    @allure.step('����һ')
    @pytest.mark.L1
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('arg', YamlParams().yaml_read("G:\Project\Request\Data\change_info.yaml"))
    def test_change_local(self,arg):
        ext_info = {"location": "�ɶ�2"}
        arg = Relace().replace_dict(arg,ext_info) # �滻yaml�ļ��е�$����
        ResuiltParams().resuilt_ast_ststus(arg)


if __name__ == '__main__':
    pytest.main(['-v'])
    # pytest.main(['-v','q','--reruns','1','--reruns-delay','2','-n','auto'])
