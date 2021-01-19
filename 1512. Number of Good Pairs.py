# ==============================
#         Information
# ==============================

# Title: 1470 - Shuffle the Array
# Link: https://leetcode.com/problems/shuffle-the-array/submissions/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Example
    # Input: nums = [1,2,3,1,1,3]
    # Output: 4
    # Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# ==============================
#         Solution
# ==============================

import math

# 0(n^2)
def get_num_of_good_pair(nums):
    pair = 0
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                pair += 1
        
    return pair


# 0(n)
def get_num_of_good_pair2(nums):
    # commented below is shorter way to generate the count of every value from the nums list to a dictionary
    # nums_hash = {value:nums.count(value) for value in nums}
    
    pair = 0
    nums_hash = {}

    for i in nums:
        if i in nums_hash.keys():
            nums_hash[i] += 1
        else:
            nums_hash[i] = 1

    for value in nums_hash.values():
        if value > 1:
            pair += math.comb(value, 2)

    return pair


nums = [1,2,3,1,1,3]
print(get_num_of_good_pair(nums))
print(get_num_of_good_pair2(nums))
