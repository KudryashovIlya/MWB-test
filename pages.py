# -*- coding: utf-8 -*-
from conf import BASE_URL, EMAIL, PASSWORD

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self):
        self.driver = webdriver.Chrome('./bin/chromedriver')
        self.driver.implicitly_wait(10)

    def open(self, url=BASE_URL):
        self.driver.get(url)
        return self.driver

    def close(self):
        self.driver.close()

    def get_browser_errors(self):
        error = False
        for log in self.driver.get_log('browser'):
            if log['level'] == 'ERROR':
                error = True
        return error

    def sign_in(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.XPATH,
                                          './/div[text() ="Sign In"]').click()
        self.driver.find_element(By.XPATH,
                                          './/span[text() = "Sign in with IMDb"]').click()
        self.driver.find_element(By.XPATH,
                                          './/input[@type="email"]').send_keys(EMAIL)
        self.driver.find_element(By.XPATH,
                                          './/input[@type="password"]').send_keys(PASSWORD)
        self.driver.find_element_by_id('signInSubmit').click()


class TopRatingPage(BasePage):
    """
        http://www.imdb.com/chart/top?ref_=nv_mv_250_6
    """
    def get_first_movie(self):
        return self.driver.find_element(By.XPATH, './/tbody/tr[1]')

    def get_rating_counter(self):
        return self.driver.find_element(By.XPATH, './/span[@class="seen-count"]')