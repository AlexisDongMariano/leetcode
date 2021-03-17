# ==============================
#         Information
# ==============================

# Title: 1 - Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# You can return the answer in any order.

# Example
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# ==============================
#         Solution
# ==============================

# 0(n^2)
def two_sum(nums, target):
    length = len(nums)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


# 0(n)
def two_sum2(nums, target):
    if not nums:
        return 'list is empty'
    
    if type(target) != int:
        return 'target is not a valid integer'

    values = {}

    for idx, num in enumerate(nums):
        diff = target - num

        if num in values.keys():
            return [values[num], idx]
        else:
            values[diff] = idx
    
    return 'no match'
        

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
print(two_sum2(nums, target))
