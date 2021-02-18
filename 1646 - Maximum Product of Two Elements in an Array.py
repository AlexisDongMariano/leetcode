# ==============================
#         Information
# ==============================

# Title: 1646 - Maximum Product of Two Elements in an Array
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Difficulty: Easy
# Language: Python

# Problem:
# Given the array of integers nums, you will choose two different indices i and j of
# that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Example
# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get
# the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

# ==============================
#         Solution
# ==============================


def max_product(nums):
    num_list = nums.copy()
    max1 = max(num_list)
    max1_idx = num_list.index(max1)
    num_list.pop(max1_idx)
    max2 = max(num_list)

    return (max1-1) * (max2-1)


def max_product2(nums):
    max1 = max(nums)
    temp = min(nums)
    max2 = min(nums)

    if len(nums) < 2 or nums is None:
        return 'invalid argument'

    if len(nums) == 2:
        return (nums[0]-1) * (nums[1]-1)

    if nums.count(max1) > 1:
        return (max1-1) ** 2

    for num in nums:
        if num != max1:
            temp = min(num, max1)
            max2 = max(max2, temp)
    
    return (max1-1) * (max2-1)


def max_product3(nums):
    sorted_nums = sorted(nums, reverse=True)
    return (sorted_nums[0]-1) * (sorted_nums[1]-1)


def max_product4(nums):
    max1 = max2 = float('-inf')

    for num in nums:
        if num > max2:
            if num >= max1:
                max1, max2 = num, max1
            else:
                max2 = num
    
    return (max1-1) * (max2-1)


nums = [3,4,5,2]
nums2 = [1,5,4,5]

print(max_product(nums))
print(max_product2(nums))
print(max_product3(nums))
print(max_product4(nums))

print(max_product(nums2))
print(max_product2(nums2))
print(max_product3(nums2))
print(max_product4(nums2))




