# ==============================
#         Information
# ==============================

# Title: 461 - Hamming Distance
# Link: https://leetcode.com/problems/hamming-distance/
# Difficulty: Easy
# Language: Python

# Problem:
# The Hamming distance between two integers is the number of positions at which
#  the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example
# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# ==============================
#         Solution
# ==============================


def hamming_distance(x, y):
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]
    x_n = len(x_bin)
    y_n = len(y_bin)
    output = 0

    if y_n > x_n:
        x_bin = ''.join((y_n - x_n) * ['0']) + x_bin
    else:
        y_bin = ''.join((x_n - y_n) * ['0']) + y_bin
        
    for i in range(len(x_bin)):
        if not x_bin[i] == y_bin[i]:
            output += 1
    return output


x = 1
y = 4
print(hamming_distance(x, y))
