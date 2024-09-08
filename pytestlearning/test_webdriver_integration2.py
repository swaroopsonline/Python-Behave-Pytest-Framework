import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_example(driver):
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("test@example.com")
    assert email_field.get_attribute("value") == "test@example.com"
