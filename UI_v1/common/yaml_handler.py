import yaml


class YamlHandler:

    def read_yaml(self,fileName):
        with open(fileName,"r",encoding="utf-8") as f:
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            return data

    def write_yaml(self,fileName,data):
        with open(fileName,"a",encoding="utf-8") as f:
            data = yaml.dump(data=data,stream=f,allow_unicode=True)
            return data

    def clean_yaml(self,fileName):
        with open(fileName,"w",encoding="utf-8") as f:
            f.truncate()
