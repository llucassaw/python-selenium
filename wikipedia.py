#coding=utf-8

from pyvirtualdisplay import Display
import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import xmlrunner

display = Display(visible=0, size=(1024, 768))
display.start()


class WikipediaTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.wikipedia.org/"

    
    def test_wikipedia_test_case(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")
        driver.find_element_by_id("searchInput").click()
        driver.find_element_by_id("searchInput").clear()
        driver.find_element_by_id("searchInput").send_keys("earth")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='en'])[1]/following::em[1]").click()
        driver.find_element_by_link_text("The Blue Marble")
   
#Throw an exception when "The Blue Marble" link text is not found.
        self.assertIsNotNone(driver.find_element_by_link_text, "The Blue Marble")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #unittest.main()
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/var/lib/jenkins/workspace/wikipedia'), failfast=False, buffer=False, catchbreak=False)
