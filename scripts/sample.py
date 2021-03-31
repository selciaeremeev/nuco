#!/usr/bin/env python
# coding: utf-8
from nuco import Nuco

nuco = Nuco()

nuco.open()
assert nuco.top.wait_for_page()

nuco.top.login.click()
assert nuco.top.entrance.wait_for_page()
