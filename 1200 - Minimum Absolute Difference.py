# ==============================
#         Information
# ==============================

# Title: 1200 - Minimum Absolute Difference
# Link: https://leetcode.com/problems/minimum-absolute-difference/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array of distinct integers arr, find all pairs of elements with
# the minimum absolute difference of any two elements. 

# Return a list of pairs in ascending order(with respect to pairs), each pair
# [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

# Example
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with
# difference equal to 1 in ascending order.

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

# ==============================
#         Solution
# ==============================


def minimum_absolute_difference(arr):
    sorted_arr = sorted(arr, key=lambda x: abs(x))
    # sorted_arr = sorted([abs(i) for i in arr])
    return sorted_arr


arr = [4,2,1,3]
arr2 = [1,3,6,10,15]
arr3 = [3,8,-10,23,19,-4,-14,27]
print(minimum_absolute_difference(arr))
print(minimum_absolute_difference(arr2))
print(minimum_absolute_difference(arr3))
