# ==============================
#         Information
# ==============================

# Title: 1309 - Decrypt String from Alphabet to Integer Mapping
# Link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# Return the string formed after mapping.

# It's guaranteed that a unique mapping will always exist.

# Example
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

# ==============================
#         Solution
# ==============================

# A. make a dictionary/map of integer - alphabet values
# B. Loop through the input string
# B.1. if current 3 adjacent elements is <= than length
# of the input, interpret it
# B.1.a. if first and second digits are <= to 26 and 3rd element equals to '#',
# get the value from the map and store in a list
# B.1.b. if first and second digits combined is > 26, get the first digit from
# the map and store in a list
# C. convert the list into a string and return

from string import ascii_lowercase

def freq_alphabets(s):
    decrypt = {str(i + 1) if i < 9 else str(i + 1) + '#':v for i, v in enumerate(ascii_lowercase)} 
    n = len(s)
    index = 0
    output = []

    while index < n:
        if index + 2 < n and s[index + 2] == '#':
            code = s[index] + s[index + 1] + '#'

            if code in decrypt:
                output.append(decrypt[code])
                index += 3  

        else:
            output.append(decrypt[s[index]])
            index += 1
        
    return ''.join(output)


def freq_alphabets2(s):
    code_map = {str(i+1):v for i, v in enumerate(ascii_lowercase)}
    n = len(s)
    i = 0
    output = []

    while i < n:
        if i + 2 < n and s[i + 2] == '#':
            output.append(code_map[s[i] + s[i + 1]])
            i += 3
        else:
            output.append(code_map[s[i]])
            i += 1
    
    return ''.join(output)

s = "10#11#12"
s1 = "1326#"

print(freq_alphabets(s))
print(freq_alphabets(s1))

print(freq_alphabets2(s))
print(freq_alphabets2(s1))

