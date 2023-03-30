import pytest
from common.log_handler import logger
from common.yaml_handler import YamlHandler


@pytest.fixture(scope="session",autouse=True)
def clean_session():
    logger.warning("------开始执行测试用例------")
    YamlHandler().clean_yaml("read_extract.yaml")
    yield
    logger.warning("------测试用例执行结束------")