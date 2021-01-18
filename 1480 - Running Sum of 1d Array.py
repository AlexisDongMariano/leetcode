# ==============================
#         Information
# ==============================

# Title: 1480 - Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy
# Language: Python

# Example
    # Input:
    # nums = [1,2,3,4]
    # Output:
    # [1,3,6,10]

# ==============================
#         Solution
# ==============================

from typing import List

# Brute force method, O(n^2)
def runningSum(nums: List[int]) -> List[int]:
    summation_list = []
    summation_list.append(nums[0])

    for i in range(1, len(nums)):
        summation_list.append(summation_list[i - 1] + nums[i])

    return summation_list


nums = [1, 2, 3, 4] 
nums_2 = [1, 1, 1, 1]

print(runningSum(nums))
print(runningSum(nums_2))