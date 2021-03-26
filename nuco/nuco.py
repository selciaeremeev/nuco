#!/usr/bin/env python
# coding: utf-8
""" Application class for Nuco """
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from top.top import Top


class Nuco:
    """ Application class for Nuco """

    def __init__(self) -> None:
        self.driver: WebDriver = webdriver.Chrome()

    @property
    def top(self) -> Top:
        """ Return Top instance """
        return Top(self.driver)

    def open(self) -> None:
        """ Open nuco """
        self.driver.get("https://nuco.moe/")

    def close(self) -> None:
        """ Close nuco """
        self.driver.quit()
