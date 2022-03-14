# -- coding: utf-8 --
'''
链表5：两两交换链表中的节点
medium

思路：
1. 画图！！
2. pre cur post 代表前中后三个node，
3. 从后往前修改节点的next
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res

        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next

        return res.next