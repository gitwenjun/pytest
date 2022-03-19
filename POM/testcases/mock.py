class Product(object):

    def __init__(self):
        pass

    def get_product_status_by_id(self, product_id):
        """
        通过商品id获取产品信息（Mock）
        :return:
        """
        # 待实现查询数据库的业务逻辑
        pass

    def buy_product(self, product_id):
        """
        购买产品（真实逻辑）
        :return:
        """
        # 产品信息
        # {"id":1,"name":"苹果","num":23}
        product = self.get_product_status_by_id(product_id)

        if product.get("num") >= 1:
            result = {"status": 0, "msg": "购买成功！"}
        else:
            result = {"status": 1, "msg": "购买失败，库存不足！"}

        return result