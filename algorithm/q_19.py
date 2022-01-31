# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외처리
        if not head or left == right:
            return head

        root = prev = ListNode(next=head)  # prev와 head가 이동하는 풀이이므로 root.next를 리턴
        pre_first = first = None
        idx = 1  # 반복문 한번 돌때마다 +1

        # idx가 right보다 작을때까지 반복
        while idx <= right:
            # 뒤집는 구간
            if left < idx <= right:
                head.next, prev, head = prev, head, head.next
            # 나머지 구간
            else:
                # 뒤집는 구간의 첫번째 노드는 next가 prev가 아님
                if idx == left:
                    pre_first, first = prev, head

                prev, head = head, head.next

            idx += 1

        # 뒤집는 구간의 첫번째 노드는 next가 뒤집기 끝난 직후 노드로 바뀐
        # 뒤집는 구간의 직전 노드는 next가 뒤집는 구간의 원래 마지막 노드로 바뀜
        pre_first.next, first.next = prev, head
        return root.next

    def solution_01(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
