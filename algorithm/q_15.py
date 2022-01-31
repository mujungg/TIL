class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev
    # 반복문으로 풀이 개쉬움. 재귀로 풀다가 포기하고 해설 보니까 반복문으로도 할수 있어서 풀어봄.

    def solution_01(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node: 다음노드, prev: 현재노드
        def reverse(node: ListNode, prev: ListNode = None):
            # 다음 노드가 없으면 현재 노드 반환
            if not node:
                return prev
            #
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)