# ==============================
#         Information
# ==============================

# Title: 1822 - Sign of the Product of an Array
# Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Difficulty: Easy
# Language: Python

# Problem:
# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values
# in the array nums.

# Return signFunc(product).

# Example
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and 
# signFunc(144) = 1

# ==============================
#         Solution
# ==============================


def array_sign(nums):
    negative_count = 0
    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            negative_count += 1
    if negative_count % 2 == 0:
        return 1
    return -1


nums = [-1,-2,-3,-4,3,2,1]
nums2 = [1,5,0,2,-3]
nums3 = [-1,1,-1,1,-1]
print(array_sign(nums))
print(array_sign(nums2))
print(array_sign(nums3))

