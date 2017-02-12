##Created by Kuznetsova Anastasia 11.02.17

import resources.MyConfig as config

## The User datas

from random import randint

# Credential type
CRED_TYPE_CORRECT=1
CRED_TYPE_INVALID_PASS=2
CRED_TYPE_INVALID_LOGIN=3

#   Modeling user, any other userinfo could be added
class User(object):

    #   Initialization of User
    #   email - user email, is used as login
    #   password - user password
    #   username - user username, is used to identify user when logged in
    def __init__(self, username="", password="", email=""):
        self.username = username
        self.password = password
        self.email = email

    # Create user with expected credential type (valid/invalid)
    # cred_type contains expected credential type constant
    @classmethod
    def new_user(cls, cred_type):
        return {
            CRED_TYPE_CORRECT: cls(username=config.CORRECT_CRED_USERNAME, email=config.CORRECT_CRED_LOGIN, password=config.CORRECT_CRED_PASSWORD),
            CRED_TYPE_INVALID_LOGIN: cls(username=config.CORRECT_CRED_USERNAME, email="n"+str(randint(0, 1000000))+"abc@front.ru", password=config.CORRECT_CRED_PASSWORD),
            CRED_TYPE_INVALID_PASS: cls(email="nastyakuz@front.ru", password="pass" + str(randint(0, 1000000)))
        }.get(cred_type)

    #   Return all user credentials as a string
    def get_cred_str(self):
        return ('username: '+self.username+', email:'+self.email+', password:'+self.password)