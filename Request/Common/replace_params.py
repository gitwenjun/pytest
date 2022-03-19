from string import Template
import yaml


class Relace:

    # 直接替换传过来的字典
    def replace_dict(self, arg, data):
        data = Template(str(arg)).substitute(data)
        return yaml.safe_load(data)

    # 先读取文件再替换
    def relace_file(self, filename,data):
            with open(filename, 'r', encoding='utf-8') as f:
                r = yaml.load(stream=f, Loader=yaml.FullLoader)
                tem = Template(str(r))
                return tem.safe_substitute(data)



# if __name__ == '__main__':
#     r = Relace()
#     ext_info = {"location": "成都"}
#     arg = r.relace_file("G:\Project\Request\Data\change_info.yaml",ext_info)
#     logger.debug(arg)
