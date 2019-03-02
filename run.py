# -*- coding: utf-8 -*-

from libs.utils import OperationsOnVehicle as ops


if __name__ == '__main__':

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
            width = 5
            values = ops.status(totalParkings, parkingDict)
            if values:
                print(*values, sep="\n")
            else:
                print("Sorry, parking lot is empty")

    while True:
        prompt = input("Input: ")
        if prompt != 'exit':
            commands(prompt)
        else:
            break
