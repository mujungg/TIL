from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h = None  # return list header
        t = None  # return list tail
        # l1.val과 l2.val중 더 작은 값으로 head 초기화
        # 더 작은 값은 tail이 선택하고 선택받은 값은 더이상 비교할때 쓰이지 않으므로 l1 or l2 한칸 이동
        if l1.val >= l2.val:
            h = t = l2
            l2 = l2.next
        else:
            h = t = l1
            l1 = l1.next

        while l1 and l2:
            if l1.val >= l2.val:
                tail, tail.next = l2, l2
                l2 = l2.next
            else:
                tail, tail.next = l1, l1
                l1 = l1.next

        # l1 = true이면 tail.next = l1
        # l2 = true이면 tail.next = l2
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return h
    # time limit


    def solution_01(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val) :
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1