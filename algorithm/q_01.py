# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 팰린드롬 : 앞뒤가 똑같은 단어나 문장. ex) '소주 만 병만 주소'
import collections
from typing import Deque, re


class Solution:
    def my_slove(self, s: str) -> bool:
        # 대소문자를 구분하지 않으므로 비교를 용이하게 하기위해 전부 소문자로 바꿔준다.
        strs = s.lower()
        char_list = []

        # 입력받은 문자열 중 숫자 또는 문자인 원소를 리스트에 넣어준다.
        for i in strs:
            if i.isalnum():
                char_list.append(i)

        # 리스트 앞 뒤 대칭 원소를 하나하나 비교하여 끝까지 진행되면 True를,
        # 중간에 불일치하면 False를 리턴한다.
        for i in char_list:
            if i != char_list.pop():
                return False

        return True

    def solve_01(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def solve_02(self, s: str) -> bool:
        strs = s.lower()
        char_list: Deque = collections.deque()

        # 입력받은 문자열 중 숫자 또는 문자인 원소를 리스트에 넣어준다.
        for i in strs:
            if i.isalnum():
                char_list.append(i)

        # 리스트 앞 뒤 대칭 원소를 하나하나 비교하여 끝까지 진행되면 True를,
        # 중간에 불일치하면 False를 리턴한다.
        for i in char_list:
            if i != char_list.pop():
                return False

        return True

    def solve_03(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
