# ==============================
#         Information
# ==============================

# Title: 852 - Peak Index in a Mountain Array
# Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Difficulty: Easy
# Language: Python

# Problem:
# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any
# i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... >
# arr[arr.length - 1].

# Example
# Input: arr = [0,1,0]
# Output: 1

# Input: arr = [0,2,1,0]
# Output: 1

# Input: arr = [0,10,5,2]
# Output: 1

# ==============================
#         Solution
# ==============================


# 0(n)
def peak_mountain(arr):
    n = len(arr)
    peak_idx = 1
    if n == 3:
        return 1
    for i in range(1, n-2):
        if arr[peak_idx] < arr[i + 1]:
            peak_idx = i + 1
    return peak_idx


arr = [0, 1, 0]
arr2 = [0, 2, 1, 0]
arr3 = [0, 10, 5, 2]
print(peak_mountain(arr))
print(peak_mountain(arr2))
print(peak_mountain(arr3))


