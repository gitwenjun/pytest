from Common.logs import logger
import pytest
from Common.yaml_req import YamlParams

@pytest.fixture(scope="session",autouse=False)
def clean_session():
    logger.info(f"清除上次保存的session")
    YamlParams().yaml_clean("G:\Project\Request\Data\session.yaml")
    yield
    print('咳咳')