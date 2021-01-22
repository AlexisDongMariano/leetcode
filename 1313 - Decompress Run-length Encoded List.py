# ==============================
#         Information
# ==============================

# Title: 1313 - Decompress Run-Length Encoded List
# Link: https://leetcode.com/problems/decompress-run-length-encoded-list/
# Difficulty: Easy
# Language: Python

# ==============================
#         Solution
# ==============================

def decompress_RLE_list(nums):
    output = []

    for i in range(0, len(nums) - 1, 2):
        output += [nums[i + 1]] * nums[i]

    return output


nums = [1, 2, 3, 4]
nums2 = [1,1,2,3]

print(decompress_RLE_list(nums))
print(decompress_RLE_list(nums2))

