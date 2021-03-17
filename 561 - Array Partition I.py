# ==============================
#         Information
# ==============================

# Title: 561 - Array Partition I
# Link: https://leetcode.com/problems/array-partition-i/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an integer array nums of 2n integers, group these integers into n pairs
# (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i
# is maximized. Return the maximized sum.

# Example
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.

# ==============================
#         Solution
# ==============================


def array_pair_sum(nums):
    output = 0
    sorted_nums = sorted(nums)
    for i in range(0, len(sorted_nums) - 1, 2):
        output += min(sorted_nums[i], sorted_nums[i + 1])
    return output


def array_pair_sum2(nums):
    sorted_nums = sorted(nums)
    return sum(sorted_nums[::2])


nums = [1, 4, 3, 2]
nums2 = [6,2,6,5,1,2]
print(array_pair_sum(nums))
print(array_pair_sum(nums2))
print(array_pair_sum2(nums))
print(array_pair_sum2(nums2))