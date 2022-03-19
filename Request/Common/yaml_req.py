import yaml

class YamlParams:
    def yaml_read(self,filename):
        try:
            with open(filename,'r',encoding='utf-8') as f:
                data = yaml.load(stream=f,Loader=yaml.FullLoader)
            return data
        except Exception as e:
            print(e)

    def yaml_wirte(self,filname,data):
        try:
            with open(filname,'w',encoding='utf-8') as f:
                yaml.dump(data=data,stream=f,allow_unicode=True)
        except Exception as e:
            print(e)

    def yaml_clean(self,filname):
        try:
            with open(filname,'w') as f:
                f.truncate()
        except Exception as e:
            print(e)

# if __name__ == '__main__':
#     a = YamlParams()
    # a.yaml_wirte("../Data/session.yaml", {"qb": {"host": "123456", "port": "3306"}})
    # a.yaml_clean("../Data/session.yaml")
    # r = a.yaml_read('G:\Project\Request\Data\info_vip.yaml')
    # print(r)