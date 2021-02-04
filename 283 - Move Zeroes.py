# ==============================
#         Information
# ==============================

# Title: 283 - Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/description/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array nums, write a function to move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.

# Example
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# ==============================
#         Solution
# ==============================

# 0(n * m)
def move_zeroes(nums):
    zero_count = nums.count(0)
    length = len(nums)

    for i in range(zero_count):
        for j in range(length - 1 - i):
            if nums[j] == 0:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums


# 0(n * m)
def move_zeroes2(nums):
    zero_count = nums.count(0)

    for i in range(zero_count):
        nums.remove(0)
    
    for i in range(zero_count):
        nums.append(0)
    
    return nums

# 0(n)
def move_zeroes3(nums):
    idx_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[idx_zero] = nums[idx_zero], nums[i]
            idx_zero += 1

    if nums[-1] != 0:
        return '0 not found'
    
    return nums


nums = [0, 1, 0, 3, 12]
nums2 = [0, 0, 1, 2, 0]
nums3 = [1, 2, 3, 4, 5] 


# print(move_zeroes(nums))
# print(move_zeroes(nums2))
# print(move_zeroes2(nums3))

# print(move_zeroes2(nums))
# print(move_zeroes2(nums2))
# print(move_zeroes2(nums3))

# print(move_zeroes3(nums))
# print(move_zeroes3(nums2))
# print(move_zeroes3(nums3))