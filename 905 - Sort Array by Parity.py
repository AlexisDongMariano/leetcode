# ==============================
#         Information
# ==============================

# Title: 905 - Sort Array by Parity
# Link: https://leetcode.com/problems/sort-array-by-parity/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.


# Example
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


# ==============================
#         Solution
# ==============================


def sort_by_parity(A):
    odd = []
    output = []
    for num in A:
        output.append(num) if num % 2 == 0 else odd.append(num)
    output.extend(odd)
    return output


A = [3, 1, 2, 4]
print(sort_by_parity(A))




