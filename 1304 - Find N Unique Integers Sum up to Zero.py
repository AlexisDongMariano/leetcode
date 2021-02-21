# ==============================
#         Information
# ==============================

# Title: 1304 - Find N Unique Integers Sum up to Zero
# Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# ==============================
#         Solution
# ==============================


def sum_zero(n):
    output = []

    if n == 1:
        return [0]

    if n % 2 != 0:
        output.append(0)

    half = n // 2

    for i in range(1, half + 1):
        output.append(i)
        output.append(-i)

    return output


n = 5

print(sum_zero(n))

