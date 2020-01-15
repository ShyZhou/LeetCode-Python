# Merge K Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Use mergeTwo
# O(nk)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = p.next.next
            else:
                p.next = l2
                l2 = p.next.next
            p = p.next
        p.next = l1 if l1 else l2
        return head.next

    def mergeKLists(self, lists):
        if not lists:
            return []

        end = len(lists) - 1
        while end > 0:
            lists[0] = self.mergeTwoLists(lists[0], lists[end])
            end -= 1
        return lists[0]

# Use heap
# O(nlogk)
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        head = ListNode(0)
        hp = head
        h = []
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, l))

        while h:
            p = heapq.heappop(h)[1]
            hp.next = p
            hp = hp.next
            if p.next:
                heapq.heappush(h, (p.next.val, p.next))
        return head.next
