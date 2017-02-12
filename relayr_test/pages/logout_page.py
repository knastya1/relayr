##Created by Kuznetsova Anastasia 11.02.17

from internal_page import InternalPage


#   This is Logout page
#   Contains LogOut button
class LogoutPage(InternalPage):


#   Logout button
    @property
    def logout_button(self):
        return self.driver.find_element_by_xpath("//input[@value='Log Out'][@type='submit']")


#   Is Logout button present
    @property
    def is_this_page(self):
        return self.logout_button.is_displayed()


