from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            print(path)
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])
        return result


candidates = [2, 3, 6, 7]
target = 7

a = Solution()
print(a.combinationSum(candidates, target))


# []
# [2]
# [2, 2]
# [2, 2, 2]
# [2, 2, 2, 2]
# [2, 2, 2, 3]
# [2, 2, 2, 6]
# [2, 2, 2, 7]
# [2, 2, 3]
# [2, 2, 6]
# [2, 2, 7]
# [2, 3]
# [2, 3, 3]
# [2, 3, 6]
# [2, 3, 7]
# [2, 6]
# [2, 7]
# [3]
# [3, 3]
# [3, 3, 3]
# [3, 3, 6]
# [3, 3, 7]
# [3, 6]
# [3, 7]
# [6]
# [6, 6]
# [6, 7]
# [7]
# [[2, 2, 3], [7]]
# path의 합이 target을 초과하면 그만 탐색하는것 구현하면 효율이 훨씬 좋아질듯