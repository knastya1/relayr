##Created by Kuznetsova Anastasia 11.02.17

# -*- coding: utf-8 -*-


from conftest import app
from model.user import User
import model.user as u
import time
import logging
import resources.MyConfig as config



#Logger initialization
logging.basicConfig(format = u'%(filename) -20s %(levelname) -8s [%(asctime)s] %(message)s', level = logging.INFO, filename =config.LOG_FILENAME )

#------- Functions used in test -------------------

#       Login to with valid credentials
def do_login_valid_cred(app):
        user= User.new_user(u.CRED_TYPE_CORRECT)
        logging.info('Get user with credentials:'+user.get_cred_str())
        app.go_to_home_page()
        assert app.is_not_logged_in()
        app.open_login_page()
        assert app.login_page_opened()
        app.do_login(user)
        assert app.user_is_loggedin(user)


#       Login with invalid credentials
#       cred_type - contains expected credential type constant
def do_login_invalid_cred(app, cred_type):
        user = User.new_user(cred_type)
        logging.info('Get user with credentials:' + user.get_cred_str())
        app.go_to_home_page()
        assert app.is_not_logged_in()
        app.open_login_page()
        assert app.login_page_opened()
        app.do_login(user)
        assert app.login_failed()

#       Logout
def do_logout(app):
        app.do_logout()
        assert app.is_not_logged_in()


#============= TESTS ===============================

#       Login from the very beginning with correct credentials
#       It is checked that exact user is logged in
def test_login_correct( app ):
        logging.info('==============================')
        logging.info('START test_login_correct')
        do_login_valid_cred(app)
        do_logout(app)
        # This time delay is required to avoid anti-robot capture on site when few request are done too frequently
        time.sleep(5)

#       Login from the very beginning with valid login(email) and invalid password
def test_login_invalid_passw( app ):
        logging.info('==============================')
        logging.info('START test_login_invalid_passw')
        do_login_invalid_cred(app, u.CRED_TYPE_INVALID_PASS)
        #This time delay is required to avoid anti-robot capture on site when few request are done too frequently
        time.sleep(5)

#       Login from the very beginning with invalid login(email) and valid password
def test_login_invalid_login( app ):
        logging.info('==============================')
        logging.info('START test_login_invalid_login')
        do_login_invalid_cred(app, u.CRED_TYPE_INVALID_LOGIN)
        # This time delay is required to avoid anti-robot capture on site when few request are done too frequently
        time.sleep(5)







