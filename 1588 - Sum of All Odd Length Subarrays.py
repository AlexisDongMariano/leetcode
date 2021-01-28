# ==============================
#         Information
# ==============================

# Title: 1588 - Sum of All Odd Length Subarrays

# Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

# Example
    # Input: arr = [1,4,2,5,3]
    # Output: 58
    # Explanation: The odd-length subarrays of arr and their sums are:
    # [1] = 1
    # [4] = 4
    # [2] = 2
    # [5] = 5
    # [3] = 3
    # [1,4,2] = 7
    # [4,2,5] = 11
    # [2,5,3] = 10
    # [1,4,2,5,3] = 15
    # If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

# ==============================
#         Solution
# ==============================

def sum_length_all_subarrays(arr):
    subarray_sum = 0
    length = len(arr)

    i = 0
    while i <= length-1:
        for j in range(0, length - i):
            subarray_sum += sum(arr[j:(j + i) + 1])
        i += 2
    
    return subarray_sum


arr = arr = [1,4,2,5,3]

print(sum_length_all_subarrays(arr))
