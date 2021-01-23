# ==============================
#         Information
# ==============================

# Title: 1720 - Decode XORed Array
# Link: https://leetcode.com/problems/decode-xored-array/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# Example
    # Input: n = 5, start = 0
    # Output: 8
    # Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
    # Where "^" corresponds to bitwise XOR operator.

# ==============================
#         Solution
# ==============================


def xor_solution(n, start):
    xor_value = start

    for i in range(1, n):
        xor_value = xor_value ^ (start + 2 * i)

    return xor_value

n = 5
start = 0
n2 = 4
start2 = 3
n3 = 1
start3 = 7

print(xor_solution(n, start))
print(xor_solution(n2, start2))
print(xor_solution(n3, start3))