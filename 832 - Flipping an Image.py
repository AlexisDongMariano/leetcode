# ==============================
#         Information
# ==============================

# Title: 832 - Flipping an Image 
# Link: https://leetcode.com/problems/flipping-an-image/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a binary matrix A, we want to flip the image horizontally, then invert it,
# and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]



# ==============================
#         Solution
# ==============================

def flip_invert_image(A):
    n = len(A)
    pixel_n = len(A[0])
    pixel_mid_n = len(A[0]) // 2
    
    for i in range(n):
        for j in range(pixel_mid_n):
            temp = A[i][j]
            A[i][j] = A[i][pixel_n - 1 - j]
            A[i][pixel_n - 1 - j] = temp
            
    for i in range(n):
        for j in range(pixel_n):
            A[i][j] = 1 - A[i][j]

    return A


def flip_invert_image2(A):
    # slicing is faster than the method reversed()
    flipped = [i[::-1] for i in A]
    return [[1 - j for j in i] for i in flipped]


def flip_invert_image3(A):
    flipped = [reversed(i) for i in A]
    return [[1 - j for j in i] for i in flipped]



input = [[1,1,0],[1,0,1],[0,0,0]]

# print(flip_invert_image(input))
# print(flip_invert_image2(input))
print(flip_invert_image3(input))