from typing import List


class Solution01:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

# import itertools
# class Solution02:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(itertools.permutations(nums))


a = Solution01()
print(a.permute([1, 2, 3]))
