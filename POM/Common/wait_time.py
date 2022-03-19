from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_element(driver, by_, elment_):
    element = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((by_, elment_)))
    return element


def wait_elements(driver, by_, elemnt_):
    elements = WebDriverWait(driver, timeout=10).until(EC.presence_of_all_elements_located((by_, elemnt_)))
    return elements
