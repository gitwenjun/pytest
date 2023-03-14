from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_element(driver,by_,loc_):
     return WebDriverWait(driver=driver,timeout=20).until(EC.presence_of_element_located((by_,loc_)))


def wait_elements(driver, by_, loc_):
    return WebDriverWait(driver=driver, timeout=20).until(EC.presence_of_all_elements_located((by_, loc_)))