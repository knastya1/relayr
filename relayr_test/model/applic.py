##Created by Kuznetsova Anastasia 11.02.17


from pages.internal_page import InternalPage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.init_page import InitPage
import logging




##### This class contains the main info about application, main action with pages###

class Application(object):

    #   Initialization of Application
    #   driver - WebDriver
    # wait - WebDriverWait in seconds
    # base_url - tested web application main url
    # init_page - any not logged in page of tested web application
    # login_page - login page of web apllication
    # internal_page - any logged in page of web application
    # logout_page - logout page of web application
    def __init__(self, driver, wait,base_url):
        self.driver = driver
        self.wait = wait
        self.base_url = base_url
        self.init_page = InitPage(driver, base_url)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage (driver, base_url)
        self.logout_page = LogoutPage (driver, base_url)




#--------- Go to URL -----------------------

    #   open application homepage
    def go_to_home_page(self):
        logging.info('go_to_home_page Base URL: '+self.base_url)
        self.driver.get(self.base_url)



#----------- Login and Logout -------------------

    #   open application login page
    def open_login_page(self):
        logging.info('open_login_page')
        self.init_page.login_link.click()

    #   Login with given users credentials
    #   user - contains all user credentials
    def do_login(self, user):
        logging.info('do_login')
        login_page = self.login_page
        login_page.username_field.clear()
        login_page.username_field.send_keys(user.email)
        login_page.password_field.clear()
        login_page.password_field.send_keys(user.password)
        login_page.submit_button.click()

    #   Check if logged in
    def is_logged_in(self):
        logging.info('is_logged_in')
        return self.internal_page.is_this_page

    #   Check if logged in with user given
    #   user - contains all user credentials
    def user_is_loggedin(self, user):
        logging.info('user_is_loggedin USER:'+user.get_cred_str())
        return(self.is_logged_in() and  (self.internal_page.user_name==user.username))


#    Logout
    def do_logout(self):
        logging.info('do_logout')
        intern_page = self.internal_page
        logout_page = self.logout_page
        intern_page.applic_menu.click()
        intern_page.logout_link.click()
        assert logout_page.is_this_page
        logout_page.logout_button.click()
        assert self.init_page.is_this_page


    #   Check if no user is logged in
    def is_not_logged_in(self):
        logging.info('login_page_opened')
        return self.init_page.is_this_page

    #   Check that logging in failed and appropriate error message is shown
    def login_failed(self):
        logging.info('login_page_opened')
        return (self.is_not_logged_in and self.login_page.error_cred_label.is_displayed())


    #   Check login page is visible
    def login_page_opened(self):
        logging.info('login_page_opened')
        return self.login_page.is_this_page




