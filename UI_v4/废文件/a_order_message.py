# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/28 20:31
@作者 ： 王齐涛
@文件名称： a_order_message.py
'''
from page.Base import Base


class OrderMessagePage(Base):
    """
    封装定位元素
    """
    url = Base.url + "/flow.php?step=checkout"
    submit_order_control = ("xpath", "//input[@src='themes/ecmoban_meilishuo/images/bnt_subOrder.gif']")  # ”提交订单“按钮

    """
    封装页面操作
    """
    def order_message(self, peisong, payment):
        """
        选择配送方式和支付方式是在选项中有的，如果没有就去后台进行配置
        :param peisong: 输入配送方式
        :param payment: 输入支付方式
        :return:
        """
        try:
            self.open_url()
            self.click(("xpath", f"//strong[text()='{peisong}']//..//..//input[@name='shipping']"))
            self.click(("xpath", f"//font[text()='{payment}']//..//..//..//input[@name='payment']"))
            self.click(self.submit_order_control)
        except Exception:
            self.log.error("支付方式和付款方式可能有问题，请检查支持的方式和对应的字段")
            raise


