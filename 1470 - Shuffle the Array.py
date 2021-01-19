# ==============================
#         Information
# ==============================

# Title: 1470 - Shuffle the Array
# Link: https://leetcode.com/problems/shuffle-the-array/submissions/
# Difficulty: Easy
# Language: Python

# Problem:
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example
    # Input:
    # nums = [2,5,1,3,4,7]
    # n = 3
    # Output:
    # [2,3,5,4,1,7]

# ==============================
#         Solution
# ==============================

# 0(n) but uses more operations and space
def arrange_list(nums, n):
    list_a = nums[:n]
    list_b = nums[n:]

    list_c = [None] * (len(list_a) + len(list_b))

    list_c[::2] = list_a
    list_c[1::2] = list_b

    return list_c


# 0(n) but better in terms of space complexity
# more readable
def arrange_list2(nums, n):
    arranged_list = []
    x, y = 0, n
    
    while y != len(nums):
        arranged_list.append(nums[x])
        arranged_list.append(nums[y])
        x += 1
        y += 1

    return arranged_list


# 0(n) better in simpler
def arrange_list3(nums, n):
    arranged_list = []

    for i in range(n):
        arranged_list.append(nums[i])
        arranged_list.append(nums[n + i])

    return arranged_list


nums = [1,2,3,4,4,3,2,1]
n = 4

print(arrange_list(nums, n))
print(arrange_list2(nums, n))
print(arrange_list3(nums, n))
