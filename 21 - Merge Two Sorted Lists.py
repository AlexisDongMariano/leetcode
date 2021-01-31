# ==============================
#         Information
# ==============================

# 21 - Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Language: Python

# Problem:
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Example
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# ==============================
#         Solution
# ==============================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_li = []
        
        # generate a list from the values of two linked lists
        while l1:
            new_li.append(l1.val)
            l1 = l1.next
        
        while l2:
            new_li.append(l2.val)
            l2 = l2.next
        
        # sort the new list
        new_li = sorted(new_li)
        
        # if the new list has no contents, return None
        if not new_li:
            return None
        
        # convert the contents of the list to a new linked list
        l3 = ListNode(new_li[0])
        last = l3
        for i in range(1, len(new_li)):
            node = ListNode(new_li[i])
            
            while last.next:
                last = last.next
                
            last.next = node
            
        return l3




