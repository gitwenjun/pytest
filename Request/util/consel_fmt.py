from Common.logs import logger
from Common.assert_respose import AssertRespose

class ConselFmt:


    def status_consel_fmt(self,name,method,url,data,response,exc,act):
        logger.debug(f"开始执行测试用例：{name}")
        logger.debug(f"请求方式：{method}")
        logger.debug(f"请求URL：{url}")
        logger.debug(f"请求参数：{data}")
        logger.debug(f"响应结果：{response}")
        AssertRespose().assert_stutas(exc,act)

    def message_consel_fmt(self,name,method,url,data,response,exc,act):
        logger.debug(f"开始执行测试用例：{name}")
        logger.debug(f"请求方式：{method}")
        logger.debug(f"请求URL：{url}")
        logger.debug(f"请求参数：{data}")
        logger.debug(f"响应结果：{response}")
        AssertRespose().assert_messags(exc,act)
