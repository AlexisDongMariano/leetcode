# ==============================
#         Information
# ==============================

# Title: 961 - N-Repeated Elements in Size 2N Array
# Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Difficulty: Easy
# Language: Python

# Problem:
# In a array A of size 2N, there are N+1 unique elements, and exactly one of 
# these elements is repeated N times.

# Example
# Input: [1,2,3,3]
# Output: 3

# ==============================
#         Solution
# ==============================


def repeated_n_times(arr):
    nums = {}
    for i in arr:
        if i not in nums:
            nums[i] = 1
        else:
            return i


arr = [1, 2, 3, 3]
arr2 = [2, 1, 2, 5, 3, 2]
print(repeated_n_times(arr))
print(repeated_n_times(arr2))


