# -- coding: utf-8 --

'''
链表8： 环形链表
medium

思路：
找准逻辑！

'''




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                p, q = head, slow
                while p != q:
                    p = p.next
                    q = q.next

                return p

        return None