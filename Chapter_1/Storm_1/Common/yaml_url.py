import yaml

def yaml_params(file,secont,param):
    with open(file,'r',encoding='utf8') as f:
        url = yaml.load(f, Loader=yaml.FullLoader)
        return url[secont][param]
if __name__ == '__main__':
    date = yaml_params('../Config/yaml_url','websits','url')
    print(date)
