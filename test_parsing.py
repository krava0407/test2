import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_google():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://google.com/')

        #assert 'google' in driver.page_source

    # def test_0(self):
    #     driver = self.driver
    #     driver.find_element_by_xpath("//button[@id='L2AGLb']").click()
    #     time.sleep(1)
    #     input_field = driver.find_element_by_xpath("//input[@title='Поиск']")
    #     time.sleep(2)
    #
    #     input_field.send_keys('python')
    #     input_field.send_keys(Keys.ENTER)
    #     time.sleep(2)
    #     titles = driver.find_elements_by_class_name('LC20lb MBeuO DKV0Md')
    #     for title in titles:
    #         assert 'python' in title.text.lower()

    def test_01(self):
        driver = self.driver
        driver.find_element_by_xpath("//button[@id='L2AGLb']").click()
        time.sleep(1)
        input_field = driver.find_element_by_xpath("//input[@title='Поиск']")
        time.sleep(2)

        input_field.send_keys('python')
        time.sleep(1)
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.DOWN)
        time.sleep(2)
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)
        titles = driver.find_elements_by_class_name('LC20lb MBeuO DKV0Md')
        for title in titles:
            assert 'python' in title.text.lower()

    def teardown(self):
        self.driver.quit()

