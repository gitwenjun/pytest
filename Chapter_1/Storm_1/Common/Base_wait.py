from selenium.webdriver.support.ui import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver = driver

    def spiit_locator(self,locator):
        by = locator.split(',')[0]
        value = locator.split(',')[1]

        # locator_dict = {'id':'id','name':'name','class':'class','tag':'tag','link':'link','plink':'partial link text','css':'css selector'}
        #
        # if by not in locator_dict.keys():
        #     raise NameError('LocatorErr')
        # return locator_dict[by],value
        return by,value
    def get_element(self,locator,sec=20):
        by,value = self.spiit_locator(locator)
        try:
            element = WebDriverWait(self.driver,sec,1).until(lambda x:x.find_element(by=by,value=value))
            return element
        except Exception as e:
            raise e

    def get_elements(self,locator,sec=20):
        by,value = self.spiit_locator(locator)
        try:
            element = WebDriverWait(self.driver,sec,1).until(lambda x:x.find_elements(by=by,value=value))
            return element
        except Exception as e:
            raise e