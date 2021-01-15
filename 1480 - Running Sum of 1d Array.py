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
    summation_list = nums[:1]

    for i in range(1, len(nums)):
        sum = 0
        # i + 1 because range stops at provided number -1 ex. given num 5, range is 0 - 4 
        for j in range(i + 1):
            sum += nums[j]
        summation_list.append(sum)
    
    return summation_list
   
# O(n)      
def runningSum2(nums: List[int]) -> List[int]:
    summation_list = []
    
    for num in nums:
        summation_list.append(int((num + 1) * num / 2))
    
    return summation_list


nums = [1,2,3,4] 

print(runningSum(nums))
print(runningSum2(nums))