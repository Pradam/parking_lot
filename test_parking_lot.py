# -*- coding: utf-8 -*-

import unittest

from libs.utils import OperationsOnVehicle as ops


def read_file_content():
    commands = {}
    with open('file_input.txt', 'r') as obj:
        data = obj.readlines()
        commands.update({index: val.rstrip('\n')
                         for index, val in enumerate(data)})
    return commands


class TestParkingLotFunction(unittest.TestCase):


    def setUp(self):
        print('*' * 70)
        print('Starting Unit Test')
        print('*' * 70)
        self.content = read_file_content()
        self.totalParkings = 0
        self.parkingDict = {}

    def test_check_commands(self):
        self.assertEqual(self.content[0].split()[0], "create_parking_lot")
        self.assertEqual(self.content[1].split()[0], "park")
        self.assertEqual(self.content[7].split()[0], "leave")
        self.assertEqual(self.content[8], "status")

        # test_create_parking_lot
        self.totalParkings = ops.create_parking_lot(self.content[0].split())
        self.parkingDict.update({value: None for value in range(self.totalParkings)})
        self.assertEqual(self.totalParkings, 6)
        self.assertEqual(len(self.parkingDict), 6)
        print('Created a parking lot with %d' % (self.totalParkings))

        # test_allocating_parking_to_user_1
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[1].split()[1:])
        self.assertEqual(ele, 1)
        print('Allocated slot number: %d' % (ele))

        # test_allocating_parking_to_user_2
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[2].split()[1:])
        self.assertEqual(ele, 2)
        print('Allocated slot number: %d' % (ele))

        # test_allocating_parking_to_user_3
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[3].split()[1:])
        self.assertEqual(ele, 3)
        print('Allocated slot number: %d' % (ele))

        # test_allocating_parking_to_user_4
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[4].split()[1:])
        self.assertEqual(ele, 4)
        print('Allocated slot number: %d' % (ele))

        # test_allocating_parking_to_user_5
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[5].split()[1:])
        self.assertEqual(ele, 5)
        print('Allocated slot number: %d' % (ele))

        # test_allocating_parking_to_user_6
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[6].split()[1:])
        self.assertEqual(ele, 6)
        print('Allocated slot number: %d' % (ele))

        # test_leaveing_from_slot_4
        ele = ops.leave(self.totalParkings, self.parkingDict, self.content[7].split()[1])
        self.assertEqual(ele, 4)
        print('Slot number %d is free' % (ele))

        # test_checking_status
        ele = ops.status(self.totalParkings, self.parkingDict)
        self.assertEqual(len(ele), 5)
        print("{0} | {1} | {2}".format('Slot No.',
                                       'Registration No.',
                                       'Color'))
        print(*ele, sep="\n")

        # test_allocation_parking_to_user_7
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[9].split()[1:])
        self.assertEqual(ele, 4)
        self.assertNotEqual(ele, 7)
        print('Allocated slot number: %d' % (ele))

        # test_allocation_parking_user_8
        ele = ops.park(self.totalParkings, self.parkingDict, self.content[10].split()[1:])
        self.assertEqual(ele, None)
        self.assertNotEqual(ele, 8)
        print('Sorry, parking lot is full')

        # test_registeration_no_for_car_with_white
        ele = ops.registration_numbers_for_cars_with_colour(self.totalParkings,
                                                            self.parkingDict,
                                                            self.content[11].split()[1])
        self.assertEqual(ele[0], 'KA-01-HH-1234')
        self.assertEqual(ele[1], 'KA-01-HH-9999')
        self.assertEqual(ele[2], 'KA-01-P-333')
        print(*ele, sep=', ')

        # test_slot_no_for_cars_with_white_color
        ele = ops.slot_numbers_for_cars_with_colour(self.totalParkings,
                                                    self.parkingDict,
                                                    self.content[12].split()[1])
        self.assertEqual(ele[0], '1')
        self.assertEqual(ele[1], '2')
        self.assertEqual(ele[2], '4')
        print(*ele, sep=', ')

        # test_slot_no_for_reg_no_KA_01_HH_3141
        ele = ops.slot_number_for_registration_number(self.totalParkings,
                                                      self.parkingDict,
                                                      self.content[13].split()[1])
        self.assertEqual(ele[0], '6')
        print(ele[0])

        # test_slot_no_for_reg_no__MH_04_AY_1111
        ele = ops.slot_number_for_registration_number(self.totalParkings,
                                                      self.parkingDict,
                                                      self.content[14].split()[1])
        self.assertEqual(ele[0], 'Not found')
        print(ele[0])

    def tearDown(self):
        print('*' * 70)
        print('End of Testcase')
        print('*' * 70)

if __name__ == '__main__':
    unittest.main()
