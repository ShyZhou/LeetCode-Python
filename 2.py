# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p1, p2, end = l1, l2, l1
        carry = 0
        while p1 and p2:
            s = p1.val + p2.val + carry
            p1.val = s - 10 if s >= 10 else s
            carry = (s >= 10)
            end = p1
            p1, p2 = p1.next, p2.next
        if p2:
            p1 = p2
        end.next = p1
        while p1:
            s = p1.val + carry
            p1.val = s - 10 if s >= 10 else s
            carry = (s >= 10)
            end = p1
            p1 = p1.next
        if carry:
            end.next = ListNode(1)
        return l1

# II

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use two stacks
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        s = 0
        res = ListNode(0)
        while stack1 or stack2:
            if stack1:
                s += stack1.pop()
            if stack2:
                s += stack2.pop()
            res.val = s % 10
            p = ListNode(s / 10)
            p.next = res
            res = p
            s /= 10
        return res.next if res.val == 0 else res
