import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class AbstractEmail:
    def __init__(self):
        self.url = None
        raise NotImplementedError

    def login(self, userName, password):
        raise NotImplementedError
    
    def register(self, userName, password):
        raise NotImplementedError
    
    def sendEmail(self, userName, password, sendTo, content):
        raise NotImplementedError
    
    def getInbox(self, userName, password):
        raise NotImplementedError
    

    
class BaseEmail(AbstractEmail):
    def _click(self, by, value):
        element = self.driver.find_element(by = by, value = value)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()
        time.sleep(1)

    def openPage(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.maximize_window()

    def closePage(self):
        self.driver.quit()

    def _write(self, by, value, text):
        element = self.driver.find_element(by = by, value = value)
        element.send_keys(text)
    

