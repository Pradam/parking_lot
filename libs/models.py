# -*- coding: utf-8 -*-

"""
libs.models
~~~~~~~~~~~~~~~
This module contains the primary objects that power Parking Lot module to store vehicle details.
"""


class Vehicle:

    def __init__(self, slot, registration_no, color):
        self._slot = slot
        self.registration_no = registration_no
        self.color = color

    @property
    def slot(self):
        return self._slot + 1

    @slot.setter
    def slot(self, value):
        self._slot = value
