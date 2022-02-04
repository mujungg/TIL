from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(idx, element):
            print(f'# dfs({idx},{element}) 실행')
            if len(element) == k:
                answer.append(element[:])
                print(f'if문 진입 - answer:{answer}')
                return

            for i in range(idx, n + 1):
                element.append(i)
                print(f'element = {element}')
                dfs(i+1, element)
                element.pop()

        dfs(1, [])
        return answer


n, k = 4, 3
a = Solution()
print(a.combine(n, k))
