class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = ""
        str_list = []
        for char in s:
            if char not in str_list:
                str_list.append(char)
        str_list.sort()
        for char in str_list:
            result = result+char

        return sorted(result)
    # 사전식 순서가 abc순서인줄 알고 풀었다가 망함...
    # 사진식 순서가 뭔지 알고나니 손댈 용기가 안남.

    def removeDuplicateLetters(self, s: str) -> str:
