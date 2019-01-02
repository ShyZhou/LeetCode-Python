# Add Two Numbers II

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Reverse list first, then add each node
class Solution(object):
    def reverseList(self, l):
        p, q = l, l.next
        p.next = None
        while q:
            t = q.next
            q.next = p
            p = q
            q = t

        return p

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h1 = self.reverseList(l1)
        h2 = self.reverseList(l2)

        rh = None
        p = None
        c = 0
        while h1 and h2:
            s = h1.val + h2.val + c
            if s >= 10:
                c = 1
                s -= 10
            else:
                c = 0

            if p:
                p.next = ListNode(s)
                p = p.next
            else:
                rh = ListNode(s)
                p = rh

            h1 = h1.next
            h2 = h2.next

        while h1:
            s = h1.val + c
            if s >= 10:
                c = 1
                s -= 10
            else:
                c = 0

            if p:
                p.next = ListNode(s)
                p = p.next
            else:
                rh = ListNode(s)
                p = rh
            h1 = h1.next

        while h2:
            s = h2.val + c
            if s >= 10:
                c = 1
                s -= 10
            else:
                c = 0

            if p:
                p.next = ListNode(s)
                p = p.next
            else:
                rh = ListNode(s)
                p = rh
            h2 = h2.next

        if c:
            p.next = ListNode(c)

        return self.reverseList(rh)


# Use Stack to store the reversed list
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        sum = 0
        p = ListNode(0)
        while s1 or s2:
            if s1:
                sum += s1.pop()
            if s2:
                sum += s2.pop()
            p.val = sum % 10
            q = ListNode(sum / 10)
            q.next = p
            p = q
            sum /= 10

        return p if p.val else p.next

# http://bookshadow.com/weblog/2016/10/29/leetcode-add-two-numbers-ii/
# 1. 统计两链表长度s1, s2；最终结果链表长度s = max(s1, s2) （若有进位，则为s+1）
# 2. 将两链表对齐并逐节点求和，记头节点为h（头节点为dummy node，最高位从h.next开始）
# 3. 初始令指针p指向头节点h，执行循环：
#     令指针q = p.next，重复向其下一节点移动，直到q为空或者q.val ≠ 9
#     如果q.val ＞ 9，说明p与q之间的所有节点需要进位，令p向q移动同时修改p.val
#     否则，令p = q
class Solution(object):
    def getSize(self, h):
        l = 0
        while h:
            l += 1
            h = h.next
        return l

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = self.getSize(l1)
        s2 = self.getSize(l2)
        s = max(s1, s2)

        h = p = ListNode(0)
        while s:
            p.next = ListNode(0)
            p = p.next
            if s <= s1:
                p.val += l1.val
                l1 = l1.next
            if s <= s2:
                p.val += l2.val
                l2 = l2.next
            s -= 1

        p = h
        while p:
            q = p.next
            while q and q.val == 9:
                q = q.next
            if q and q.val > 9:
                while p != q:
                    p.val += 1
                    p = p.next
                    p.val -= 10
            else:
                p = q

        return h if h.val else h.next