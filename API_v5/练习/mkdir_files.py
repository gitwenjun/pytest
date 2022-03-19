# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/8 10:32
@作者 ： 王齐涛
@文件名称： mkdir_files.py 
'''
import time
from faker import Faker

fake =  Faker(locale="zh_CN")

test = fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)

# 执行了第134006次10G就满了
def test01():
    for i in range(1,2000000000000):
        filename = str(time.time())
        with open(f"M:\\"+filename + ".txt","w") as f:
            for j in range(1,25):
                f.write(f"{test,test,test}")
        print(f"执行了第{i}次")




if __name__ == '__main__':
    test01()