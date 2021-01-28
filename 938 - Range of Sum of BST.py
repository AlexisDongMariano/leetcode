# ==============================
#         Information
# ==============================

# Title: 1720 - Decode XORed Array
# Link: https://leetcode.com/problems/range-sum-of-bst/
# Difficulty: Easy
# Language: Python

# Problem:
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

# Example
    # Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    # Output: 32

# ==============================
#         Solution
# ==============================


# def range_sum_bst(root, low, high):
#     sum_bst = 0

#     for i in root:
#         if i is not None and (i >= low and i <= high):
#             sum_bst += i

#     return sum_bst


# root = [10,5,15,3,7,None,18]
# low = 7
# high = 15

# print(range_sum_bst(root, low, high))



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high):
    sum_bst = 0
    current = root
    stack = []
    
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()

            if current.val is not None and (current.val >= low and current.val <= high):
                sum_bst += current.val

            current = current.right
        else:
            break
            
    return sum_bst


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(1)
root.left.right.left = TreeNode(6)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)

low = 6
high = 10

print(rangeSumBST(root, low, high))
