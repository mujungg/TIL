class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(), ListNode()
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    '''
    node <-> new <-> node.left 이렇게 사이게 끼우는 형식
    node의 오른쪽에 new를 연결
    따라서 insertFront: add(head), insertLast: add(tail.left)
    '''

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):  # node의 오른쪽 노드를 삭제. 따라서 head 삭제: del(head), tail 삭제: del(tail.left.left)
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.k == self.len:
            return False
        self._add(self.head, ListNode(value))
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.len:
            return False
        self._add(self.tail.left, ListNode(value))
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self._del(self.head)
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self._del(self.tail.left.left)
        self.len -= 1
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.k == self.len
