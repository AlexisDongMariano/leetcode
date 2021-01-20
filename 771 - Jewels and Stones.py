# ==============================
#         Information
# ==============================

# Title: 771 - Jewels and Stones
# Link: https://leetcode.com/problems/shuffle-the-array/submissions/
# Difficulty: Easy
# Language: Python

# Problem:
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example
    # Input: jewels = "aA", stones = "aAAbbbb"
    # Output: 3

# ==============================
#         Solution
# ==============================

# 0(n * m)
def get_num_of_jewels_in_stones(jewels, stones):
    jewel_occurrence = 0

    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                jewel_occurrence += 1
    
    return jewel_occurrence


# 0(n)
def get_num_of_jewels_in_stones2(jewels, stones):
    jewel_occurrence = 0
    jewels = set(jewels)

    for stone in stones:
        if stone in jewels:
            jewel_occurrence += 1

    return jewel_occurrence



# 0(n)
# Runtime: 20 ms, faster than 99.21% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.2 MB, less than 75.79% of Python3 online submissions for Jewels and Stones.
def get_num_of_jewels_in_stones3(jewels, stones):
    stones_map = {stone:stones.count(stone) for stone in stones}
    jewel_occurrence = 0

    for jewel in jewels:
        if jewel in stones_map:
            jewel_occurrence += stones_map[jewel]

    return jewel_occurrence


jewels = "aA"
stones = "aAAbbbb"
# jewels = "z"
# stones = "ZZ"
print(get_num_of_jewels_in_stones(jewels, stones))
print(get_num_of_jewels_in_stones2(jewels, stones))
print(get_num_of_jewels_in_stones2(jewels, stones))