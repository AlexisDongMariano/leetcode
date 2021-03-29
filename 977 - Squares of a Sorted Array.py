# ==============================
#         Information
# ==============================

# Title: 1 - Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.

# Example
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# ==============================
#         Solution
# ==============================


# 0(nlogn) because of tim sort
def sorted_squares(nums):
    output = []
    for i in nums:
        output.append(i*i)
    return sorted(output)


# one-liner version of above
def sorted_squares2(nums):
    return sorted([i*i for i in nums])


# 0(n) - uses two pointer algorithm
def sorted_squares3(nums):
    output = [None for _ in nums]
    l, r = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[l]) > abs(nums[r]):
            output[i] = nums[l] ** 2
            l += 1
        else:
            output[i] = nums[r] ** 2
            r -= 1
    return output


nums = [-4,-1,0,3,10]
print(sorted_squares(nums))
print(sorted_squares2(nums))
print(sorted_squares3(nums))
