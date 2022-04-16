# def print_text1():
#     print('Func 1.')
# def print_text2():
#     print('Func 2.')
#
# def simple_decorator(fn):
#     def wrapper():
#         print('Run func.')
#         fn()
#         print('Stop func.')
#     return wrapper
#
# first_test_wrapper = simple_decorator(print_text1)
# second_test_wrapper = simple_decorator(print_text2)
#
# first_test_wrapper()
# second_test_wrapper()
#
# """
# @
# """
# def simple_decorator(fn):
#     def wrapper():
#         print('Run func: ' + fn.__name__)
#         fn()
#         print('Stop func.')
#     return wrapper
#
# @simple_decorator
# def print_text():
#     print('Test func 1')
#
# print_text()
#
#
# my_dict = {'a': 1, 'c': 3, 'e': 5, 'f': 6, 'b': 2, 'd': 4}
# mysorted = sorted(my_dict)
# print(mysorted)           # ['a', 'b', 'c', 'd', 'e', 'f']
# mysorted = sorted(my_dict.items())
# print(mysorted)           # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
# mysorted = sorted(my_dict.values())
# print(mysorted)           # [1, 2, 3, 4, 5, 6]
#
#
# """Объединение словарей"""
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dic3 = {**dict1, **dict2}


import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://leafground.com/')

def test_smoke():
    req = requests.get('http://leafground.com/')
    assert req.status_code == 200

def page_edit():
    search_button = driver.find_element_by_xpath("//a[@href='pages/Edit.html']")
    search_button.click()
    assert "TestLeaf - Interact with Edit Fields" == driver.title

page_edit()

search_field_email = driver.find_element_by_xpath("//input[@id='email']")
search_field_email.click()
search_field_email.send_keys("asd@gmail.com")
time.sleep(1)
search_field_email.send_keys(Keys.TAB)
time.sleep(1)
search_field_append = driver.find_element_by_xpath("//input[@value='Append ']")
search_field_append.click()

search_field_append.send_keys("new text")
search_field_append.send_keys(Keys.TAB)
time.sleep(1)
search_field_text = driver.find_element_by_xpath("//input[@value='TestLeaf']").get_attribute("value")
assert "TestLeaf" == search_field_text
search_field_clear = driver.find_element_by_xpath("//input[@value='Clear me!!']").clear()
time.sleep(5)
search_field_disable = driver.find_element_by_xpath("//input[@disabled='true']").get_attribute('disabled')
assert 'true' == search_field_disable

driver.quit()

