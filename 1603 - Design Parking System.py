# ==============================
#         Information
# ==============================

# Title: 1603 - Design Parking System
# Link: https://leetcode.com/problems/design-parking-system/
# Difficulty: Easy
# Language: Python

# Problem:
# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: 
# big, medium, and small, with a fixed number of slots for each size.

# Implement the ParkingSystem class:

# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. 
# The number of slots for each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants
#  to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented
#  by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space
#  available, return false, else park the car in that size space and return true.

# Example
# Input:
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# Output:
# [null, true, true, false, false]

# ==============================
#         Solution
# ==============================

class ParkingSystem:
    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        if carType == 1 and self.big:
            self.big -= 1
            return True
        elif carType == 2 and self.medium:
            self.medium -= 1
            return True
        elif carType == 3 and self.small:
            self.small -= 1
            return True

        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# obj = ParkingSystem(1,1,0)
# print(obj.car)
# print(obj.small)
# param_1 = obj.addCar(1)
# print(param_1)
# param_1 = obj.addCar(2)
# print(param_1)
# param_1 = obj.addCar(3)
# print(param_1)
# param_1 = obj.addCar(1)
# print(param_1)
