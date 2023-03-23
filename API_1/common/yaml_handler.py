import os

import yaml

from common.all_path import Data_Path


class YamlHandler:

    def read_yaml(self, fileName):
        with open(Data_Path+os.sep+fileName,"r",encoding="utf-8") as f:
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            return data

    def write_yaml(self, fileName, data):
        with open(Data_Path+os.sep+fileName,"a",encoding="utf-8") as f:
            data = yaml.dump(data=data,stream=f,allow_unicode=True)
            return data

    def clean_yaml(self, fileName):
        with open(Data_Path+os.sep+fileName,"w",encoding="utf-8") as f:
            f.truncate()

    def read_extrct_yaml(self,key):
        fileName = Data_Path+os.sep+"read_extract.yaml"
        with open(fileName,"r",encoding="utf-8") as f:
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            return data[key]

    def write_extract_yaml(self,data):
        fileName = Data_Path+os.sep+"read_extract.yaml"
        with open(fileName,"a",encoding="utf-8") as f:
            data = yaml.dump(data=data,stream=f,allow_unicode=True)
            return data
