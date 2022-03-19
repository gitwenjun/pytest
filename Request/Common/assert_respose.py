from Common.logs import logger

class AssertRespose:

    def assert_stutas(self,exc,act):
        try:
            assert exc == act
            return logger.debug(f"断言检查点：预期结果 {exc},实际结果 {act}"),\
                   logger.debug("【断言结果：成功】")
        except:
            return logger.debug(f"断言检查点：预期结果 {exc},实际结果 {act}"),\
                   logger.debug("【断言结果：失败】")

    def assert_messags(self,exc,act):
        try:
            assert exc in act
            return logger.debug(f"断言检查点：预期结果 {exc},实际结果 {act}"),\
                   logger.debug("【断言结果：成功】")
        except:
            return logger.debug(f"断言检查点：预期结果 {exc},实际结果 {act}"),\
                   logger.debug("【断言结果：失败】")
