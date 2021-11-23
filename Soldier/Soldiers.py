# 需求：士兵，开枪


# 枪类
class Gun:
    def __init__(self, type):
        self.type = type
        self.count = 0

    def add_buillt(self, count):
        self.count += count

    def shoot(self):
        if self.count <= 0:
            print('开玩笑呢，没有子弹了，请先装填子弹！')
            return
        self.count -= 1
        print('biubiubiu.......')
        print('剩余子弹：%d' % self.count)


ak47 = Gun('ak47')


# ak47.add_buillt(20)
# ak47.shoot()


# 士兵类
class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def add(self,count):
        if self.gun is None:
            print('士兵 %s 还没有枪，请先分配枪' % self.name)
            return
        self.gun.add_buillt(count)

    def fire(self):
        if self.gun is None:
            print('士兵 %s 还没有枪，请先分配枪' % self.name)
            return
        self.gun.shoot()


xusanduo = Soldier('许三多',ak47)
xusanduo.add(2)
xusanduo.fire()

