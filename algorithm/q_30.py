class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # 모르겠음
    def solution_01(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used:
                start += 1
            else:
                max_length = max(max_length, index+1-start)
            used[char] = index

        return max_length
