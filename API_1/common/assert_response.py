import json

from common.logs_handler import logger


class AssertResponse:

    def assert_equals(self,name,method,url,parmase,response,response_exp,response_act):
        logger.info(f"测试用例名：{name}")
        logger.info(f"请求方法：{method}")
        logger.info(f"请求URL：{url}")
        logger.info(f"请求参数：{parmase}")
        logger.info(f"响应结果：{response}")
        try:
            assert response_exp == response_act
            return logger.info(f"预期结果：{response_exp}"), \
                   logger.info(f"实际结果：{response_act}"), \
                   logger.info(f"测试结果：成功")
        except:
            logger.error(f"预期结果：{response_exp}"), \
            logger.error(f"实际结果：{response_act}"), \
            logger.error(f"测试结果：失败")

    # def assert_contains(self,name,method,url,parmase,response,response_exp,response_act):
    #     logger.info(f"测试用例名：{name}")
    #     logger.info(f"测试方法：{method}")
    #     logger.info(f"测试URL：{url}")
    #     logger.info(f"测试参数：{parmase}")
    #     logger.info(f"响应结果：{response}")
    #     response_exp = str(response_exp)
    #     response_act = str(response_act)
    #     try:
    #         assert response_exp in response_act
    #         return logger.info(f"预期结果：{response_exp}"),\
    #                logger.info(f"实际结果：{response_act}"),\
    #         logger.info(f"测试结果：成功")
    #     except:
    #         logger.error(f"预期结果：{response_exp}"), \
    #         logger.error(f"实际结果：{response_act}"), \
    #         logger.error(f"测试结果：失败")

    def assert_contains(self,name,method,url,parmase,response,response_exp,response_act):
        logger.info(f"测试用例名：{name}")
        logger.info(f"测试方法：{method}")
        logger.info(f"测试URL：{url}")
        logger.info(f"测试参数：{parmase}")
        logger.info(f"响应结果：{response}")
        response_exp = str(response_exp)
        response_act = str(response_act)
        try:
            assert response_exp in response_act
            return logger.info(f"预期结果：{response_exp}"),\
                   logger.info(f"实际结果：{response_act}"),\
            logger.info(f"测试结果：成功")
        except:
            logger.error(f"预期结果：{response_exp}"), \
            logger.error(f"实际结果：{response_act}"), \
            logger.error(f"测试结果：失败")
            return False
