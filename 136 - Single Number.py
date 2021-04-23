# ==============================
#         Information
# ==============================

# Title: 53 - Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/description/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# ==============================
#         Solution
# ==============================

# 0(n^2)
def max_subarray(nums):
    max_sum = 0
    length = len(nums)

    if not nums:
        return 'list is empty'
    elif type(nums) != list:
        return 'argument is not a list'

    for i in range(length - 1):
        temp_sum = nums[i]
        for j in range(i + 1, length):
            temp_sum += nums[j]
            max_sum = max(max_sum, temp_sum)
    
    return max_sum


def max_subarray2(nums):
    temp_sum = max_sum = 0

    for num in range(len(nums)):
        temp_sum  = max(temp_sum + nums[num], 0)
        max_sum = max(max_sum, temp_sum)

    if max_sum == 0:
        return max(nums)
    
    return max_sum
        

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [-1, -2, -3, -4, -5, -6]

print(max_subarray(nums))
print(max_subarray2(nums))
print(max_subarray(nums2))
print(max_subarray2(nums2))
