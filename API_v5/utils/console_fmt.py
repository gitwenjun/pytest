# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/11 23:03
@作者 ： 王齐涛
@文件名称： console_fmt.py
'''
import pytest
from common.logger_handler import GetLogger
from common.response_assert import ResponseAssert

"""
【开始执行测试用例：登录】
请求url：
请求参数：
返回结果：
断言检查点1：预期结果，实际结果
断言检查点2：预期结果，实际结
【测试结果：通过、失败】
"""


class ConsoleFmt:

    def all_console_fmt(self, name_case, url, method, data, response, exc, act):
        log = GetLogger()
        log.debug(f"【开始执行测试用例：{name_case}】")
        log.debug(f"请求url：{url}")
        log.debug(f"请求方法：{method}")
        log.debug(f"请求参数：{data}")
        log.debug(f"响应结果：{response}")
        ResponseAssert().assert_message(exc, act)


if __name__ == '__main__':
    pytest.main(["-sv","console_fmt.py"])