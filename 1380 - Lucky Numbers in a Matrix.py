# ==============================
#         Information
# ==============================

# Title: 1380 - Lucky Numbers in a Matrix
# Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a m * n matrix of distinct numbers, return all lucky numbers in the
# matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum
# element in its row and maximum in its column.

# Example
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row
# and the maximum in its column

# ==============================
#         Solution
# ==============================


def lucky_numbers(matrix):
    mi = [min(row) for row in matrix]
    mx = [max(col) for col in zip(*matrix)]
    return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == mx[j]]


matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(lucky_numbers(matrix))