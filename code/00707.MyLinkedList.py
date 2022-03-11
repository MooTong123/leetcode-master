# -- coding: utf-8 --

# 单链表
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._size = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._size:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self._size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._size:
            return

        self._size += 1

        add_node = Node(val)
        prev_node, cur_node = None, self._head

        for _ in range(index + 1):
            prev_node, cur_node = cur_node, cur_node.next
        else:
            prev_node.next, add_node.next = add_node, cur_node

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._size:
            self._size -= 1
            prev_node, cur_node = None, self._head
            for _ in range(index + 1):
                prev_node, cur_node = cur_node, cur_node.next
            else:
                prev_node.next, cur_node.next = cur_node.next, None

# 双链表
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head, self._tail = Node(0), Node(0)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    # 根据index返回node
    def _get_node(self, index: int):
        if index >= self._size // 2:
            # 用tail往前找
            node = self._tail
            for _ in range(self._size - index):
                node = node.prev
        else:
            # 用head往后找
            node = self._head
            for _ in range(index + 1):
                node = node.next
        return node

        # 获取链表中第 index 个节点的值。如果索引无效，则返回-1

    def get(self, index: int) -> int:
        if 0 <= index < self._size:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    # 更新一个新点
    def _update(self, prev: Node, next: Node, val: int):
        self._size += 1
        node = Node(val)
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    # 在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点
    def addAtHead(self, val: int) -> None:
        self._update(self._head, self._head.next, val)

    # 将值为 val 的节点追加到链表的最后一个元素
    def addAtTail(self, val: int) -> None:
        self._update(self._tail.prev, self._tail, val)

    # 在链表中的第 index 个节点之前添加值为 val  的节点
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._size:
            return

        node = self._get_node(index)
        self._update(node.prev, node, val)

    # 如果索引 index 有效，则删除链表中的第 index 个节点
    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._size:
            node = self._get_node(index)
            self._size -= 1
            node.prev.next, node.next.prev = node.next, node.prev