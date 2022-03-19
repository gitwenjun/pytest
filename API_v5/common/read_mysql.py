# -*- encoding: utf-8 -*-
"""
@时间:   2021/10/3 14:45
@作者:   王齐涛
@文件:   read_mysql.py
"""
import configparser
import pymysql


class MysqlDB:
    def __init__(self,configPath,db):
        """
        :param configPath:  配置文件路径
        :param db:   配置文件中[]
        """
        try:
            config = configparser.ConfigParser()   # 读取config或ini文件
            config.read(configPath)      # 配置文件所在的路径
            host = config[db]["host"]
            port = int(config[db]["port"])
            user = config[db]["user"]
            password = config[db]["password"]
            database = config[db]["database"]
            charset = config[db]["charset"]
            self.con = pymysql.connect(host=host, port=port, user=user, password=password, database=database,charset=charset)  # 打开
        except Exception as e:
            print("连接失败" % e)
        self.cur = self.con.cursor()   # 创建一个游标对象 cur

    def query(self,query):
        """
        适用于查询
        :param query:
        :return:
        """
        try:
            self.cur.execute(query)  # 使用 execute()  方法执行 SQL 查询
            data = self.cur.fetchall()  # 查询全部数据
            self.con.close()  # 关闭
            return data
        except Exception as e:
            print("查询失败" % e)

    def insert_query(self,insertquery):
        """
        适用于增删改
        :param insertquery:
        :return:
        """
        try:
            self.cur.execute(insertquery)  # 使用 execute()  方法执行 SQL 查询
            self.cur.execute('commit')  # 提交数据 只有增删改的时候用
            self.con.close()  # 关闭
            return True
        except Exception as e:
            print("查询失败" % e)


if __name__ == '__main__':
    aa = (MysqlDB("../config/mysql_data.ini","DEV_MYSQL").query("select * from ecs_goods where goods_id; "))
    for i in aa:
        print(i)




"""
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象

"""
