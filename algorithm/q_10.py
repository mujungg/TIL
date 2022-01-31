from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:  #정렬하여 붙어있는 값끼리 짝지을 때 min()의 총 합이 최대
        nums.sort()
        sum = 0
        for i in [n for n in range(len(nums))
                  if n % 2 == 0]:
            sum += min(nums[i], nums[i + 1])
        return sum
    #1번 풀이와 일치

    def solution_02(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum

    def solution_03(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])



sol = Solution()
nums = [1, 4, 3, 2]
print(sol.arrayPairSum(nums))
