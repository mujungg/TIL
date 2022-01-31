class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head가 노드 하나짜리거나 None이면 그냥 그대로 리턴
        if head is None or head.next is None:
            return head
        # head의 첫번째 노드는 움직일 일이 없으므로 root노드를 따로 생성할 필요가 없다.
        # 하지만 포인터 head가 연결리스트를 이동하므로 첫번째 노드를 가리키는 포인터 root는 필요하다.
        # 마지막 odd 노드가 첫번째 even노드를 가리켜야 하므로 첫번째 even노드(head.next)를 기억한다.
        root = head
        first_even = head.next

        while True:
            even = head.next  # head:홀수 even:짝수

            # even이 None이거나 even.next가 None이면 반복 종료
            if (even is None) or (even.next is None):
                break

            # 홀 짝 각각 다음 홀과 짝을 가리킴
            head.next = head.next.next
            even.next = even.next.next
            # head와 even 모두 다음 홀 짝으로 이동
            head = head.next

        head.next = first_even
        return root
    # 잘품. 어려웠던건 while문의 조건을 정해주는 것.
    # 하지만 even과 evev.next의 경우로 처리해주면 쉽게 해결
