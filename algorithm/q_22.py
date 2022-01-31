class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i in range(len(temperatures)):
            is_zero = True
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    answer.append(j-i)
                    is_zero = False
                    break
            if is_zero:
                answer.append(0)

        return answer
    # 브루트포스 -> TimeLimmit
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):   # i: index, cur: temperature
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
