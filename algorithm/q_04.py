import collections
from typing import List, re
from typing import Dict


class Solution:
    def my_solution(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()  # case-insensitive -> 전부 소문자로 바꾸기
        letters: str = ""
        # 기호(,.!?)를 뺀, 알파벳과 띄어쓰기만 있는 문장 만들기
        for char in paragraph:
            if char.isalpha() or char == " ":
                letters += char

        str_list: List[str] = letters.split()  # 단어 리스트 만듬
        letters_dict: Dict = {}
        # 각 단어를 key로 갖는 딕셔너리 생성. 중복이면 value 1 커짐. 중복 아니면 value 1.
        for char in str_list:
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1

        # del 함수를 이용해 banned에 속한 단어 삭제
        for word in banned:
            del letters_dict[word]

        # max value의 index를 구하는 과정
        key_list = list(letters_dict.keys())
        value_list = list(letters_dict.values())
        max_idx: int = 0
        max_value: int = 0
        for i in range(len(value_list)):
            if max_value < value_list[i]:
                max_value = value_list[i]
                max_idx = i

        return key_list[max_idx]

    # 결과: runtime error ㅠ

    def solution_01(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)

    def solution_02(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
        counts = collections.defaultdict(int)

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

