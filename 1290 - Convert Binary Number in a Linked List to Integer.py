# ==============================
#         Information
# ==============================

# Title: 1290 - Convert Binary Number in a Linked List to Integer
# Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Difficulty: Easy
# Language: Python

# Problem:
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Example
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# ==============================
#         Solution
# ==============================

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def get_decimal_value(head):
    binary_list = []

    while head:
        binary_list.append(head.val)
        head = head.next
    
    x = 0
    ans = 0

    for i in reversed(binary_list):
        ans += i * (2 ** x) 
        x += 1
    print(ans)
     

    return binary_list


def get_decimal_value2(head):
    s = 0

    while head:
        s = 2*s + head.val
        print('head:',head.val)
        head = head.next
        print('s:',s)

    return s

    
node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)

node1.next = node2
node2.next = node3

print(get_decimal_value(node1))


