# ==============================
#         Information
# ==============================

# Title: 1534 - Count Good Triplets
# Link: https://leetcode.com/problems/count-good-triplets/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

# Example
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

# ==============================
#         Solution
# ==============================

from itertools import combinations

# brute force 0(n^3) --> bad solution
def count_good_triplets(arr, a, b, c):
    length = len(arr)
    good_count = 0
        
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b \
                and abs(arr[i] - arr[k]) <= c:
                    good_count += 1
    
    return good_count


def count_good_triplets2(arr, a, b, c):
    triplets = list(combinations(arr, 3))
    good_count = 0

    for triplet in triplets:
        if abs(triplet[0] - triplet[1]) <= a and abs(triplet[1] - triplet[2]) <= b \
            and abs(triplet[0] - triplet[2]) <= c:
            good_count += 1
    
    return good_count



arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

print(count_good_triplets(arr, a, b, c))
print(count_good_triplets2(arr, a, b, c))




