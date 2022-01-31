from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # 첫번째 인덱스(0~len)
            for j in range(i + 1, len(nums)):  # 두번째 인덱스(1~len) : 중복 불가
                if nums[i] + nums[j] == target: #모든 조합을 탐색: 브루스 포트 -> 효율 떨어짐
                    return [i, j]
    #1번 풀이와 일치.

    def solution_02(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

    def solution_03(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        #{값: 인덱스} 형태
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
    """
    이건 [3,3]처럼 중복된 값이 포함된 리스트에서 사용 불가아닌교? -> nums_map을 만들때 중복된 키에 대입하면
    뒤에 나온 값이 대입되므로 괜춘.
    """
    def solution_04(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


nums = [2, 7, 3, 15]
target = 9
solution = Solution()
print(solution.solution_01(nums, target))
