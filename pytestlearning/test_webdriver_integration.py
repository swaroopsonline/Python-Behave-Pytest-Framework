import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


def get_data():
    return [
        ("Harry@gmail.com", "asfdsaf"),
        ("Hermione@gmail.com", "wrtewt"),
        ("Ron@gmail.com", "zcvzvv")
    ]


def setup_function():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://facebook.com")
    # driver.maximize_window()
    time.sleep(2)

def teardown_function():
    driver.quit()

#
# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     driver.get("https://facebook.com")
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
    driver.find_element(By.ID("email")).send_keys(username)
    driver.find_element(By.ID("pass")).send_keys(password)