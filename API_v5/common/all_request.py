# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 16:12
@作者:   王齐涛
@文件:   all_request.py
"""
import requests


class AllRequest:

    session_huihua = requests.session()  # session会话

    def all_send_request(self, method, url, data=None, **kwargs):
        """定义请求的一个入口，方便做统计"""
        try:
            method = str(method).lower()   # 将传入的参数全部转换为小写
            res = None
            if method == "post":
                # strdata = json.dumps(data)   将格式转为字符串,这里不需要，传进来的就是字符串
                # print(method, url, data)
                res = AllRequest.session_huihua.request(method=method, url=url, data=data, allow_redirects=False, **kwargs)
            elif method == "get":
                res = AllRequest.session_huihua.request(method=method, url=url, params=data, allow_redirects=False, **kwargs)
            else:
                print("你输入的参数有误，不支持的请求方式")
            return res
        except Exception:
            raise ConnectionError("可能是服务器没有开或者网络异常")




