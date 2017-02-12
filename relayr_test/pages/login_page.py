##Created by Kuznetsova Anastasia 11.02.17

from init_page import InitPage

#   This is Login page
#   Contains Login, passwor fields, LogIn button
class LoginPage(InitPage):


#   Login field
    @property
    def username_field(self):
        return self.driver.find_element_by_id("email")

#   Password field
    @property
    def password_field(self):
        return self.driver.find_element_by_id("password")

#   LogIn button
    @property
    def submit_button(self):
        return self.driver.find_element_by_id("submit-button")

#   Error login message
    @property
    def error_cred_label(self):
        return self.driver.find_element_by_xpath("//div[.='The email or password is incorrect.']")


#   Login button is present
    @property
    def is_this_page(self):
        return self.submit_button.is_displayed()


