import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigate to google.com')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://google.com")
    context.driver.implicitly_wait(2)


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is "+title)
    assert "Googles" in title


@then('I enter the text as "{searchText}"')
def step_impl(context, searchText):
    context.driver.find_element(By.NAME, 'q').send_keys(searchText)
    time.sleep(2)
    # pass



@then(u'I click the search button')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
    # time.sleep(2)
    pass


