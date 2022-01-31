          from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 오른차순으로 정렬하여 조회하기 쉽게 만든다.
        result: List[List[int]] = []

        # ex)[0,1,2,3,4] -> [a,b,~~~~~~~,c] 형태로 인덱스를 설정해 b와 c를 이동해 값을 찾는다.
        for a in range(len(nums) - 2):
            b = a + 1
            c = len(nums) - 1
            # b와 c가 만나면(b가 c를 역전) 반복 끝
            while b < c:
                # print(f"a:{a} b:{b} c:{c}")  # #
                triplet = [nums[a], nums[b], nums[c]]
                # print(f"triplet:{triplet}")  # #
                # triplet의 합이 0이면 중복 검사 후 result에 삽입
                # b 오른쪽으로, c 왼쪽으로 한칸 이동
                if sum(triplet) == 0:
                    if triplet not in result:
                        result.append(triplet)
                        b += 1
                        c += -1
                    else:
                        b += 1
                        c += -1
                # triplet의 합이 0보다 작으면 b 오른쪽 한칸 이동
                # nums는 정렬돼있으므로 sum(triplet)<0 이면 더 큰 수 필요
                elif sum(triplet) < 0:
                    b += 1
                # triplet의 합이 0보다 크면 c 왼쪽 한칸 이동
                # nums는 정렬돼있으므로 sum(triplet)>0 이면 더 작은 수 필요
                elif sum(triplet) > 0:
                    c += -1
        return result

    def threeSum_02(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 오른차순으로 정렬하여 조회하기 쉽게 만든다.
        result: List[List[int]] = []

        # ex)[0,1,2,3,4] -> [a,b,~~~~~~~,c] 형태로 인덱스를 설정해 b와 c를 이동해 값을 찾는다.
        for a in range(len(nums) - 2):
            # 중복 건너뛰기
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b = a + 1
            c = len(nums) - 1
            # b와 c가 만나면(b가 c를 역전) 반복 끝
            while b < c:
                # print(f"a:{a} b:{b} c:{c}")  # #
                triplet = [nums[a], nums[b], nums[c]]
                # print(f"triplet:{triplet}")  # #
                # triplet의 합이 0이면 중복 검사 후 result에 삽입
                # b 오른쪽으로, c 왼쪽으로 한칸 이동
                if sum(triplet) == 0:
                    if triplet not in result:
                        result.append(triplet)
                        b += 1
                        c += -1
                    else:
                        b += 1
                        c += -1
                # triplet의 합이 0보다 작으면 b 오른쪽 한칸 이동
                # nums는 정렬돼있으므로 sum(triplet)<0 이면 더 큰 수 필요
                elif sum(triplet) < 0:
                    b += 1
                # triplet의 합이 0보다 크면 c 왼쪽 한칸 이동
                # nums는 정렬돼있으므로 sum(triplet)>0 이면 더 작은 수 필요
                elif sum(triplet) > 0:
                    c += -1
        return result

    def solution_01(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results

    def solution_02(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue


            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.solution_02(nums))
