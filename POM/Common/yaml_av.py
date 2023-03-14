import yaml


def read_yaml(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data

def write_yaml(filname,data):
    with open(filname,'w',encoding='utf-8') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)

def clear_yaml(filname):
    with open(filname,'w',encoding='utf-8') as f:
        f.truncate()