import yaml

def yaml_params(file,secont,params):
    with open(file,'r',encoding='utf8') as f:
        ps = yaml.load(f,Loader=yaml.FullLoader)
        return ps[secont][params]