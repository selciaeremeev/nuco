#!/usr/bin/env python
# coding: utf-8
""" Base class for POM """
from loguru import logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    """ Base class for POM """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def wait_for_page(self, max_wait: int = 10) -> bool:
        """ Wait for all elements to be displayed
        Returns:
            bool: True if all elements are displayed, False otherwise
        """
        try:
            return WebDriverWait(self.driver, max_wait).until(expected_conditions.presence_of_all_elements_located)
        except TimeoutException as e:
            logger.error(f"{self.__class__.__name__} page is not displayed", exc_info=e)
