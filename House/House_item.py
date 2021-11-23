# 需求，房子里放家具
class House_item:
    """家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return ('家具名：%s， 占用：%.1f平米' % (self.name, self.area))


bed = House_item('席梦思', 4)
print(bed)
chest = House_item('衣柜', 6)
print(chest)
table = House_item('餐桌', 10)
print(table)
print('-' * 50)


class House:
    """房子类"""

    def __init__(self, house_type, areas):
        self.house_type = house_type  # 房子类型
        self.area = areas  # 总面积
        self.free_area = areas  # 剩余面积
        self.items_list = []  # 家具列表

    def __str__(self):
        return '房子类型是：%s，剩余面积：%.1f，家具：%s' % (self.house_type, self.free_area, self.items_list)

    def add_items(self, item):
        """放入家具的方法"""
        # 判断剩余面积是否够放入家具
        if item.area > self.free_area:
            print('对不起，没有充足的空间再放入新的家具了')
            return
        else:
            # 更新剩余面积
            self.free_area -= item.area
            # 添加家具到列表
            self.items_list.append(item.name)


big_house = House('小别墅', 60)
print(big_house)
print('-' * 30)
big_house.add_items(bed)
print(big_house)
print('-' * 30)
big_house.add_items(chest)
print(big_house)
print('-' * 30)
big_house.add_items(table)
print(big_house)