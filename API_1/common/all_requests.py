import requests


class RequestHandler:
    def __init__(self):
        self.session = requests.session()

    def sent_request2(self, method=None, url=None, params=None, data=None, headers=None, json=None, **kwargs):
        return self.session.request(method=method, url=url, params=params, data=data, headers=headers, json=json,**kwargs)

    def sent_request(self, url, method, headers=None, params=None, content_type=None,**kwargs):
        '''请求工具类封装'''
        try:
            method = str(method).lower()  # 将传入的参数全部转换为小写
            if method == "get":
                result = self.session.request(method=method,url=url, params=params, headers=headers,**kwargs)
                return result
            elif method == "post":
                if headers:
                    if headers["content-type"] == "application/json":
                        result = self.session.request(method=method,url=url, json=params, headers=headers,**kwargs)
                        return result
                else:
                    result = self.session.request(method=method,url=url, data=params, headers=headers,**kwargs)
                    return result
            else:
                print('只做了post and get请求')
        except Exception as e:
            print("http请求报错：{0}".format(e))

    def close_session(self):
        self.session.close()
