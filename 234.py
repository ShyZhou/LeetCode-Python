# Palindrome Linked List

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        q = self.reverse(slow.next)

        p = head
        while q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

    def reverse(self, head):
        p = head
        while p and p.next:
            q = p.next
            p.next = q.next
            q.next = head
            head = q
        return head