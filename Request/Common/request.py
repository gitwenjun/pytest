import requests

class Request:
    def __init__(self):
        self.session = requests.session()

    def request_hanle(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
        return self.session.request(method,url,params=params,data=data,json=json,headers=headers,**kwargs)

    def close_session(self):
        self.session.close()