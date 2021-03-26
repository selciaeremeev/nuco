#!/usr/bin/env python
# coding: utf-8
""" POM class fot Entrance """
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.base import Base


class Entrance(Base):
    """ POM class fot Entrance """

    @property
    def message(self) -> WebElement:
        """ Return Message WebElement """
        return self.driver.find_element_by_id("msg")

    @property
    def video_streaming(self) -> WebElement:
        """ Return Video Streaming WebElement """
        return self.driver.find_element_by_id("startVideo")

    @property
    def audio_streaming(self) -> WebElement:
        """ Return Audio Streaming WebElement """
        return self.driver.find_element_by_id("startAudio")

    @property
    def auto_listen(self) -> WebElement:
        """ Return Auto Listen WebElement """
        return self.driver.find_element_by_id("checkAllListen")

    @property
    def wa_i(self) -> WebElement:
        """ Return wa_i WebElement """
        return self.driver.find_element_by_id("wa_i")

    @property
    def clear(self) -> WebElement:
        """ Return clear WebElement """
        return self.driver.find_element_by_id("clear")

    @property
    def noise(self) -> WebElement:
        """ Return noise WebElement """
        return self.driver.find_element_by_id("logNoiseButton")

    @property
    def logs(self) -> List[WebElement]:
        """ Return Logs List """
        return self.driver.find_element_by_id("logs").find_elements_by_class_name("flexContainer")
