##Created by Kuznetsova Anastasia 11.02.17

from any_page import AnyPage
from selenium.webdriver.common.by import By

#   This is homepage of application in not logged in state
class InitPage(AnyPage):

    #   LogIn link
    @property
    def login_link(self):
        return self.driver.find_element_by_link_text("log in")

    #   SignUp link
    @property
    def signup_link(self):
        return self.driver.find_element_by_link_text("sign up")

    #   Are LogIn and SignUp links are present
    @property
    def is_this_page(self):
        return self.login_link.is_displayed()


