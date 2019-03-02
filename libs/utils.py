# -*- coding: utf-8 -*-

"""
parking_lot.utils
~~~~~~~~~~~~~~
This module provides utility functions that are used within Parking Lot module
that are also useful for external consumption.
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



class OperationsOnVehicle:


    @staticmethod
    def create_parking_lot(_input):
        return int(_input[1])

    @staticmethod
    def park(totalParkings, parkingDict, _input):
        if totalParkings > 0:
            free_slot = findParking(parkingDict)
            if free_slot:
                free = free_slot[0]
                parkingDict[free] = Vehicle(slot=free,
                                            registration_no=_input[0],
                                            color=_input[1])
                free += 1
                return free
            return None
        return None

    @staticmethod
    def leave(totalParkings, parkingDict, _input):
        key = int(_input) - 1
        if totalParkings > 0:
            parkingDict[key] = None
            key += 1
            return key
        else:
            return None

    @staticmethod
    def status(totalParkings, parkingDict):
        if totalParkings > 0:
            return ['{0:>8} | {1:>15}  | {2}'.format(value.slot,
                                                     value.registration_no,
                                                     value.color)
                    for value in parkingDict.values()
                    if value]
        else:
            return []


    @staticmethod
    def registration_numbers_for_cars_with_colour(totalParkings,
                                                  parkingDict,
                                                  _input):
        if totalParkings > 0:
            return [value.registration_no
                    for value in parkingDict.values()
                    if value
                    if value.color == _input]
        else:
            return None

    @staticmethod
    def slot_numbers_for_cars_with_colour(totalParkings,
                                          parkingDict,
                                          _input):
        if totalParkings > 0:
            return [str(value.slot)
                    for value in parkingDict.values()
                    if value
                    if value.color == _input]
        else:
            return None

    @staticmethod
    def slot_number_for_registration_number(totalParkings,
                                            parkingDict,
                                            _input):
        if totalParkings > 0:
            data = [str(value.slot)
                    for value in parkingDict.values()
                    if value
                    if value.registration_no == _input]
            if not data:
                data = ['Not found']
            return data
        else:
            return None


def findParking(parkingDict):
    free_slot = []
    for index, value in parkingDict.items():
        if value is None:
            free_slot.append(index)
    return free_slot
