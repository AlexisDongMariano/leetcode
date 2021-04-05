# ==============================
#         Information
# ==============================

# Title: 1710 - Maximum Units on a Truck
# Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Difficulty: Easy
# Language: Python

# Problem:
# You are assigned to put some amount of boxes onto one truck. You are given 
# a 2D array boxTypes, where 
# boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of 
# boxes that can be put on the truck. You can choose any boxes to put on the
# truck as long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.

# Example
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the
# third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

# ==============================
#         Solution
# ==============================


def maximum_units(box_types, truck_size):
    sorted_box_types =  sorted(box_types, key=lambda x: x[1], reverse=True)
    # boxTypes.sort(key=lambda x: -x[1]) # another type for above
    boxes_left = truck_size
    total_units = 0
    for type in sorted_box_types:
        diff = boxes_left - type[0]
        if diff > 0:
            total_units += type[0] * type[1]
            boxes_left = diff
        else:
            total_units += boxes_left * type[1]
            return total_units
    return total_units

# def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#     boxTypes.sort(key=lambda x: -x[1])
#     ans = 0
#     for box, units in boxTypes:
#         if truckSize > box:
#             truckSize -= box
#             ans += box * units
#         else:
#             ans += truckSize * units
#             return ans
#     return ans 


box_types = [[1,3],[2,2],[3,1]]
truck_size = 4
box_types2 = [[5,10],[2,5],[4,7],[3,9]]
truck_size2 = 10
print(maximum_units(box_types, truck_size))
print(maximum_units(box_types2, truck_size2))