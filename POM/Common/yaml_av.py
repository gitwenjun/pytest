import yaml

def load_yaml(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data