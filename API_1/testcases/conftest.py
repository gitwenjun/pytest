import pytest
from common.log_handler import logger
from common.yaml_handler import YamlHandler


@pytest.fixture(scope="session",autouse=True)
def clean_session():
    logger.info("------开始执行测试用例------")
    YamlHandler().clean_yaml("./data/session.yaml")
    yield
    logger.info("------测试用例执行结束------")