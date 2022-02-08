from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def dfs(length, index, path):
            if len(path) == length:
                result.append(path[:])
                print(f'path = {path}')
                print(f'length = {length}')
                print(f'result = {result}')
                return

            for i in range(index, len(nums)):
                dfs(length, i+1, path+[nums[i]])

        for i in range(1, len(nums)+1):
            dfs(i, 0, [])

        return result

class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

nums = [1, 2, 3, 4, 5]
a = Solution()
print(a.subsets(nums))
