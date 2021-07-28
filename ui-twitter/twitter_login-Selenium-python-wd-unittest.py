# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TwitterLogin:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
    def test_twitter_login(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1739,828 | ]]
        driver.get("https://twitter.com/")
        driver.find_element_by_css_selector("div.css-901oao.r-1awozwy.r-13gxpu9.r-6koalj.r-18u37iz.r-16y2uox.r-1qd0xha.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0").click()
        #driver.find_element_by_name("session[username_or_email]").clear()
        time.sleep(5)
        driver.find_element_by_name("session[username_or_email]").send_keys("Samrat_Ghosh_")
        #driver.find_element_by_name("session[password]").clear() 
        driver.find_element_by_name("session[password]").send_keys("Samrat321")
        time.sleep(3)
        driver.find_element_by_css_selector("div.css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-1qd0xha.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.css-901oao.css-bfa6kz.r-1awozwy.r-1fmj7o5.r-6koalj.r-1qd0xha.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0 > span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0 > span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-1xcajam.r-zchlnj.r-ipm5af").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.css-1dbjc4n.r-1twgtwe.r-sdzlij.r-rs99b7.r-1p0dtai.r-1mi75qu.r-1d2f490.r-1ny4l3l.r-u8s1d.r-zchlnj.r-ipm5af").click()
        time.sleep(3)
        driver.find_element_by_css_selector("span.css-901oao.css-16my406.css-bfa6kz.r-1fmj7o5.r-18u37iz.r-poiln3.r-bcqeeo.r-qvutc0 > span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-1qd0xha.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0").click()

    
    def tearDown(self):
        self.driver.quit()


t = TwitterLogin()
t.setup()
t.test_twitter_login()
t.tearDown()