from alerts import open_alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import logging
import config as cfg


class GradeChecker(object):
    @staticmethod
    def grade_is_published(website_url, user, passwd, module_name):
        """
        Login into a grade management system and verify that module grade was published or not.
        :param website_url: URL to the grade management system.
        :param user: Username for grade management system.
        :param passwd: Password for grade management system.
        :param module_name: Module to check.
        :return: True if grade is published, False otherwise.
        """
        # open grade management system
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(website_url)
            driver.implicitly_wait(3)
        except Exception as e:
            logging.error(e)
            return True

        # execute login
        element = driver.find_element_by_id(cfg.USERNAME_INPUT_ID)
        element.send_keys(user)
        element = driver.find_element_by_id(cfg.PASSWORD_INPUT_ID)
        element.send_keys(passwd)
        element.send_keys(Keys.RETURN)
        time.sleep(1)

        # navigate through grade management system
        for anchor in cfg.NAVIGATION_XPATHS:
            element = driver.find_element(By.XPATH, anchor)
            element.click()
            time.sleep(1)

        # check if html content contains module
        element = driver.find_element_by_id(cfg.CONTENT_ELEM_ID)
        time.sleep(1)
        html_source = element.get_attribute('innerHTML')
        grade_published = module_name not in html_source

        if grade_published:
            logging.info(f"NOTE FÜR {module_name} EINGETRAGEN!")
            open_alert("%s ist eingetragen" % module_name, "Note eingetragen!")
        else:
            logging.info(f"Note für {module_name} nicht eingetragen!")

        # logout, close browser
        element = driver.find_element(By.XPATH, cfg.LOGOUT_XPATH)
        element.click()
        driver.close()

        return grade_published
