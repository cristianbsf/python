from selenium import webdriver

import unittest

from page_object.login_po import LoginPO



def setUp(self0):
    self.driver = webdriver.Chrome()
    self.driver.get()
