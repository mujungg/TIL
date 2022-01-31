class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # head가 none이면 그대로 출력
            return head

        result = head
        l, r = head, head.next  # 입력받은 연결리스트의 첫번째, 두번째 노드를 각각 l, r로 참조

        while l and r:  # 하나라도 none이면 종료
            l.next, r.next = r.next, l  # l, r의 next를 서로 바꿈

            if r.next.next and l.next.next:  # 앞에 노드가 두개 이상 존재하면 이동
                l, r = r.next.next, l.next.next
            else:
                break

        return result

    # 실패
    # 노드를 스왑하는 과정에서 head(result)가 직접 움직인다는 것을 간과.
    # 스왑하는 과정에서 prev.next도 새로 연결해줘하 하는 것을 간과.

    def Solution_02(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head 노드가 직접 움직이므로 head를 그대로 리턴할 수 없음. 빈 노드인 root를 만들고 root.next를 리턴
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next  # prev -> head -> b -> x -> y 순으로 노드 존재
            head.next = b.next  # prev -> head -> x -> y
            b.next = head  # b -> head -> x -> y

            prev.next = b  # prev -> b -> head -> x -> y

            head = head.next
            prev = prev.next.next

        return root.next

    def Solution_03(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
