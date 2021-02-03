# ==============================
#         Information
# ==============================

# Title: 804 - Unique Morse Code Words
# Link: https://leetcode.com/problems/unique-morse-code-words/
# Difficulty: Easy
# Language: Python

# Problem:
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots
# and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",
# ".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-...").
# We'll call such a concatenation, the transformation of a word.
# Return the number of different transformations among all words we have.

# Example
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".

# ==============================
#         Solution
# ==============================
from string import ascii_lowercase

def transform_to_morse(word):
    # create a map that for each character has equivalent morse code
    morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
    ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_map = dict(zip(ascii_lowercase, morse_list))

    # store each morse code for every character in a list
    morse_output = []
    for c in word:
        morse_output.append(morse_map[c])
    
    # return the string version of transformed input
    return ''.join(morse_output)


def get_unique_morse_transformations(words):
    transformation_set = set()

    for word in words:
        transformation_set.add(transform_to_morse(word))

    return len(transformation_set)


words = ["gin", "zen", "gig", "msg"]

print(get_unique_morse_transformations(words))



