# ==============================
#         Information
# ==============================

# Title: 242 - Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Language: Python

# Problem:
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example
    # Input: s = "anagram", t = "nagaram"
    # Output: true

# ==============================
#         Solution
# ==============================

# 0(n * m)
def is_anagram(s, t):
    s_list = [i for i in s]

    for i in t:
        if i not in s_list:
            return False
        s_list.remove(i)

    if s_list:
        return False
    return True


# 0(n)
def is_anagram2(s, t):
    s_map = {}

    for i in s:
        if i not in s_map.keys():
            s_map[i] = 1
        else:
            s_map[i] += 1
    
    for i in t:
        if i in s_map.keys():
            s_map[i] -= 1
        else:
            return False
    
    for i in s_map.values():
        if i != 0:
            return False

    return True


def is_anagram3(s, t):
    s_map, t_map = {}, {}

    for i in s:
        s_map[i] = s_map.get(i, 0) + 1
    
    for i in t:
        t_map[i] = t_map.get(i, 0) + 1
    
    return s_map == t_map


def is_anagram4(s, t):
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagarams"

print(is_anagram(s, t))
print(is_anagram2(s, t))
print(is_anagram3(s, t))
print(is_anagram4(s, t))




