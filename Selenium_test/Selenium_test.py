from filecmp import cmp
from time import sleep
from io import BytesIO
from PIL import Image
import requests
from selenium import webdriver
import os


class Pictrue():

    def __init__(self):
        # self.headers = '{\'User-Agent\': \'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36\'}'
        self.url = 'https://unsplash.com/'
        self.path = os.path.dirname(__file__)

    def makedir(self, name):
        path = os.path.join(self.path, name)
        isExist = os.path.lexists(path)
        if not isExist:
            os.mkdir(path)
            print('file has been create')
        else:
            print('the file is exited')
        os.chdir(path)

    def open_brow(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        sleep(3)

    def get_img(self,name):
        self.makedir(name)
        img_url = self.driver.find_elements_by_css_selector('.oCCRx')
        i=0
        for images_element in img_url:
            imge = images_element.get_attribute("src")
            imges = requests.get(imge)
            pictrue = Image.open(BytesIO(imges.content))
            pictrue.save(str(i)+'.'+pictrue.format,pictrue.format)
            i += 1

    def cs(self):
        a = [1,3,2,4]
        # a.sort()
        aa = set(a)
        b = [1,2,3,4,5,6]
        bb = set(b)
        # b.reverse()
        # c = cmp(a,b)
        print(aa&bb)

if __name__ == "__main__" :
    get_pic = Pictrue()
    get_pic.cs()





