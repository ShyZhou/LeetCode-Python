# Intersection of Two Linked Lists

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = self.getlen(headA)
        len_b = self.getlen(headB)

        if len_a > len_b:
            for i in range(0, len_a - len_b):
                headA = headA.next
        elif len_b > len_a:
            for i in range(0, len_b - len_a):
                headB = headB.next

        while headA is not None and headB is not None:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getlen(self, head):
        cnt = 0
        while head is not None:
            cnt += 1
            head = head.next
        return cnt