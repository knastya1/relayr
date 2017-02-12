##Created by Kuznetsova Anastasia 11.02.17

import pytest
from selenium import webdriver
from model.applic import Application
from selenium.webdriver.support.wait import WebDriverWait
import resources.MyConfig as config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")
    parser.addoption("--base_url", action="store", default=config.BASE_URL, help="base URL")




@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="session")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
       driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 30)
    request.addfinalizer(driver.quit)
    return Application(driver,wait, base_url)

