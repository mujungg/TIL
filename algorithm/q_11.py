from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = []

        for i in range(len(nums)):
            result.append(1)  # result[i] = 1
            for j in range(len(nums)):
                if i != j:  # 인덱스 i를 제외하고
                    result[i] *= nums[j]  # result[i]에 전부 곱함
        return result
    # 타임리밋 걸림. O(n)제약때문.

    def solution_01(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        #왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        #왼쪽 곱셈 값에 오른쪽 곱셈 값 값을 곱
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out


nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))
