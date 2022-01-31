from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 리스트를 받아서 블럭 양 끝을 구하는 함수
        # 블럭 사이에 물이 고이므로, 양 끝이 0이어도 물은 안고임
        def two_pointer(new_height: List[int]):
            left: int = 0
            right: int = len(new_height) - 1

            # 양 끝에서 하나하나 검증
            # left = right이면 중간에 만났다는 건데 이는 블록이 더.이상 없거나,
            # 하나만 남아서 물이 못고이는 상태
            while left != right:
                if new_height[left] > 0 and new_height[right] > 0:
                    return left, right
                if new_height[left] <= 0:
                    left += 1
                if new_height[right] <= 0:
                    right -= 1
            return left, right

        water = 0  # 고인 물 count하는 변수

        # i = 높이
        # left, right 사이에서
        # 높이별로 0또는 음수인 경우 물이 고일 수 있음
        for i in range(max(height)):
            new_height = [x - i for x in height]  # 리스트에서 높이 인덱스를 빼줘서 한 층씩 검증
            left, right = two_pointer(new_height)  # two_pointer를 통해 양쪽 끝 구함
            if left == right:  # 양 끝이 같으면 더이상 물이 못고이므로 break
                break

            for j in new_height[left:right + 1]:  # 0인 끝을 제외한 물이 고일 수 있는 범위를 떼옴
                if j <= 0:  # 0보다 작으면 물이 고일 수 있음ㅊㅌ
                    water += 1
        return water

    # 타임리밋 스벌..

    def solution_01(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), \
                                  max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    # def solution_02(self, height: List[int]) -> int:


sol = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol.solution_01(height))
