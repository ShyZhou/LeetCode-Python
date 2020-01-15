# Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

l1 = ListNode(0)
p = l1
p.next = ListNode(1)
p = p.next
p.next = ListNode(2)
p = p.next
p.next = ListNode(4)

l2 = ListNode(0)
p = l2
p.next = ListNode(1)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)

# p = l1.next
# while p:
#     print(p.val)
#     p = p.next

# p = l2.next
# while p:
#     print(p.val)
#     p = p.next

sol = Solution()
res = sol.mergeTwoLists(l1.next, l2.next)
print(res)
p = res
while p:
    print(p.val)
    p = p.next
