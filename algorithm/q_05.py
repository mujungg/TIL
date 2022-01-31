import collections
from typing import List


class Solution:
    def my_solution(self, strs: List[str]) -> List[List[str]]:
        result = []

        for i in range(0, len(strs)):
            group = [strs[i]]
            del_idx = []

            for j in range(1, len(strs)):
                if sorted(list(strs[i])) == sorted(list(strs[j])):
                    group.append(strs[j])
                    del_idx.append(j)

            for j in del_idx:
                del strs[j]

            result.append(group)

        return result
        # 실패

    def solution_01(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            #정렬하여 딕셔너리 키로 사용
            #value는 그룹
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())