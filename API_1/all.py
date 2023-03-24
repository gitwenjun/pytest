import os
from time import sleep

import pytest

if __name__ == '__main__':
    pytest.main()
    sleep(2)
    os.system("allure generate ./report/temp -o ./report/reports --clean")