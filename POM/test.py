import requests
import json
def a():
   serach = {'wd': "测试"}
   headers = {'user-agent': 'my-app/0.0.1'}
   res = requests.get('http://www.baidu.com',headers=headers,params=serach,verify=False)
   print(res.status_code)
   print(res.headers.get('user-agent'))
   print(json.dumps(res.json()))

if __name__=='__main__':
    a()