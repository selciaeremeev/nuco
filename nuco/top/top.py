#!/usr/bin/env python
# coding: utf-8
""" POM class for Top """
from selenium.webdriver.remote.webelement import WebElement

from base.base import Base
from top.entrance.entrance import Entrance


class Top(Base):
    """ POM class for Top """

    @property
    def entrance(self) -> Entrance:
        """ Return Entrance instance """
        return Entrance(self.driver)

    @property
    def user_name(self) -> WebElement:
        """ Returns UserName WebElement """
        return self.driver.find_element_by_id("userName")

    @property
    def login(self) -> WebElement:
        """ Return Login WebElement """
        return self.driver.find_element_by_id("loginButton")
