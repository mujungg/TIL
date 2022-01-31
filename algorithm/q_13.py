# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #def isPalindrome(self, head: Optional[ListNode]) -> bool:  # 못품

    def solution_01(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        for i in q:
            if i != q.pop():
                return False

        return True

    def solution_04(self, head: Optional[ListNode]) -> bool :
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # while문 다 돌았는데 fast가 none이 아니면 연결리스트가 홀수라는 소리
        # 홀수면 중앙에 중립인 값이 있다는 소리
        # 그 값은 팰린드롬에 검증에 포함시키면 안됨
        # slow로 만든 역 연결리스트와 앞으로 slow가 걸어갈 길을 비교하는데 중립값을 배제
        # 어떻게? slow 한칸 이동
        if fast:
            slow = slow.next

        #팰린드롬 검증
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        # while문 다 았으면 팰린드롬 맞고, rev = None ==> not rev = not False ==> True
        # while문 중간에 빠져나왔으면 팰린드롬 아니고, rev = not None ==> not rev = not True ==> False
        return not rev
