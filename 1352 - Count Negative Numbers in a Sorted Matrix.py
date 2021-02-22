# ==============================
#         Information
# ==============================

# Title: 1351 - Count Negative Numbers in a Sorted Matrix
# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise
# and column-wise, return the number of negative numbers in grid.

# Example
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# ==============================
#         Solution
# ==============================


def count_negative(grid):
    count = 0
    for i in grid:
        for j in i:
            if j < 0:
                count += 1
    return count


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(count_negative(grid))



