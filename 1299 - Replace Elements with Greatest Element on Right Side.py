# ==============================
#         Information
# ==============================

# Title: 1299 - Replace Elements with Greatest Element on Right Side
# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array arr, replace every element in that array with the greatest element among the
#  elements to its right, and replace the last element with -1.

# After doing so, return the array.

# Example
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# ==============================
#         Solution
# ==============================


# 0(m*n)
def replace_elements(arr):
    n = len(arr)
    for i in range(0, n - 1):
        arr[i] = max(arr[i + 1:n])
    arr[-1] = -1
    return arr


def replace_elements2(arr):
    mx = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], mx = mx, max(mx, arr[i])
    return arr


arr = [17,18,5,4,6,1]
arr2 = [400]
arr3 = [17,18,5,4,6,1]
arr4 = [400]
print(replace_elements(arr))
print(replace_elements(arr2))
print(replace_elements2(arr3))
print(replace_elements2(arr4))

