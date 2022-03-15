# -- coding: utf-8 --


'''
链表第6节：删除链表的倒数第N个节点
medium

双指针法：
1. fast先移动n个，然后slow，fast一起移动
2. 直到fast.next为空，就删除slow.next 即可

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(next=head)
        slow, fast = dummy_node, dummy_node

        while n != 0:
            fast = fast.next
            n -= 1

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy_node.next