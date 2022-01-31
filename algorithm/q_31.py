class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        print("freqs = {", end="")
        for key in freqs:
            print(f"{key}:{freqs[key]}")
        print("}")
        if len(freqs) <= k:
            return list(freqs.keys())
        answer = []

        values = list(freqs.values())
        values = sorted(values, reverse=True)[:k]

        print(f"values = {values}")

        for key in freqs:
            print(f"freqs[key] = {freqs[key]}")
            if freqs[key] in values:
                answer.append(key)

        print()
        return answer

    def solution_01(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        # 힙에 음수로 삽입 -> 가장 높은 빈도가 먼저 나옴
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        for _ in range(k):
            topk.append(heapq.heqppop(freqs_heap)[1])

        return topk

    def solution_02(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

