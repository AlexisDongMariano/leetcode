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


# 0(n) but uses more memory
def sort_by_parity(A):
    odd = []
    output = []
    for num in A:
        output.append(num) if num % 2 == 0 else odd.append(num)
    output.extend(odd)
    return output


# 0(logN), not the fastest but cleaner and elegant
def sort_by_parity2(A):
    return sorted(A, key=lambda x: x % 2)


# 0(n), efficient as well with memory, uses 2 pointer
def sort_by_parity3(A):
    l, r = 0, len(A) - 1
    while l <= r:
        if A[l] % 2 == 0:
            l += 1
        else:
            A[l], A[r] = A[r], A[l]
            r -= 1
    return A


A = [3, 1, 2, 4]
print(sort_by_parity(A))
print(sort_by_parity2(A))
print(sort_by_parity3(A))




