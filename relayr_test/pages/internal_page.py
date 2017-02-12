##Created by Kuznetsova Anastasia 11.02.17

from any_page import AnyPage


#   This is any internal (logged in) page
#   Contains user profile avatar and link
class InternalPage(AnyPage):

    #   Users profile link
    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector(".profile-me")

    #   LogOut link
    @property
    def logout_link(self):
        return self.driver.find_element_by_link_text("log out")

    #   Get username from UI element
    @property
    def user_name(self):
        return self.driver.find_element_by_css_selector(".profile-me>*").get_attribute("title")


    #   For logged in user
    @property
    def is_this_page(self):
        return self.user_profile_link.is_displayed()




