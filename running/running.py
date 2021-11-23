# 小明跑步案例
# 需求：跑一次瘦了0.5公斤，吃一次胖1公斤
class Person:
    def __init__(self,name,weight):
        """初始化属性"""
        self.name = name
        self.weight =weight


    def __str__(self):
        return '姓名：%s  体重：%.2f公斤' % (self.name,self.weight)

    def __del__(self):
        print ('程序执行完成，调用del方法')


    def run(self):
        """跑方法"""
        self.weight -= 0.5


    def eat(self):
        """吃方法"""
        self.weight += 1


xiao_ming = Person('小明',75)
print(xiao_ming)

print('-' * 30)
xiao_ming.run()
print(xiao_ming)

print('-' * 30)
xiao_ming.eat()
print(xiao_ming)