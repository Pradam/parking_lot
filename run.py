# -*- coding: utf-8 -*-

from libs.utils import OperationsOnVehicle as ops


totalParkings = 0
parkingDict = {}


def commands(_input):

    global totalParkings, parkingDict

    n = [val.strip() for val in _input.split()]

    data = n[0]

    if data == 'create_parking_lot':
        totalParkings = ops.create_parking_lot(n)
        parkingDict.update({value: None for value in range(totalParkings)})
        print(f"Created a parking lot with {totalParkings} slots.")

    elif data == 'park':
        slotNumber = ops.park(totalParkings, parkingDict, n[1:])
        if slotNumber:
            print(f"Allocated slot number: {slotNumber}")
        else:
            print("Sorry, parking lot is full")

    elif data == 'leave':
        slotNumber = ops.leave(totalParkings, parkingDict, n[1])
        if slotNumber:
            print(f"Slot number {slotNumber} is free.")
        else:
            print("Sorry, parking lot is full")

    elif data == 'status':
        values = ops.status(totalParkings, parkingDict)
        if values:
            print("{0} | {1} | {2}".format('Slot No.',
                                           'Registration No.',
                                           'Color'))
            print(*values, sep="\n")
        else:
            print("Sorry, parking lot is empty")

    elif data == 'registration_numbers_for_cars_with_colour':
        regNum = ops.registration_numbers_for_cars_with_colour(totalParkings,
                                                               parkingDict,
                                                               n[1])
        if regNum:
            print(', '.join(regNum))
        else:
            print('Sorry, No record found for color ', n[1])

    elif data == 'slot_numbers_for_cars_with_colour':
        slotNumber = ops.slot_numbers_for_cars_with_colour(totalParkings,
                                                           parkingDict,
                                                           n[1])
        if slotNumber:
            print(', '.join(slotNumber))
        else:
            print('Sorry, No record found for color ', n[1])

    elif data == 'slot_number_for_registration_number':
        slotNumber = ops.slot_number_for_registration_number(totalParkings,
                                                             parkingDict,
                                                             n[1])
        if slotNumber:
            print(*slotNumber)
        else:
            print('Sorry, No record found for Registration No. ', n[1])

    else:
        print('Invalid Command')


if __name__ == '__main__':

    print('*' * 70)
    print('Welcome to Parking Lot Console.')
    print('*' * 70)
    while True:
        prompt = input("Input: ")
        if prompt != 'exit':
            commands(prompt)
        else:
            break
