##Created by Kuznetsova Anastasia 11.02.17

from page_page import Page


#   This is homepage of application
#   Implements any web application page
#   Contains Main menu link
class AnyPage(Page):

    #   Main application menu
    @property
    def applic_menu(self):
        return self.driver.find_element_by_xpath("//a[contains(@title,'Stack Exchange sites')]")



