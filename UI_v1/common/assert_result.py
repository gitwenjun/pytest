import json

from common.log_handler import logger


class AssertResults:

    def assert_messges(self, exp_result, act_result):
        try:
            assert exp_result in act_result
            return logger.info(f"【预期结果】:{exp_result} \n【实际结果】:{act_result}"),\
                   logger.info("【测试结果：断言成功】")
        except:
            logger.error(f"【预期结果】:{exp_result} \n【实际结果】:{act_result}"),\
            logger.error("【测试结果：断言失败】")