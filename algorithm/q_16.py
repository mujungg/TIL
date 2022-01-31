class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None
        carry = 0  # 받아올림

        while True:
            # l1과 l2가 None이고 받아올림이 없으면 끝
            if (l1 is None) and (l2 is None) and (carry == 0):
                break

            # 두 노드 중 하나가 None어도 연산을 이어가야함
            # None인 경우 0으로 계산
            # 따라서 하나만 None인 경우, 둘 다 None인 경우, 둘다 not None인 경우 연산을 달리 진행
            # None인 경우 다음 노드로 더이상 이동 할 필요도, 이동할 수도 없기 때문에 이동하는 연산도 달리 진행
            if l1 is not None and l2 is not None:
                n = carry + l1.val + l2.val
                l1, l2 = l1.next, l2.next
            elif l1 is None and l2 is not None:
                n = carry + 0 + l2.val
                l2 = l2.next
            elif l1 is not None and l2 is None:
                n = carry + l1.val + 0
                l1 = l1.next
            else:
                n = carry

            # 받아올린 값 + l1.val + l2.val하여 나온 값을 10으로 나눴을때,
            # 몫은 받아올림 값으로 사용되고, 나머지는 결과 노드의 val로 사용된다.
            value = n % 10
            carry = n // 10

            node = ListNode(value)  # 노드를 만들어준다.

            # 맨 처음 단계에서 결과 리스트의 헤드를 이어준다.
            if head is None:
                head = tail = node
            # 맨 처음이 아니라면 tail을 통해 리스트를 연결해주고, tail은 최신 노드를 가리키게 유지한다.
            else:
                tail.next = node
                tail = node

        return head
