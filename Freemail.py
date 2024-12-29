
import time
import datetime

from Base import BaseEmail

from selenium.webdriver.common.by import By

class Freemail(BaseEmail):
    def __init__(self):
        self.url = "https://www.freemail.hu"

    def login(self, userName, password):
        pass

    def _clickTovabb(self):
        self._click(By.XPATH, '//button[contains(span, "Tovább")]')

        time.sleep(3)


    def register(self, emailBody, lastName, firstName, password, secureAnswer, birthDay: datetime.datetime):
        fail = True
        counter = 0
        while fail:
            try:
                self.openPage()
        
                self._registerSequence(emailBody, lastName, firstName, password, secureAnswer, birthDay)
                fail = False
            except:
                counter += 1
                if counter>10:
                    raise IndexError
            finally:
                self.closePage()

    
    def _registerSequence(self, emailBody, lastName, firstName, password, secureAnswer, birthDay: datetime.datetime):

        self._click(By.XPATH, '//button[contains(span, "ELFOGADOM")]')

        self._click(By.XPATH, '//a[contains(@href, "register")]')

        time.sleep(5)

        self._write(By.ID,'email', emailBody )
        
        self._write(By.ID,'lastName', lastName)
        
        self._write(By.ID,'firstName', firstName)

        self._clickTovabb()

        self._write(By.ID,'password', password )
        
        self._write(By.ID,'passwordConfirm', password)

        self._clickTovabb()

        self._write(By.ID,'securityAnswer', secureAnswer )
        
        self._clickTovabb()

        self._write(By.ID,'birthday', birthDay.year )

        self._write(By.NAME,'day', birthDay.day )

        self._click(By.XPATH, '//button[contains(span, "Január")]')

        #TODO implement month selector
        
        self._clickTovabb()

        self._click(By.XPATH, '//button[contains(span, "Regisztrálok")]')